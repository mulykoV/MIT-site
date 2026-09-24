import re
import csv
import io
import requests
from django.db import transaction

from .models import Schedule, Teacher


# ============================================================
# НАЛАШТУВАННЯ
# ============================================================

DAY_ALIASES = {
    "понеділок": "Понеділок",
    "вівторок": "Вівторок",
    "середа": "Середа",
    "четвер": "Четвер",
    "п'ятниця": "П'ятниця",
    "п’ятниця": "П'ятниця",
    "субота": "Субота",
}

# Магістри — окремі мітки; бакалавр НЕ повинен матчитись на "... маг"
COURSE_LABELS = {
    "m1": ["1 курс маг", "1 курс маг.", "магістратура 1", "м1"],
    "m2": ["2 курс маг", "2 курс маг.", "магістратура 2", "м2"],
    "c1": ["1 курс"],
    "c2": ["2 курс"],
    "c3": ["3 курс"],
    "c4": ["4 курс"],
}

TIME_RE = re.compile(
    r"(?P<start>\d{1,2}[:.]\d{2})\s*[-–—]\s*(?P<end>\d{1,2}[:.]\d{2})"
)


# ============================================================
# UTILS
# ============================================================

def _norm(value):
    if value is None:
        return ""
    return (
        str(value)
        .replace("\xa0", " ")
        .replace("\u202f", " ")
        .replace("\u2019", "'")
        .replace("`", "'")
        .strip()
        .lower()
    )


def clean_text(value):
    if value is None:
        return ""
    value = str(value).replace("\xa0", " ").replace("\u202f", " ")
    value = re.sub(r"[ \t]+", " ", value)
    value = re.sub(r"\n+", "\n", value)
    return value.strip()


def parse_time(value):
    value = clean_text(value)
    m = TIME_RE.search(value)
    if not m:
        return None, None
    start = m.group("start").replace(".", ":")
    end = m.group("end").replace(".", ":")
    if len(start) == 4:
        start = "0" + start
    if len(end) == 4:
        end = "0" + end
    return start, end


def detect_day(value):
    n = _norm(value)
    for key, day in DAY_ALIASES.items():
        if key in n:
            return day
    return None


def _header_matches_course(header_text: str, course_id: str) -> bool:
    """
    Суворе порівняння заголовка з course_id.

    - c1..c4: 'N курс' без слова 'маг'
    - m1/m2: потрібна наявність 'маг' / 'магістр' (або коротка мітка м1/м2)
    """
    n = _norm(header_text)
    if not n:
        return False

    labels = COURSE_LABELS.get(course_id, [])
    is_mag = course_id.startswith("m")

    for lab in labels:
        lab_n = _norm(lab)
        if lab_n not in n:
            continue

        # Бакалавр: клітинка з "маг" — чужа
        if not is_mag and ("маг" in n or "магістр" in n):
            continue

        # Магістр: має бути "маг"/"магістр", крім коротких м1/м2
        if is_mag and "маг" not in n and "магістр" not in n and lab_n not in ("м1", "м2"):
            continue

        return True

    return False


# ============================================================
# FETCH CSV
# ============================================================

def fetch_csv_grid(pubhtml_url):
    """
    Google published sheet → CSV.
    """
    if "gid=" in pubhtml_url:
        gid = pubhtml_url.split("gid=")[1].split("&")[0].split("#")[0]
    else:
        gid = "0"

    if "/d/e/" in pubhtml_url:
        base = pubhtml_url.split("/pub")[0]
    elif "/d/" in pubhtml_url:
        base = pubhtml_url.split("/pub")[0]
    else:
        raise ValueError("Невідомий формат URL Google Sheets")

    csv_url = f"{base}/pub?gid={gid}&single=true&output=csv"

    resp = requests.get(
        csv_url,
        timeout=30,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (X11; Linux x86_64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/120.0.0.0 Safari/537.36"
            )
        },
    )
    resp.raise_for_status()

    text = resp.content.decode("utf-8-sig")

    if text.lstrip().startswith("<!") or "does not exist" in text[:500]:
        raise ValueError(
            f"CSV не отримано (можливо лист приватний). URL: {csv_url}"
        )

    reader = csv.reader(io.StringIO(text))
    grid = [list(row) for row in reader]

    if not grid or len(grid) < 5:
        raise ValueError("Порожня або занадто мала CSV-таблиця")

    max_cols = max(len(r) for r in grid)
    for r in grid:
        while len(r) < max_cols:
            r.append("")

    return grid, csv_url


# ============================================================
# COURSE COLUMNS
# ============================================================

def find_course_blocks(grid, target_course_id):
    if target_course_id not in COURSE_LABELS:
        raise ValueError(f"Невідомий course_id: {target_course_id}")

    header_row = grid[1] if len(grid) > 1 else []
    found_cols = []

    for col, val in enumerate(header_row):
        if _header_matches_course(val, target_course_id):
            found_cols.append(col)

    # fallback — перші 5 рядків
    if not found_cols:
        for r_idx in range(min(5, len(grid))):
            for col, val in enumerate(grid[r_idx]):
                if col in found_cols:
                    continue
                if _header_matches_course(val, target_course_id):
                    found_cols.append(col)

    if not found_cols:
        visible = [c for c in header_row if c.strip()]
        raise ValueError(
            f"Курс {target_course_id} не знайдено. Заголовки: {visible}"
        )

    blocks = []
    for subject_col in found_cols:
        # time_col — найближча колонка зліва з часом
        time_col = None
        for c in range(subject_col - 1, max(-1, subject_col - 6), -1):
            hits = 0
            for r in grid[4:40]:
                if c < len(r) and parse_time(r[c])[0]:
                    hits += 1
            if hits >= 2:
                time_col = c
                break
        if time_col is None:
            time_col = max(0, subject_col - 1)

        # day_col — найближча зліва від time
        day_col = None
        for c in range(time_col, max(-1, time_col - 4), -1):
            hits = 0
            for r in grid[4:80]:
                if c < len(r) and detect_day(r[c]):
                    hits += 1
            if hits >= 1:
                day_col = c
                break
        if day_col is None:
            day_col = max(0, time_col - 1)

        # підгрупа з рядків 2–3
        subgroup = ""
        for r_idx in (2, 3):
            if r_idx < len(grid) and subject_col < len(grid[r_idx]):
                raw = clean_text(grid[r_idx][subject_col])
                if raw:
                    m = re.search(r"[/](\d+)\s*$", raw)
                    if m:
                        subgroup = f"Підгрупа {m.group(1)}"
                    elif "підгруп" in _norm(raw):
                        subgroup = raw
                    else:
                        subgroup = raw  # "група МІТм-11"
                    break

        blocks.append({
            "subject_col": subject_col,
            "time_col": time_col,
            "day_col": day_col,
            "subgroup": subgroup,
            "header": header_row[subject_col] if subject_col < len(header_row) else "",
        })

    return blocks


# ============================================================
# PARSE ONE LESSON BLOCK (multi-row)
# ============================================================

def parse_lesson_blob(lines):
    lines = [clean_text(l) for l in lines if clean_text(l)]
    if not lines:
        return None

    full = "\n".join(lines)
    full_n = _norm(full)

    result = {
        "subject": "",
        "type": "Лекція",
        "teacher": "",
        "room": "",
        "link": "",
        "raw": full,
    }

    # link
    for line in lines:
        low = line.lower()
        if any(x in low for x in ("http://", "https://", "meet.google", "zoom.us")):
            result["link"] = line.strip()
            break
        if (
            re.search(r"(?:id|meeting id)\s*[:=]?\s*\d{9,}", low)
            or "passcode" in low
            or "код:" in low
        ):
            if not result["link"]:
                result["link"] = line.strip()

    # type
    if "(лаб)" in full_n or "лаборатор" in full_n:
        result["type"] = "Лабораторна"
    elif "(пр)" in full_n or "практич" in full_n:
        result["type"] = "Практична"
    elif "(сем)" in full_n or "(с)" in full_n or "семінар" in full_n:
        result["type"] = "Семінар"
    elif "(л)" in full_n or "лекці" in full_n:
        result["type"] = "Лекція"

    # teacher
    teacher_patterns = [
        r"[А-ЯІЇЄҐ][а-яіїєґ']+\s+[А-ЯІЇЄҐ][а-яіїєґ']+\s+[А-ЯІЇЄҐ][а-яіїєґ']+",
        r"[А-ЯІЇЄҐ][а-яіїєґ']+\s+[А-ЯІЇЄҐ]\.\s*[А-ЯІЇЄҐ]\.?",
        r"[А-ЯІЇЄҐ][а-яіїєґ']+\s+[А-ЯІЇЄҐ]\.[А-ЯІЇЄҐ]\.?",
        r"(?:доц\.|проф\.|ст\.?\s*викл\.?)\s*[А-ЯІЇЄҐ][А-ЯІЇЄҐа-яіїєґ'\s\.]+",
        r"[А-ЯІЇЄҐ][а-яіїєґ']+\s+[А-ЯІЇЄҐ]\.",
    ]
    for line in lines:
        for pat in teacher_patterns:
            m = re.search(pat, line)
            if m:
                result["teacher"] = m.group(0).strip()
                break
        if result["teacher"]:
            break

    # room
    room_patterns = [
        r"(?:ауд\.?|аудиторія)\s*[\w\-./]+",
        r"(?:каб\.?)\s*[\w\-./]+",
    ]
    for line in lines:
        for pat in room_patterns:
            m = re.search(pat, line, re.IGNORECASE)
            if m:
                result["room"] = m.group(0)
                break
        if result["room"]:
            break

    # subject
    ignore = {result["teacher"], result["link"], result["room"]}
    for line in lines:
        if line in ignore:
            continue
        n = _norm(line)
        if n.startswith("http") or ("zoom" in n and len(line) < 40):
            continue
        if re.fullmatch(r"[\(\)лпрсемлаб\s\d\.т\[\]\,\-–—]+", n):
            continue

        subject = re.sub(
            r"\s*\((л|лаб|пр|с|сем)\)\s*",
            " ",
            line,
            flags=re.IGNORECASE,
        )
        subject = re.sub(r"\s+\d+т\b.*$", "", subject)
        subject = re.sub(r"\s*\[[\d\.\s,\-–—]+\]\s*", " ", subject)
        subject = clean_text(subject)
        if len(subject) >= 3:
            result["subject"] = subject
            break

    if not result["subject"]:
        result["subject"] = lines[0][:255]

    return result


def find_teacher(teacher_str):
    if not teacher_str:
        return None
    teacher_str = clean_text(teacher_str)
    teacher_str = re.sub(
        r"^(доц\.|проф\.|ст\.?\s*викл\.?)\s*",
        "",
        teacher_str,
        flags=re.IGNORECASE,
    ).strip()

    parts = teacher_str.split()
    if not parts:
        return None
    last_name = parts[0]
    qs = Teacher.objects.filter(last_name__iexact=last_name)
    if qs.count() == 1:
        return qs.first()
    if len(parts) > 1:
        initials = re.findall(r"[А-ЯІЇЄҐ]", " ".join(parts[1:]))
        for t in qs:
            if t.first_name and t.first_name[0] in initials:
                return t
    return None


# ============================================================
# EXTRACT LESSONS
# ============================================================

def extract_lessons(grid, blocks, target_course_id):
    lessons = []

    for block in blocks:
        subject_col = block["subject_col"]
        time_col = block["time_col"]
        day_col = block["day_col"]
        subgroup = block["subgroup"]

        current_day = None
        current_start = None
        current_end = None
        blob_lines = []

        def flush():
            nonlocal blob_lines
            if not blob_lines or not current_day or not current_start:
                blob_lines = []
                return
            parsed = parse_lesson_blob(blob_lines)
            blob_lines = []
            if not parsed or not parsed["subject"]:
                return

            teacher_obj = find_teacher(parsed["teacher"])
            external = parsed["teacher"] if not teacher_obj else None

            lessons.append({
                "course_id": target_course_id,
                "day": current_day,
                "timeStart": current_start,
                "timeEnd": current_end,
                "subject": parsed["subject"][:255],
                "type": parsed["type"][:50],
                "teacher": teacher_obj,
                "external_teacher": (external[:150] if external else None),
                "room": (parsed["room"] or parsed["link"] or "")[:100],
                "link": parsed["link"] or None,
                "subgroup": subgroup or None,
            })

        for r_idx in range(4, len(grid)):
            row = grid[r_idx]

            if day_col < len(row):
                d = detect_day(row[day_col])
                if d:
                    flush()
                    current_day = d

            if time_col < len(row):
                start, end = parse_time(row[time_col])
                if start:
                    flush()
                    current_start = start
                    current_end = end

            if subject_col < len(row):
                cell = clean_text(row[subject_col])
                if cell:
                    blob_lines.append(cell)

        flush()

    return lessons


# ============================================================
# PUBLIC API
# ============================================================

def parse_google_sheet(pubhtml_url, target_course_id):
    grid, csv_url = fetch_csv_grid(pubhtml_url)
    blocks = find_course_blocks(grid, target_course_id)
    lessons = extract_lessons(grid, blocks, target_course_id)

    return {
        "source_url": pubhtml_url,
        "csv_url": csv_url,
        "course": target_course_id,
        "blocks": blocks,
        "lessons": lessons,
        "matrix_rows": len(grid),
        "matrix_cols": len(grid[0]) if grid else 0,
    }


@transaction.atomic
def sync_pubhtml_schedule(pubhtml_url, target_course_id, schedule_status):
    try:
        result = parse_google_sheet(pubhtml_url, target_course_id)
        lessons = result["lessons"]

        deleted, _ = Schedule.objects.filter(
            course_id=target_course_id,
            status=schedule_status,
        ).delete()

        objs = [
            Schedule(
                status=schedule_status,
                course_id=les["course_id"],
                day=les["day"],
                timeStart=les["timeStart"],
                timeEnd=les["timeEnd"],
                subject=les["subject"],
                type=les["type"],
                teacher=les["teacher"],
                external_teacher=les["external_teacher"],
                room=les["room"],
                link=les["link"],
                subgroup=les["subgroup"],
            )
            for les in lessons
        ]
        Schedule.objects.bulk_create(objs)

        blocks_info = ", ".join(
            f"col={b['subject_col']} ({b['header']})" for b in result["blocks"]
        )

        return (
            f"✅ Синхронізація успішна!\n\n"
            f"Курс: {target_course_id}\n"
            f"Статус: {schedule_status}\n"
            f"Видалено старих пар: {deleted}\n"
            f"Створено нових пар: {len(objs)}\n"
            f"Блоки: {blocks_info}\n"
            f"Матриця: {result['matrix_rows']}×{result['matrix_cols']}\n"
            f"CSV: {result['csv_url']}"
        )
    except Exception as e:
        return f"❌ ПОМИЛКА ПАРСЕРА:\n\n{type(e).__name__}: {e}"