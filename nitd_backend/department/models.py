from django.db import models
from django.core.exceptions import ValidationError

class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Ім'я")
    last_name = models.CharField(max_length=50, verbose_name="Прізвище")
    patronymic = models.CharField(max_length=50, verbose_name="По батькові", blank=True)
    position = models.CharField(max_length=100, verbose_name="Посада (напр., Доцент)")
    degree = models.CharField(max_length=100, verbose_name="Науковий ступінь", blank=True)
    
    # Контакти
    email = models.EmailField(unique=True, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True, verbose_name="LinkedIn")
    github = models.URLField(blank=True, null=True, verbose_name="GitHub") # Додали GitHub
    
    # Зображення
    photo = models.ImageField(upload_to='teachers/', blank=True, null=True)
    
    bio = models.TextField(blank=True, verbose_name="Біографія")
    
    # Додаємо сортування, щоб виводити завідувача кафедри першим
    order = models.IntegerField(default=100, verbose_name="Порядок сортування (менше число = вище)")

    class Meta:
        ordering = ['order', 'last_name'] # Спочатку за порядком, потім за алфавітом
        verbose_name = "Викладач"
        verbose_name_plural = "Викладачі"

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.patronymic}"


class Course(models.Model):
    DEGREE_CHOICES = [
        ('bsc', 'Бакалавр'),
        ('msc', 'Магістр'),
    ]
    
    CATEGORY_CHOICES = [
        ('mandatory', 'Обов\'язкові компоненти'),
        ('block', 'Вибіркові блоки'),
        ('list', 'Вибір з переліку'),
        ('free', 'Факультативи / Вільний вибір'),
    ]

    title = models.CharField(max_length=200, verbose_name="Назва дисципліни")
    description = models.TextField(verbose_name="Опис", blank=True, null=True)
    
    # Нові поля для фільтрації
    degree = models.CharField(max_length=10, choices=DEGREE_CHOICES, default='bsc', verbose_name="Рівень вищої освіти")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='mandatory', verbose_name="Категорія")
    subcategory = models.CharField(max_length=100, blank=True, verbose_name="Підкатегорія (напр. '1 КУРС' або 'Блок 1')")
    
    # Викладачі (текстом, бо там багато регалій типу "д.т.н., проф.")
    teachers_text = models.CharField(max_length=255, blank=True, verbose_name="Викладачі (ПІБ та регалії)")
    
    # Документи
    rpnd_file = models.FileField(upload_to='syllabi/', blank=True, null=True, verbose_name="РПНД (Файл)")
    syllabus_file = models.FileField(upload_to='syllabi/', blank=True, null=True, verbose_name="Силабус / РП (Файл)")

    # Зв'язок з реальною моделлю викладачів (залишаємо для сторінки дисциплін)
    teachers = models.ManyToManyField('Teacher', related_name='courses', blank=True, verbose_name="Прив'язка до профілів викладачів")

    class Meta:
        verbose_name = "Дисципліна"
        verbose_name_plural = "Дисципліни (Силабуси)"
        ordering = ['degree', 'category', 'subcategory', 'title']

    def __str__(self):
        return f"[{self.get_degree_display()}] {self.title}"

# --- НОВІ МОДЕЛІ ДЛЯ НОВИН ---

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст новини")
    date_posted = models.DateField(auto_now_add=True, verbose_name="Дата публікації")
    
    # Закріплення та сортування
    is_pinned = models.BooleanField(default=False, verbose_name="Закріпити нагорі")
    order = models.IntegerField(default=100, verbose_name="Порядок (менше число = вище)")

    class Meta:
        # Django спочатку покаже закріплені, потім відсортує за order, а потім за свіжістю
        ordering = ['-is_pinned', 'order', '-date_posted']
        verbose_name = "Новина"
        verbose_name_plural = "Новини"

    def __str__(self):
        return self.title


class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/', verbose_name="Фото")
    
    class Meta:
        verbose_name = "Фотографію"
        verbose_name_plural = "Галерея новини"

class Schedule(models.Model):
    COURSE_CHOICES = [
        ('c1', '1 Курс'),
        ('c2', '2 Курс'),
        ('c3', '3 Курс'),
        ('c4', '4 Курс'),
        ('m1', 'Магістратура'),
        ('m2', 'Магістратура 2'),
    ]
    
    DAY_CHOICES = [
        ('Понеділок', 'Понеділок'),
        ('Вівторок', 'Вівторок'),
        ('Середа', 'Середа'),
        ('Четвер', 'Четвер'),
        ('П\'ятниця', 'П\'ятниця'),
        ('Субота', 'Субота'),
    ]

    STATUS_CHOICES = [
        ('week_1', 'Тимчасовий (1 Тиждень)'),
        ('week_2', 'Тимчасовий (2 Тиждень)'),
        ('permanent', 'Постійний розклад'),
    ]

    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='permanent', 
        verbose_name="Статус розкладу"
    )

    course_id = models.CharField(max_length=5, choices=COURSE_CHOICES, verbose_name="Курс")
    day = models.CharField(max_length=20, choices=DAY_CHOICES, verbose_name="День тижня")
    timeStart = models.CharField(max_length=10, help_text="Формат HH:MM (наприклад, 08:40)", verbose_name="Час початку")
    timeEnd = models.CharField(max_length=10, help_text="Формат HH:MM (наприклад, 10:15)", verbose_name="Час закінчення")
    subject = models.CharField(max_length=255, verbose_name="Предмет")
    type = models.CharField(max_length=50, verbose_name="Тип (Лекція, Практика, Лаб)")
    
    # ВИПРАВЛЕНО: Додано null=True, blank=True, щоб SET_NULL працював коректно
    teacher = models.ForeignKey(
        'Teacher', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        verbose_name="Викладач (наша кафедра)"
    )
    
    # 2. Для викладачів з інших кафедр (вводимо ручками)
    external_teacher = models.CharField(
        max_length=150, 
        null=True, 
        blank=True, 
        verbose_name="Викладач (інша кафедра)", 
        help_text="Заповніть, якщо викладача немає в списку нашої кафедри"
    )

    room = models.CharField(max_length=100, verbose_name="Аудиторія (або Google Meet)")
    link = models.URLField(blank=True, null=True, verbose_name="Посилання на онлайн пару")
    subgroup = models.CharField(max_length=20, blank=True, null=True, verbose_name="Підгрупа")

    class Meta:
        verbose_name = "Пара (Розклад)"
        verbose_name_plural = "Розклад занять"
        ordering = ['course_id', 'day', 'timeStart']

    def __str__(self):
        return f"{self.get_course_id_display()} | {self.day} | {self.timeStart} - {self.subject}"

class ScheduleSync(models.Model):
    course_id = models.CharField(max_length=5, choices=Schedule.COURSE_CHOICES, verbose_name="Курс")
    status = models.CharField(max_length=20, choices=Schedule.STATUS_CHOICES, verbose_name="Статус розкладу")
    google_sheet_url = models.URLField(verbose_name="Посилання на Google Таблицю (/pubhtml)", help_text="Вставте сюди посилання на розклад")
    
    sync_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата синхронізації")
    result_message = models.TextField(blank=True, null=True, verbose_name="Результат виконання")

    class Meta:
        verbose_name = "Синхронізація розкладу"
        verbose_name_plural = "Синхронізації (Google Sheets)"

    def __str__(self):
        return f"Синхронізація {self.get_course_id_display()} від {self.sync_date.strftime('%d.%m.%Y %H:%M')}"

class Conference(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва конференції")
    content = models.TextField(verbose_name="Текст / Опис")
    photo = models.ImageField(upload_to='conferences/', blank=True, null=True, verbose_name="Фото")
    link = models.URLField(blank=True, null=True, verbose_name="Посилання на матеріали/реєстрацію")
    date_held = models.DateField(blank=True, null=True, verbose_name="Дата проведення")

    class Meta:
        ordering = ['-date_held']
        verbose_name = "Конференція"
        verbose_name_plural = "Конференції"

    def __str__(self):
        return self.title


class Olympiad(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва олімпіади")
    content = models.TextField(verbose_name="Текст / Опис")
    photo = models.ImageField(upload_to='olympiads/', blank=True, null=True, verbose_name="Фото")
    link = models.URLField(blank=True, null=True, verbose_name="Посилання на реєстрацію/результати")
    date_held = models.DateField(blank=True, null=True, verbose_name="Дата проведення")

    class Meta:
        ordering = ['-date_held']
        verbose_name = "Олімпіада"
        verbose_name_plural = "Олімпіади"

    def __str__(self):
        return self.title


class Textbook(models.Model):
    title = models.CharField(max_length=255, verbose_name="Назва посібника")
    description = models.TextField(verbose_name="Анотація / Опис")
    cover_image = models.ImageField(upload_to='textbooks/', blank=True, null=True, verbose_name="Обкладинка")
    link = models.URLField(blank=True, null=True, verbose_name="Посилання на завантаження/перегляд")
    
    # Зв'язок з нашими викладачами для швидкого вибору
    teachers = models.ManyToManyField(Teacher, related_name='textbooks', blank=True, verbose_name="Автори (з кафедри)")
    # Якщо співавтори з інших кафедр або університетів
    external_authors = models.CharField(max_length=255, blank=True, null=True, verbose_name="Інші автори (вручну)")
    
    publication_year = models.PositiveIntegerField(verbose_name="Рік видання", blank=True, null=True)

    class Meta:
        ordering = ['-publication_year', 'title']
        verbose_name = "Навчальний посібник"
        verbose_name_plural = "Навчальні посібники"

    def __str__(self):
        return self.title


class Curator(models.Model):
    # Використовуємо ті ж самі налаштування курсів, що і в розкладі
    course = models.CharField(max_length=5, choices=Schedule.COURSE_CHOICES, verbose_name="Курс")
    group_name = models.CharField(max_length=50, verbose_name="Назва групи (напр., МІТ-11)", help_text="Залиште порожнім, якщо куратор на весь потік")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='curatorships', verbose_name="Викладач (Куратор)")

    class Meta:
        ordering = ['course', 'group_name']
        verbose_name = "Куратор"
        verbose_name_plural = "Куратори груп"

    def __str__(self):
        return f"{self.group_name or self.get_course_display()} - {self.teacher.last_name} {self.teacher.first_name}"

class EduSection(models.Model):
    title = models.CharField("Назва", max_length=200)
    slug = models.SlugField("Slug (якір)", unique=True)
    intro = models.TextField("Вступний текст", blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)
    show_in_menu = models.BooleanField("Показувати в меню", default=True)
    is_published = models.BooleanField("Опубліковано", default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Розділ освітнього процесу"
        verbose_name_plural = "Освітній процес: розділи"

    def __str__(self):
        return self.title


class EduGroup(models.Model):
    section = models.ForeignKey(EduSection, related_name="groups", on_delete=models.CASCADE)
    title = models.CharField("Назва групи", max_length=250, blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Група посилань"
        verbose_name_plural = "Групи посилань"

    def __str__(self):
        return f"{self.section} → {self.title or 'без назви'}"


class EduLink(models.Model):
    group = models.ForeignKey(EduGroup, related_name="links", on_delete=models.CASCADE)
    title = models.CharField("Текст посилання", max_length=300)
    note = models.CharField("Дрібний підпис (роки тощо)", max_length=100, blank=True)  # "2023 - 2025"
    url = models.URLField("Посилання", blank=True)
    file = models.FileField("Або файл", upload_to="edu/", blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Посилання"
        verbose_name_plural = "Посилання"

    def clean(self):
        if self.url and self.file:
            raise ValidationError("Вкажи або посилання, або файл, не обидва.")

    def __str__(self):
        return self.title


class EduImage(models.Model):  # сертифікати та інші зображення розділу
    section = models.ForeignKey(EduSection, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="edu/images/")
    caption = models.CharField("Підпис", max_length=250, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

class ProgramFeedback(models.Model):
    name = models.CharField(max_length=150, verbose_name="ПІБ")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Повідомлення")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата відправки")

    class Meta:
        verbose_name = "Пропозиція до програми"
        verbose_name_plural = "Пропозиції до програм"
        ordering = ['-created_at']

    def __str__(self):
        return f"Пропозиція від {self.name} ({self.created_at.strftime('%d.%m.%Y')})"

class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('science', 'Наукова діяльність'),
        ('education', 'Навчальний процес'),
        ('students', 'Студентське життя'),
        ('events', 'Івенти та Хакатони'),
    ]

    title = models.CharField(max_length=200, verbose_name="Підпис до фото")
    image = models.ImageField(upload_to='gallery/', verbose_name="Фотографія")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='students', verbose_name="Категорія")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата додавання")
    is_published = models.BooleanField(default=True, verbose_name="Опубліковано")

    class Meta:
        verbose_name = "Фотографія"
        verbose_name_plural = "Галерея"
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"
