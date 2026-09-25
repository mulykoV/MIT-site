<template>
  <main class="page" :style="{ '--accent': currentDegree.color }">
    <div class="grid-bg" aria-hidden="true"></div>

    <div class="wrap">
      <!-- HEADER -->
      <header class="head">
        <div>
          <p class="tag font-pixel">[ АРХІВ ДОКУМЕНТІВ ]</p>
          <h1 class="title">Силабуси та<br /><span class="title__mark">РПНД</span></h1>
        </div>
        <NuxtLink to="/education-process" class="btn font-pixel">← До освітнього процесу</NuxtLink>
      </header>

      <!-- БАКАЛАВРАТ / МАГІСТРАТУРА -->
      <div class="seg" role="group" aria-label="Освітній рівень">
        <button
          v-for="d in degrees" :key="d.id" type="button"
          :class="['seg__b', { on: activeDegree === d.id }]"
          :style="{ '--c': d.color }"
          :aria-pressed="activeDegree === d.id"
          @click="activeDegree = d.id"
        >
          <span class="seg__name font-pixel">&gt; {{ d.label }}</span>
          <span class="seg__n">{{ degreeCount(d.id) }} дисциплін</span>
        </button>
      </div>

      <nav class="jump" aria-label="Швидкий перехід">
        <a href="#coursework" class="font-pixel">↓ Курсове проєктування</a>
        <a href="#practice" class="font-pixel">↓ Виробнича практика</a>
      </nav>

      <div class="layout">
        <!-- САЙДБАР -->
        <aside class="side">
          <label class="search">
            <span class="sr">Пошук за назвою або викладачем</span>
            <input v-model.trim="query" type="search" placeholder="Пошук: назва або викладач…" />
          </label>

          <p class="side__t font-pixel">// Категорії</p>
          <nav class="cats" aria-label="Категорії дисциплін">
            <button
              v-for="cat in categories" :key="cat.id" type="button"
              :class="['cat', { on: !query && activeCategory === cat.id }]"
              :aria-pressed="!query && activeCategory === cat.id"
              @click="query = ''; activeCategory = cat.id"
            >
              <span>{{ cat.name }}</span><b>{{ catCount(cat.id) }}</b>
            </button>
          </nav>
        </aside>

        <!-- СПИСОК -->
        <section class="content" aria-live="polite">
          <p class="result font-pixel">
            <template v-if="query">Знайдено: {{ visible.length }} · «{{ query }}»</template>
            <template v-else>{{ currentDegree.label }} · {{ categoryName }} · {{ visible.length }}</template>
          </p>

          <Transition name="swap" mode="out-in">
            <div :key="viewKey">
              <div v-for="(courses, sub) in grouped" :key="sub" class="group">
                <h3 class="group__h"><span>{{ sub }}</span><em class="font-pixel">{{ courses.length }}</em></h3>

                <ul class="list">
                  <li v-for="(c, i) in courses" :key="c.title + i" class="row">
                    <span class="row__n font-pixel">{{ String(i + 1).padStart(2, '0') }}</span>

                    <div class="row__main">
                      <h4>{{ c.title }}</h4>
                      <p v-if="c.teacher">{{ c.teacher }}</p>
                      <span v-if="query" class="chip font-pixel">{{ catName(c.category) }} · {{ c.subcategory }}</span>
                    </div>

                    <component
                      :is="c.url ? 'a' : 'span'"
                      v-if="c.docType"
                      v-bind="c.url ? { href: c.url, target: '_blank', rel: 'noopener' } : { title: 'Файл ще не додано' }"
                      :class="['doc', 'doc--' + meta(c.docType).cls, { 'doc--off': !c.url }]"
                    >
                      {{ meta(c.docType).label }} <i aria-hidden="true">{{ c.url ? '↗' : '·' }}</i>
                    </component>
                  </li>
                </ul>
              </div>

              <div v-if="!visible.length" class="empty">
                <p class="font-pixel">[ NO_DATA_FOUND ]</p>
                <p>{{ query ? 'За цим запитом нічого не знайдено.' : 'У цій категорії поки немає документів.' }}</p>
                <button v-if="query" type="button" class="btn font-pixel" @click="query = ''">Скинути пошук</button>
              </div>
            </div>
          </Transition>
        </section>
      </div>

      <!-- КУРСОВЕ ПРОЄКТУВАННЯ -->
      <section id="coursework" class="extra" aria-labelledby="cw-title">
        <h2 id="cw-title" class="extra__h"><span class="font-pixel">[ 01 ]</span> Курсове проєктування</h2>
        <div class="cw">
          <article v-for="lvl in coursework" :key="lvl.degree" class="cw__card" :style="{ '--c': lvl.color }">
            <h3 class="cw__top font-pixel">Освітній рівень «{{ lvl.degree }}»</h3>
            <ul class="cw__list">
              <li v-for="it in lvl.items" :key="it.title" class="cw__item">
                <span class="sem font-pixel">{{ it.sem }} сем.</span>
                <div>
                  <h4>{{ it.title }}</h4>
                  <p>У {{ it.sem }} семестрі за навчальним планом — курсова робота</p>
                </div>
              </li>
            </ul>
          </article>
        </div>
      </section>

      <!-- ВИРОБНИЧА ПРАКТИКА -->
      <section id="practice" class="extra" aria-labelledby="pr-title">
        <h2 id="pr-title" class="extra__h"><span class="font-pixel">[ 02 ]</span> Виробнича практика</h2>

        <div class="pr-top">
          <article class="pr-card">
            <h3 class="font-pixel">// Мета виробничої практики</h3>
            <p>{{ practice.goal }}</p>
          </article>
          <article class="pr-card">
            <h3 class="font-pixel">// Завдання</h3>
            <p>{{ practice.task }} <strong>студент повинен:</strong></p>
          </article>
        </div>

        <div class="pr-lists">
          <article class="pr-list pr-list--know">
            <h3 class="font-pixel">Знати:</h3>
            <ul><li v-for="t in practice.know" :key="t">{{ t }}</li></ul>
          </article>
          <article class="pr-list pr-list--can">
            <h3 class="font-pixel">Вміти:</h3>
            <ul><li v-for="t in practice.can" :key="t">{{ t }}</li></ul>
          </article>
        </div>

        <div class="pr-docs">
          <component
            :is="d.url ? 'a' : 'span'"
            v-for="d in practice.docs" :key="d.level"
            v-bind="d.url ? { href: d.url, target: '_blank', rel: 'noopener' } : { title: 'Файл ще не додано' }"
            :class="['doc', 'doc--plan', { 'doc--off': !d.url }]"
          >
            Робоча програма практики · {{ d.level }} <i aria-hidden="true">{{ d.url ? '↗' : '·' }}</i>
          </component>
        </div>
      </section>
    </div>
  </main>
</template>

<script setup>
import { ref, computed } from 'vue';

const activeDegree = ref('bsc');
const activeCategory = ref('mandatory');
const query = ref('');

const degrees = [
  { id: 'bsc', label: 'Бакалаврат', color: '#2563eb' },
  { id: 'msc', label: 'Магістратура', color: '#dc2626' },
];

const categories = [
  { id: 'mandatory', name: "Обов'язкові компоненти" },
  { id: 'block', name: 'Вибіркові блоки' },
  { id: 'list', name: 'Вибір з переліку' },
  { id: 'free', name: 'Факультативи' },
];

const docMeta = {
  'РПНД': { label: 'РПНД', cls: 'plan' },
  'РП': { label: 'РП', cls: 'plan' },
  'Силабус': { label: 'Силабус', cls: 'syl' },
  'Методичні рекомендації': { label: 'Методичні', cls: 'met' },
  'Методичні вказівки': { label: 'Методичні', cls: 'met' },
};
const meta = (t) => docMeta[t] || { label: t, cls: 'plan' };

// Викладачі, що повторюються
const T = {
  kr: 'д.т.н., проф., зав.кафедри Кравченко Ю.В.',
  lesh: 'к.т.н., доцент Лещенко О.О.',
  dakh: 'к.т.н., доцент Дахно Н.Б.',
  myk: 'доктор філософії, асистент Миколайчук В.Р.',
  dud: 'д.т.н., доцент Дуднік А.С.',
  star: 'к.т.н., асистент Старкова О.В.',
  ger: 'к.т.н., доцент Герасименко О.Ю.',
  stav: 'с.н.с., доцент Ставицький С.Д.',
  mah: 'к.т.н., асистент Махович О.І.',
  pl: 'д.т.н., доцент Плющ О.Г.',
};

// [рівень, категорія, підкатегорія, назва, викладач, тип документа, url (необов'язково)]
const rows = [
  // Бакалаври · 1 курс
  ['bsc', 'mandatory', '1 КУРС', 'Вступ до фаху', T.kr, 'РПНД', 'https://drive.google.com/file/u/0/d/1g_FZ7QzbIFWUZmlmhg7hzX0JpIyuypR6/view'],
  ['bsc', 'mandatory', '1 КУРС', 'Основи програмування', T.lesh, 'РПНД'],
  ['bsc', 'mandatory', '1 КУРС', 'Фізика', 'к.ф.-м.н., доцент Подолян А.О.', 'РПНД'],
  ['bsc', 'mandatory', '1 КУРС', 'Вступ до університетських студій', 'к.і.н., доцент Левінець Р.П.', 'РПНД'],
  ['bsc', 'mandatory', '1 КУРС', "Комп'ютерні мережі", T.kr, 'РПНД'],
  ['bsc', 'mandatory', '1 КУРС', 'Теорія алгоритмів', T.ger, 'РПНД'],
  ['bsc', 'mandatory', '1 КУРС', 'Електротехніка та електроніка', T.lesh, 'РПНД'],
  ['bsc', 'mandatory', '1 КУРС', 'Вища математика в інформаційних технологіях', T.dakh, 'РПНД'],
  ['bsc', 'mandatory', '1 КУРС', 'Іноземна мова (Англійська)', 'к.п.н., асистент Степаненко О.І., асистент Гончаренко О.А.', 'РПНД'],
  // 2 курс
  ['bsc', 'mandatory', '2 КУРС', 'Веб-дизайн та веб-програмування', T.myk, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', "Комп'ютерна графіка", T.dud, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Основи схемотехніки', T.lesh, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', "Комп'ютерна логіка та дискретна математика", T.dakh, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Українська та зарубіжна культура', 'д.ф.н., професор Сторожук С.В.', 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Технології безпровідних мереж', `${T.star}, ${T.stav}`, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Основи інформаційної безпеки', T.mah, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Ймовірнісні основи в інформаційних технологіях', T.dakh, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', "Архітектура комп'ютерів", T.lesh, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Обробка даних в інформаційних технологіях', T.myk, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Оптичні транспортні системи та мережі', T.dud, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Технології корпоративних мереж', T.star, 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Науковий образ світу', 'д.ф.-м.н., професор Лозовський В.З. та ін.', 'РПНД'],
  ['bsc', 'mandatory', '2 КУРС', 'Іноземна мова (Англійська)', 'к.п.н., доцент Зеліковька О.О.', 'РПНД'],
  // 3 курс
  ['bsc', 'mandatory', '3 КУРС', 'Теорія систем та системний аналіз', T.kr, 'РПНД'],
  ['bsc', 'mandatory', '3 КУРС', 'Захищені інформаційні технології', T.stav, 'РПНД'],
  ['bsc', 'mandatory', '3 КУРС', 'Інтелектуальний аналіз даних', T.myk, 'РПНД'],
  ['bsc', 'mandatory', '3 КУРС', 'Філософія', 'к.ф.н., доцент Савинська І.В.', 'РПНД'],
  ['bsc', 'mandatory', '3 КУРС', 'Технології програмування', T.ger, 'РПНД'],
  ['bsc', 'mandatory', '3 КУРС', 'Бази даних та інформаційні системи', T.myk, 'РПНД'],
  ['bsc', 'mandatory', '3 КУРС', 'Операційні системи', T.dud, 'РПНД'],
  ['bsc', 'mandatory', '3 КУРС', 'Соціально-політичні студії', 'к.п.н., доцент Теремко В.В.', 'РПНД'],
  // 4 курс
  ['bsc', 'mandatory', '4 КУРС', 'Технології штучного інтелекту', T.kr, 'РПНД'],
  ['bsc', 'mandatory', '4 КУРС', 'Організація баз даних', T.ger, 'РПНД'],
  ['bsc', 'mandatory', '4 КУРС', 'Кібернетична безпека підприємства', T.pl, 'РПНД'],
  ['bsc', 'mandatory', '4 КУРС', 'Побудова систем інтернет речей', T.dud, 'РПНД'],
  ['bsc', 'mandatory', '4 КУРС', 'Системне програмування', T.mah, 'РПНД'],
  ['bsc', 'mandatory', '4 КУРС', 'Виробнича практика', T.kr, 'РП'],
  ['bsc', 'mandatory', '4 КУРС', 'Положення про бакалаврську роботу', 'Комісія', 'Методичні рекомендації'],
  // Блоки
  ['bsc', 'block', 'Блок 1 — Інтернет технології', 'Технології безпровідних мереж', '', 'РПНД'],
  ['bsc', 'block', 'Блок 1 — Інтернет технології', 'Хмарні технології', '', 'РПНД'],
  ['bsc', 'block', 'Блок 1 — Інтернет технології', "Системи зв'язку з рухомими об'єктами", '', 'РПНД'],
  ['bsc', 'block', 'Блок 1 — Інтернет технології', "Об'єктно-орієнтоване програмування", '', 'РПНД'],
  ['bsc', 'block', 'Блок 2 — Мережеві технології', 'Програмні мережі', T.pl, 'Силабус'],
  ['bsc', 'block', 'Блок 2 — Мережеві технології', 'Технології транспортних телекомунікаційних мереж', '', 'Силабус'],
  ['bsc', 'block', 'Блок 2 — Мережеві технології', "Системи мобільного зв'язку", '', 'Силабус'],
  ['bsc', 'block', 'Блок 2 — Мережеві технології', 'Адміністрування телекомунікаційних мереж', '', 'Силабус'],
  // Вибір з переліку
  ['bsc', 'list', 'Перелік №1 (4 семестр)', 'Менеджмент та маркетинг', '', 'РПНД'],
  ['bsc', 'list', 'Перелік №1 (4 семестр)', 'Економіка', '', 'Силабус'],
  ['bsc', 'list', 'Перелік №2 (5 семестр)', 'Захищені інформаційні технології', '', 'РПНД'],
  ['bsc', 'list', 'Перелік №2 (5 семестр)', 'Системи банкової безпеки', '', 'Силабус'],
  ['bsc', 'list', 'Перелік №3 (6 семестр)', 'Екологія', '', 'Силабус'],
  ['bsc', 'list', 'Перелік №4 (6 семестр)', 'Бази даних та інформаційні системи', '', 'Силабус'],
  // Факультативи
  ['bsc', 'free', 'Факультативні курси', 'Іноземна мова (Рівень В1+)', '', ''],
  ['bsc', 'free', 'Факультативні курси', 'Фізична культура', '', ''],
  ['bsc', 'free', 'Факультативні курси', 'Ділова українська мова', '', ''],
  // Магістри
  ['msc', 'mandatory', "Загальні обов'язкові компоненти", 'Методологія та організація наукових досліджень', 'д.т.н., проф. Кравченко Ю.В.', 'РПНД'],
  ['msc', 'mandatory', "Загальні обов'язкові компоненти", 'Нейронні мережі', T.stav, 'РПНД'],
  ['msc', 'mandatory', "Загальні обов'язкові компоненти", 'Проектування телекомунікаційних систем', T.pl, 'РПНД'],
  ['msc', 'mandatory', "Загальні обов'язкові компоненти", 'Широкосмугові технології та телекомунікації', T.star, 'РПНД'],
  ['msc', 'mandatory', "Загальні обов'язкові компоненти", 'Положення про магістерську роботу', 'Комісія', 'Методичні рекомендації'],
  ['msc', 'block', '1 Блок — Інтернет технології', 'Бізнес-аналітика', T.dakh, 'РПНД'],
  ['msc', 'block', '2 Блок — Мережеві технології', 'Сенсорні мережі', 'д.т.н., проф., доцент Дуднік А.С.', 'Силабус'],
];

// ===== Курсове проєктування =====
const coursework = [
  { degree: 'Бакалавр', color: '#2563eb', items: [
    { sem: 'III', title: 'Веб-дизайн та веб-програмування' },
    { sem: 'VII', title: 'Організація баз даних' },
  ] },
  { degree: 'Магістр', color: '#dc2626', items: [
    { sem: 'I', title: 'Проектування телекомунікаційних систем' },
  ] },
];

// ===== Виробнича практика =====
const practice = {
  goal: 'Основною метою виробничої практики є вивчення принципів, методів та засобів організації мережевих та інтернет систем, поглиблення та закріплення теоретичних знань, опанування навичок виконання практичних робіт на виробництві. Переддипломна практика є складовою частиною безперервної практичної підготовки студентів на протязі їх навчання в університеті.',
  task: 'Набуття студентами теоретичних знань і практичних навичок для проектування та реалізації організації мережевих та інтернет систем. В результаті вивчення навчальної дисципліни',
  know: [
    'правила техніки безпеки, протипожежної безпеки та виробничої санітарії на підприємствах;',
    'організаційну і технологічну структуру підприємства, служби контрольно-вимірювальних приладів і автоматики (КВП і А);',
    'схеми функціональних структур керування і технологічних процесів, систему керування підприємством, методи оптимізації, критерії керування, апаратуру автоматизації, передачі даних;',
    'контрольно-вимірювальні прилади, систему організації монтажних і ремонтно-налагоджувальних робіт, методи економії енергоресурсів, економічні показники підприємства, організацію праці.',
  ],
  can: [
    'використовувати набуті в університеті знання в практичній діяльності на підприємстві, закладі, лабораторії;',
    'опрацьовувати науково-технічну літературу і проектну документацію, організовувати і проводити роботи з монтажу, налагодження і ремонту автоматичних систем, мереж, технічних засобів передачі даних, уніфікованих модулів контролерів;',
    "використовувати в інженерній діяльності можливості, що надаються комп'ютерними мережами спеціалізованого і загального призначення;",
    'набути навички організації і проведення робіт пристроїв автоматизованих систем і мереж, виконання експериментальних робіт, пошуку і опрацювання інформації на задану тему, користування науково-технічною літературою, проектною технічною і планово-нормативною документацією.',
  ],
  // Сюди вставляй посилання на робочі програми:
  docs: [
    { level: 'Бакалавр', url: '' },
    { level: 'Магістр', url: '' },
  ],
};

const db = rows.map(([degree, category, subcategory, title, teacher = '', docType = '', url = '']) => (
  { degree, category, subcategory, title, teacher, docType, url }
));

const currentDegree = computed(() => degrees.find((d) => d.id === activeDegree.value));
const catName = (id) => categories.find((c) => c.id === id)?.name ?? '';
const categoryName = computed(() => catName(activeCategory.value));

const pool = computed(() => db.filter((c) => c.degree === activeDegree.value));
const degreeCount = (id) => db.filter((c) => c.degree === id).length;
const catCount = (id) => pool.value.filter((c) => c.category === id).length;

const visible = computed(() => {
  const q = query.value.toLowerCase();
  if (q) return pool.value.filter((c) => `${c.title} ${c.teacher}`.toLowerCase().includes(q));
  return pool.value.filter((c) => c.category === activeCategory.value);
});

const grouped = computed(() => {
  const g = {};
  visible.value.forEach((c) => { (g[c.subcategory] ||= []).push(c); });
  return g;
});

const viewKey = computed(() => `${activeDegree.value}-${query.value ? 'search' : activeCategory.value}`);
</script>

<style scoped>
.page { --ink: #000; --paper: #f4f4f0; --mute: #52525b;
  position: relative; overflow: hidden; min-height: 100vh; padding: clamp(7rem, 12vw, 10rem) 0 6rem;
  background: var(--paper); color: var(--ink); font-family: ui-monospace, 'Courier New', monospace; line-height: 1.5; }
.page *, .page *::before, .page *::after { box-sizing: border-box; }
.page ::selection { background: var(--accent); color: #fff; }
.grid-bg { position: absolute; inset: 0; opacity: .08; pointer-events: none;
  background: linear-gradient(#000 1px, transparent 1px) 0 0 / 40px 40px, linear-gradient(90deg, #000 1px, transparent 1px) 0 0 / 40px 40px; }
.wrap { position: relative; z-index: 1; max-width: 1400px; margin: 0 auto; padding: 0 clamp(1rem, 4vw, 2rem); }
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }

/* Header */
.head { display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 1.5rem; padding-bottom: 2rem; margin-bottom: 2.5rem; border-bottom: 8px solid var(--ink); }
.tag { display: inline-block; margin: 0 0 .75rem; padding: .25rem .6rem; background: var(--ink); color: #fff; font-size: .9rem; letter-spacing: .1em; box-shadow: 4px 4px 0 var(--accent); transition: box-shadow .3s; }
.title { margin: 0; font-size: clamp(2.4rem, 7vw, 5.5rem); font-weight: 900; line-height: .95; letter-spacing: -.04em; text-transform: uppercase; }
.title__mark { display: inline-block; margin-top: .5rem; padding: 0 .3em; background: var(--ink); color: #fff; box-shadow: 8px 8px 0 var(--accent); transition: box-shadow .3s; }

.btn { display: inline-flex; align-items: center; justify-content: center; padding: .85rem 1.4rem; border: 4px solid var(--ink); background: #fff; color: var(--ink);
  font-size: .8rem; text-transform: uppercase; text-decoration: none; cursor: pointer; box-shadow: 4px 4px 0 var(--ink); transition: transform .12s, box-shadow .12s, background .12s, color .12s; }
.btn:hover { background: var(--accent); color: #fff; transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--ink); }
.btn:active { transform: translate(4px, 4px); box-shadow: none; }
:where(.btn, .seg__b, .cat, .search input, .doc):focus-visible { outline: 4px solid #facc15; outline-offset: 3px; }

/* Degree switch */
.seg { display: grid; grid-template-columns: 1fr 1fr; gap: 1.25rem; margin-bottom: 3rem; }
.seg__b { display: flex; flex-direction: column; align-items: flex-start; gap: .3rem; padding: 1.2rem 1.5rem; border: 4px solid var(--ink); background: #fff; color: var(--ink);
  text-align: left; cursor: pointer; box-shadow: 6px 6px 0 var(--ink); transition: transform .15s, box-shadow .15s, background .15s, color .15s; }
.seg__b:hover:not(.on) { background: #e4e4e7; }
.seg__name { font-size: clamp(1.1rem, 2.4vw, 1.6rem); text-transform: uppercase; }
.seg__n { font-size: .8rem; font-weight: 700; opacity: .65; }
.seg__b.on { background: var(--c); color: #fff; transform: translate(6px, 6px); box-shadow: 0 0 0 var(--ink); }
.seg__b.on .seg__n { opacity: .9; }

/* Layout */
.layout { display: grid; grid-template-columns: 290px 1fr; gap: 2.5rem; align-items: start; }
.side { position: sticky; top: 6.5rem; display: flex; flex-direction: column; gap: .8rem; }
.search input { width: 100%; padding: .9rem 1rem; border: 4px solid var(--ink); background: #fff; font: inherit; font-weight: 700; box-shadow: 4px 4px 0 var(--ink); }
.search input:focus { background: #eff6ff; border-color: var(--accent); }
.side__t { margin: 1rem 0 .2rem; padding-bottom: .4rem; border-bottom: 2px solid var(--ink); font-size: .7rem; color: var(--mute); text-transform: uppercase; }
.cats { display: flex; flex-direction: column; gap: .8rem; }
.cat { display: flex; align-items: center; justify-content: space-between; gap: .8rem; padding: .9rem 1rem; border: 4px solid var(--ink); background: #fff; color: var(--ink);
  font: inherit; font-weight: 800; text-align: left; text-transform: uppercase; font-size: .85rem; cursor: pointer; box-shadow: 4px 4px 0 var(--ink); transition: transform .12s, box-shadow .12s, background .12s; }
.cat b { min-width: 1.8rem; padding: .1rem .4rem; background: var(--ink); color: #fff; text-align: center; font-size: .75rem; }
.cat:hover:not(.on) { background: #fef08a; transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--ink); }
.cat.on { background: var(--ink); color: #fff; transform: translate(4px, 4px); box-shadow: none; }
.cat.on b { background: var(--accent); }

/* Content */
.result { margin: 0 0 1.5rem; font-size: .8rem; color: var(--mute); text-transform: uppercase; }
.group { margin-bottom: 3rem; }
.group__h { display: flex; align-items: center; justify-content: space-between; gap: 1rem; margin: 0 0 1.2rem; padding: .7rem 1rem; background: #e4e4e7; border-left: 10px solid var(--accent);
  font-size: clamp(1.3rem, 2.6vw, 1.9rem); font-weight: 900; text-transform: uppercase; letter-spacing: -.01em; }
.group__h em { flex-shrink: 0; padding: .15rem .6rem; background: var(--ink); color: #fff; font-style: normal; font-size: .8rem; }
.list { display: flex; flex-direction: column; gap: 1rem; margin: 0; padding: 0; list-style: none; }

.row { display: grid; grid-template-columns: auto 1fr auto; align-items: center; gap: 1rem 1.25rem; padding: 1.1rem 1.3rem; background: #fff; border: 4px solid var(--ink);
  box-shadow: 4px 4px 0 var(--ink); transition: transform .15s, box-shadow .15s; }
.row:hover { transform: translate(-3px, -3px); box-shadow: 8px 8px 0 var(--accent); }
.row__n { color: #a1a1aa; font-size: 1.1rem; transition: color .15s; }
.row:hover .row__n { color: var(--accent); }
.row__main h4 { margin: 0; font-size: clamp(1rem, 1.7vw, 1.2rem); font-weight: 800; line-height: 1.2; text-transform: uppercase; transition: color .15s; }
.row:hover h4 { color: var(--accent); }
.row__main p { margin: .4rem 0 0; font-size: .85rem; color: var(--mute); }
.chip { display: inline-block; margin-top: .5rem; padding: .15rem .5rem; border: 2px solid var(--ink); font-size: .6rem; text-transform: uppercase; }

.doc { display: inline-flex; align-items: center; gap: .5rem; padding: .55rem .9rem; border: 3px solid var(--ink); color: #fff; font-family: inherit; font-weight: 800; font-size: .75rem;
  text-transform: uppercase; text-decoration: none; white-space: nowrap; transition: background .12s, color .12s, transform .12s; }
.doc i { font-style: normal; transition: transform .15s; }
.doc--plan { background: var(--ink); }
.doc--syl { background: #2563eb; }
.doc--met { background: #dc2626; }
a.doc:hover { background: #facc15; color: #000; }
a.doc:hover i { transform: translate(3px, -3px); }
.doc--off { background: #e4e4e7; color: #71717a; border-style: dashed; cursor: not-allowed; }

.empty { padding: 3.5rem 1.5rem; text-align: center; background: #fff; border: 4px dashed #a1a1aa; }
.empty > * + * { margin-top: .8rem; }
.empty p:first-child { font-size: 1.5rem; color: var(--mute); }

.swap-enter-active, .swap-leave-active { transition: opacity .18s, transform .18s; }
.swap-enter-from { opacity: 0; transform: translateY(12px); }
.swap-leave-to { opacity: 0; transform: translateY(-8px); }

@media (max-width: 1000px) {
  .layout { grid-template-columns: 1fr; gap: 1.5rem; }
  .side { position: static; }
  .cats { flex-direction: row; overflow-x: auto; padding: 0 0 .8rem 0; gap: .8rem; scroll-snap-type: x proximity; }
  .cat { flex: 0 0 auto; scroll-snap-align: start; white-space: nowrap; }
}
@media (max-width: 640px) {
  .seg { grid-template-columns: 1fr; }
  .row { grid-template-columns: 1fr; gap: .6rem; }
  .row__n { display: none; }
  .doc { justify-self: start; }
}
/* Швидкий перехід */
.jump { display: flex; flex-wrap: wrap; gap: .8rem; margin: -1.5rem 0 3rem; }
.jump a { padding: .6rem 1rem; border: 3px solid var(--ink); background: #fff; color: var(--ink); font-size: .75rem; text-transform: uppercase; text-decoration: none;
  box-shadow: 3px 3px 0 var(--ink); transition: transform .12s, box-shadow .12s, background .12s; }
.jump a:hover { background: #facc15; transform: translate(-2px, -2px); box-shadow: 5px 5px 0 var(--ink); }
:global(html) { scroll-behavior: smooth; }

/* Додаткові блоки */
.extra { margin-top: 5rem; scroll-margin-top: 7rem; }
.extra__h { display: flex; align-items: center; gap: 1rem; margin: 0 0 2rem; padding: .8rem 1.2rem; background: var(--ink); color: #fff;
  font-size: clamp(1.5rem, 3.4vw, 2.6rem); font-weight: 900; text-transform: uppercase; letter-spacing: -.02em; box-shadow: 8px 8px 0 var(--accent); transition: box-shadow .3s; }
.extra__h span { color: #facc15; font-size: .5em; }

.cw { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: start; }
.cw__card { background: #fff; border: 4px solid var(--ink); box-shadow: 8px 8px 0 var(--c); }
.cw__top { margin: 0; padding: .9rem 1.2rem; background: var(--c); color: #fff; font-size: 1rem; text-transform: uppercase; }
.cw__list { margin: 0; padding: 0; list-style: none; }
.cw__item { display: flex; align-items: center; gap: 1.1rem; padding: 1.2rem; border-top: 3px dashed #d4d4d8; }
.cw__item:first-child { border-top: 0; }
.sem { flex-shrink: 0; min-width: 4.5rem; padding: .4rem .5rem; border: 3px solid var(--ink); text-align: center; font-size: .8rem; }
.cw__item h4 { margin: 0; font-size: 1.1rem; font-weight: 800; line-height: 1.2; text-transform: uppercase; }
.cw__item p { margin: .3rem 0 0; font-size: .78rem; color: var(--mute); }

.pr-top, .pr-lists { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 2rem; align-items: start; }
.pr-card, .pr-list { padding: 1.5rem; background: #fff; border: 4px solid var(--ink); box-shadow: 6px 6px 0 var(--ink); }
.pr-card h3, .pr-list h3 { margin: 0 0 .9rem; font-size: .8rem; text-transform: uppercase; }
.pr-card h3 { color: var(--accent); }
.pr-card p { margin: 0; font-weight: 500; }
.pr-list--know { box-shadow: 6px 6px 0 #2563eb; }
.pr-list--can { box-shadow: 6px 6px 0 #dc2626; }
.pr-list h3 { font-size: 1.1rem; }
.pr-list ul { display: flex; flex-direction: column; gap: .9rem; margin: 0; padding: 0; list-style: none; }
.pr-list li { position: relative; padding-left: 1.5rem; font-size: .9rem; }
.pr-list li::before { content: '▪'; position: absolute; left: 0; font-weight: 900; }
.pr-docs { display: flex; flex-wrap: wrap; gap: 1rem; }
.pr-docs .doc { white-space: normal; }

@media (max-width: 1000px) { .cw, .pr-top, .pr-lists { grid-template-columns: 1fr; } }
@media (prefers-reduced-motion: reduce) { :global(html) { scroll-behavior: auto; } }
@media (prefers-reduced-motion: reduce) { * { transition-duration: .01ms !important; animation: none !important; } }
</style>