<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-sans selection:bg-purple-600 selection:text-white pb-32 pt-20 lg:pt-28 relative overflow-hidden">
    <!-- Технічна сітка на фоні -->
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#e5e7eb_1px,transparent_1px),linear-gradient(to_bottom,#e5e7eb_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none z-0"></div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10">
      <!-- КОМПАКТНИЙ HEADER -->
      <div class="pb-8 mb-12 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-mono text-purple-600 text-sm md:text-base mb-3 uppercase tracking-widest font-bold">
            [ R&D_COMMAND_CENTER ]
          </div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter leading-[0.85]">
            НАУКОВА <br>
            <span class="text-purple-600">ДІЯЛЬНІСТЬ</span>
          </h1>
        </div>
      </div>

      <!-- СЕКЦІЯ 1: ЛАБОРАТОРІЯ + ГЛІТЧ -->
      <div class="bg-white border-4 border-black shadow-[16px_16px_0px_0px_rgba(0,0,0,1)] flex flex-col lg:flex-row mb-16 relative">
        <div class="absolute -top-5 -right-5 bg-red-600 text-white font-mono font-bold text-xs px-4 py-2 border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] rotate-3 z-20">
          [ TOP_SECRET // МОН УКРАЇНИ ]
        </div>

        <!-- Текст -->
        <div class="lg:w-1/2 p-8 md:p-12 flex flex-col justify-between border-b-4 lg:border-b-0 lg:border-r-4 border-black">
          <div>
            <h2 class="text-3xl md:text-5xl font-black uppercase leading-[0.9] tracking-tight mb-6">
              Лабораторія <br>
              <span class="text-purple-600">інтелектуального</span><br>
              сенсорного моніторингу
            </h2>
            <p class="text-base md:text-lg font-medium text-gray-800 leading-relaxed mb-6">
              У межах фінансування МОН України проєктів прикладних наукових досліджень створена лабораторія супутникової навігації та сенсорного моніторингу.
            </p>
          </div>
          <div class="font-mono text-sm font-bold text-black border-l-4 border-purple-600 pl-5 py-2 bg-purple-50/50">
            Оснащена сучасним обладнанням для експериментального стендового та натурного моделювання систем моніторингу, розвідки, розмінування та автономної навігації (GNSS).
          </div>
        </div>

        <!-- Тільки глітч МІТ -->
        <div class="lg:w-1/2 bg-black relative flex flex-col items-center justify-center p-6 min-h-[320px] overflow-hidden">
          <div class="w-full flex justify-between items-center mb-4 border-b-2 border-zinc-800 pb-2 absolute top-5 px-6">
            <span class="font-mono text-zinc-500 text-xs">decode(payload, key.rotate(t))</span>
            <span class="flex gap-2">
              <span class="w-3 h-3 bg-red-500 rounded-full"></span>
              <span class="w-3 h-3 bg-yellow-500 rounded-full"></span>
              <span class="w-3 h-3 bg-green-500 rounded-full"></span>
            </span>
          </div>

          <div
            class="glitch-text font-mono font-black text-purple-400 whitespace-pre select-none tracking-[0.15em]"
            style="font-size: clamp(3.5rem, 9vw, 6.5rem); line-height: 1;"
            aria-hidden="true"
          >{{ glitchText }}</div>

          <div class="absolute bottom-5 left-6 font-mono text-[10px] text-zinc-600 uppercase">
            return b2ASCII(new Vector4(light.x, light.y, light.z, 1));
          </div>
        </div>
      </div>

      <!-- ПРОЦЕС РОБОТИ (з lab1) -->
      <div class="mb-20">
        <div class="font-mono font-bold text-sm text-gray-500 uppercase tracking-widest mb-6 flex items-center gap-2">
          <span class="text-purple-600 text-lg">/></span> Процес роботи та моделювання
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
          <div
            v-for="stand in hardwareStands"
            :key="stand.file"
            class="group flex flex-col cursor-pointer focus-visible:outline focus-visible:outline-4 focus-visible:outline-purple-600 focus-visible:outline-offset-2"
            role="button"
            tabindex="0"
            @click="openImageModal(stand.file)"
            @keydown.enter="openImageModal(stand.file)"
            @keydown.space.prevent="openImageModal(stand.file)"
          >
            <div class="border-4 border-black aspect-[4/3] bg-zinc-200 mb-3 overflow-hidden shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] group-hover:shadow-[2px_2px_0px_0px_rgba(147,51,234,1)] group-hover:translate-x-1 group-hover:translate-y-1 transition-all">
              <img :src="stand.file" :alt="stand.title" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
            </div>
            <h5 class="font-black uppercase text-sm leading-tight text-gray-900 group-hover:text-purple-600 transition-colors">
              {{ stand.title }}
            </h5>
          </div>
        </div>
      </div>

      <!-- ОФІЦІЙНІ ПОЛОЖЕННЯ (компактно) -->
      <div class="mb-20">
        <div class="font-mono font-bold text-sm text-gray-500 uppercase tracking-widest mb-6 flex items-center gap-3">
          <span class="w-3 h-3 rounded-full bg-red-500"></span> Офіційні положення
        </div>

        <div class="bg-white border-4 border-black shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] p-5 max-w-3xl relative">
          <div class="absolute -top-4 -right-4 bg-red-600 text-white font-mono font-bold text-[10px] px-3 py-1.5 border-2 border-black rotate-6 shadow-[3px_3px_0px_0px_rgba(0,0,0,1)]">
            APPROVED
          </div>

          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
            <div
              v-for="doc in officialDocs"
              :key="doc.file"
              role="button"
              tabindex="0"
              class="group flex items-center gap-4 border-2 border-black bg-[#F4F4F0] p-3 cursor-pointer hover:bg-purple-50 transition-colors focus-visible:outline focus-visible:outline-4 focus-visible:outline-purple-600 focus-visible:outline-offset-2"
              @click="openImageModal(doc.file)"
              @keydown.enter="openImageModal(doc.file)"
              @keydown.space.prevent="openImageModal(doc.file)"
            >
              <div class="w-16 shrink-0 aspect-[3/4] bg-white border-2 border-black overflow-hidden flex items-center justify-center">
                <img :src="doc.file" :alt="doc.alt" class="w-full h-full object-contain">
              </div>
              <div class="flex flex-col gap-1 min-w-0">
                <span class="font-mono font-bold text-xs uppercase tracking-widest">{{ doc.label }}</span>
                <span class="font-mono text-[10px] text-gray-500 uppercase leading-snug">{{ doc.caption }}</span>
                <span class="font-mono text-[10px] text-purple-600 font-bold uppercase group-hover:underline">Відкрити ↗</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- НАУКОВО-ДОСЛІДНІ ПРОЄКТИ -->
      <div class="mb-20">
        <div class="mb-10 flex items-center justify-between border-b-4 border-black pb-5">
          <h3 class="text-3xl md:text-5xl font-black uppercase tracking-tighter">
            Науково-дослідні <span class="text-purple-600">проєкти</span>
          </h3>
          <span class="hidden md:inline-block font-mono font-bold text-sm bg-black text-white px-4 py-2 uppercase">Active Dossiers</span>
        </div>

        <div class="flex flex-col gap-12">
          <!-- ПРОЄКТ КРАВЧЕНКА -->
          <div class="bg-white border-4 border-black shadow-[12px_12px_0px_0px_rgba(147,51,234,1)] flex flex-col overflow-hidden">
            <div class="bg-black text-white px-6 md:px-8 py-5 flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b-4 border-black">
              <h4 class="text-xl md:text-2xl font-black uppercase tracking-tight">
                Проєкт <span class="text-purple-400">Юрія Кравченка</span>
              </h4>
              <span class="font-mono text-sm bg-white text-black px-3 py-1 font-bold tracking-widest w-fit">TRL: 3 → 6</span>
            </div>

            <div class="p-6 md:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8">
              <div class="lg:col-span-6 flex flex-col gap-6">
                <div>
                  <div class="font-mono text-purple-600 font-bold uppercase mb-2 text-sm tracking-widest">Тема дослідження</div>
                  <p class="text-lg md:text-xl font-black uppercase leading-tight">
                    «Методи та засоби інтелектуального забезпечення функціональної стійкості системи розвідки та автономної навігації лінії бойового зіткнення з використанням БПЛА»
                    <span class="text-gray-400 font-normal normal-case text-base">(2025–2027)</span>
                  </p>
                </div>

                <div class="grid gap-5 font-medium text-gray-800 text-sm md:text-base">
                  <div class="flex gap-3">
                    <div class="shrink-0 bg-black text-white font-mono text-xs uppercase px-2 py-1 h-fit mt-0.5">Ідея</div>
                    <p>Поєднання сенсорної системи розвідки та системи автономної навігації, які функціонують у спільному районі та використовують мережу сенсорів і псевдолітів.</p>
                  </div>
                  <div class="flex gap-3">
                    <div class="shrink-0 bg-black text-white font-mono text-xs uppercase px-2 py-1 h-fit mt-0.5">Гіпотеза</div>
                    <p>Комплексна система забезпечить достовірність і оперативність інформації за умови надання їй властивості функціональної стійкості.</p>
                  </div>
                  <div class="flex gap-3">
                    <div class="shrink-0 bg-purple-600 text-white font-mono text-xs uppercase px-2 py-1 h-fit mt-0.5">Результат</div>
                    <p class="font-bold text-black">Створено програмний комплекс «Імітаційна модель комплексної системи сенсорного моніторингу та автономної навігації».</p>
                  </div>
                </div>
              </div>

              <!-- Більші фото -->
              <div class="lg:col-span-6 grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div
                  class="border-4 border-black aspect-video bg-zinc-200 overflow-hidden shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] group cursor-pointer"
                  role="button" tabindex="0"
                  @click="openImageModal('/science-edu-processes/lab5.jpg')"
                  @keydown.enter="openImageModal('/science-edu-processes/lab5.jpg')"
                >
                  <img src="/science-edu-processes/lab5.jpg" alt="Карта та зона покриття" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
                </div>
                <div
                  class="border-4 border-black aspect-video bg-zinc-200 overflow-hidden shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] group cursor-pointer"
                  role="button" tabindex="0"
                  @click="openImageModal('/science-edu-processes/lab6.jpg')"
                  @keydown.enter="openImageModal('/science-edu-processes/lab6.jpg')"
                >
                  <img src="/science-edu-processes/lab6.jpg" alt="Імітаційна модель" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
                </div>
              </div>
            </div>
          </div>

          <!-- ПРОЄКТ ДУДНІКА -->
          <div class="bg-white border-4 border-black shadow-[12px_12px_0px_0px_rgba(34,197,94,1)] flex flex-col overflow-hidden">
            <div class="bg-black text-white px-6 md:px-8 py-5 flex flex-col sm:flex-row sm:items-center justify-between gap-3 border-b-4 border-black">
              <h4 class="text-xl md:text-2xl font-black uppercase tracking-tight">
                Проєкт <span class="text-green-400">Андрія Дудніка</span>
              </h4>
              <span class="font-mono text-sm bg-white text-black px-3 py-1 font-bold tracking-widest w-fit">TRL: 3 → 6</span>
            </div>

            <div class="p-6 md:p-10 grid grid-cols-1 lg:grid-cols-12 gap-8">
              <!-- Більші фото зліва -->
              <div class="lg:col-span-6 grid grid-cols-1 sm:grid-cols-2 gap-4 order-last lg:order-first">
                <div
                  class="border-4 border-black aspect-video bg-zinc-200 overflow-hidden shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] group cursor-pointer"
                  role="button" tabindex="0"
                  @click="openImageModal('/science-edu-processes/lab7.jpg')"
                  @keydown.enter="openImageModal('/science-edu-processes/lab7.jpg')"
                >
                  <img src="/science-edu-processes/lab7.jpg" alt="Стенд бездротової системи" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
                </div>
                <div
                  class="border-4 border-black aspect-video bg-zinc-200 overflow-hidden shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] group cursor-pointer"
                  role="button" tabindex="0"
                  @click="openImageModal('/science-edu-processes/lab8.jpg')"
                  @keydown.enter="openImageModal('/science-edu-processes/lab8.jpg')"
                >
                  <img src="/science-edu-processes/lab8.jpg" alt="Тестування протоколу" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105">
                </div>
              </div>

              <div class="lg:col-span-6 flex flex-col gap-6">
                <div>
                  <div class="font-mono text-green-600 font-bold uppercase mb-2 text-sm tracking-widest">Тема дослідження</div>
                  <p class="text-lg md:text-xl font-black uppercase leading-tight">
                    «Бездротова захищена система мінування/розмінування та моніторингу з інтелектуальним управлінням»
                    <span class="text-gray-400 font-normal normal-case text-base">(2024–2026)</span>
                  </p>
                </div>

                <div class="grid gap-5 font-medium text-gray-800 text-sm md:text-base">
                  <div class="flex gap-3">
                    <div class="shrink-0 bg-black text-white font-mono text-xs uppercase px-2 py-1 h-fit mt-0.5">Мета</div>
                    <p>Синтез роботизованої сенсорної мережі моніторингу надзвичайних ситуацій та розмінування демілітаризованої смуги.</p>
                  </div>
                  <div class="flex gap-3">
                    <div class="shrink-0 bg-black text-white font-mono text-xs uppercase px-2 py-1 h-fit mt-0.5">Завдання</div>
                    <ul class="list-disc pl-4 space-y-1">
                      <li>Аналіз можливостей ШІ для криптографічного захисту даних</li>
                      <li>Розробка методів вибору оптимальних протоколів передачі</li>
                      <li>Тестування статистичних характеристик протоколів із використанням ML</li>
                      <li>Створення захищених багатосторонніх обчислень</li>
                    </ul>
                  </div>
                  <div class="flex gap-3">
                    <div class="shrink-0 bg-green-600 text-white font-mono text-xs uppercase px-2 py-1 h-fit mt-0.5">Результат</div>
                    <p class="font-bold text-black">Експериментальний зразок інтелектуалізованої сенсорної мережі, перевірений за критеріями стійкості до РЕБ.</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- ВИСНОВОК -->
          <div class="bg-black text-white border-4 border-black p-8 md:p-10 relative overflow-hidden shadow-[12px_12px_0px_0px_rgba(0,0,0,1)]">
            <h4 class="font-mono text-lg text-purple-400 mb-6 uppercase font-bold tracking-widest">Реалізація проєктів забезпечує:</h4>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-5 font-bold text-base md:text-lg">
              <div class="flex items-start gap-3"><span class="text-purple-500 mt-1">/></span> Експериментальне підтвердження нових моделей і методів</div>
              <div class="flex items-start gap-3"><span class="text-purple-500 mt-1">/></span> Розвиток технологій керування групами БПЛА</div>
              <div class="flex items-start gap-3"><span class="text-purple-500 mt-1">/></span> Підвищення функціональної стійкості сенсорних мереж</div>
              <div class="flex items-start gap-3"><span class="text-purple-500 mt-1">/></span> Практичний внесок у безпеку та обороноздатність України</div>
            </div>
          </div>
        </div>
      </div>

      <!-- НАПРЯМКИ ДІЯЛЬНОСТІ -->
      <div>
        <div class="mb-10 flex items-center justify-between border-b-4 border-black pb-4">
          <h3 class="text-3xl md:text-5xl font-black uppercase tracking-tighter">
            Напрямки <span class="text-purple-600">діяльності</span>
          </h3>
          <span class="hidden md:inline-block font-mono font-bold text-sm bg-black text-white px-4 py-2 uppercase">Global Directions</span>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <div
            v-for="module in directionModules"
            :key="module.number"
            class="bg-white border-4 border-black p-6 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] flex flex-col transition-transform hover:-translate-y-1"
          >
            <div class="border-b-2 border-black pb-2 mb-4 flex items-start gap-2">
              <span class="font-black text-lg leading-none">{{ module.number }}</span>
              <span class="font-mono text-[10px] text-gray-500 uppercase tracking-widest mt-1">Module 0{{ module.number }}</span>
            </div>
            <h4 class="text-lg md:text-xl font-black uppercase mb-3 leading-tight">{{ module.title }}</h4>
            <p class="font-medium text-gray-600 leading-relaxed mt-auto text-sm">{{ module.description }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- МОДАЛКА -->
    <Teleport to="body">
      <Transition name="modal">
        <div
          v-if="selectedImage"
          class="fixed inset-0 z-[100] flex items-center justify-center bg-black/95 p-4 md:p-8 cursor-pointer backdrop-blur-md"
          @click="closeImageModal"
        >
          <div class="relative w-full max-w-6xl h-full flex justify-center items-center" @click.stop>
            <button
              @click="closeImageModal"
              class="absolute top-4 right-4 md:top-6 md:right-6 bg-white border-4 border-black text-black font-mono font-bold px-4 py-2 hover:bg-red-500 hover:text-white transition-colors shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] z-10 uppercase"
            >
              Закрити [x]
            </button>
            <img
              :src="selectedImage"
              :alt="selectedImageAlt"
              class="max-w-full max-h-full object-contain border-8 border-black bg-white shadow-[16px_16px_0px_0px_rgba(147,51,234,1)]"
            />
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// --- ДАНІ ---
const officialDocs = [
  {
    file: '/science-edu-processes/laboratory1.jpg',
    label: 'Скан 1',
    caption: 'Положення про лабораторію, стор. 1',
    alt: 'Скан 1: перша сторінка положення про лабораторію',
  },
  {
    file: '/science-edu-processes/laboratory2.jpg',
    label: 'Скан 2',
    caption: 'Положення про лабораторію, стор. 2',
    alt: 'Скан 2: друга сторінка положення про лабораторію',
  },
];

const hardwareStands = [
  { file: '/science-edu-processes/lab1.jpg', title: 'Апаратні модулі, безпілотні системи' },
  { file: '/science-edu-processes/lab2.jpg', title: 'Головний термінал лабораторії' },
  { file: '/science-edu-processes/lab3.jpg', title: 'Стенд експериментального моделювання' },
  { file: '/science-edu-processes/lab4.jpg', title: 'Робота над зразками мікроелектроніки' },
];

const directionModules = [
  {
    number: 1,
    title: 'Функціональна стійкість телекомунікаційних систем',
    description: 'Математичне та програмне забезпечення для функціонування систем в умовах відмов та кібератак (розподіл ресурсів, резервування).',
  },
  {
    number: 2,
    title: 'Сенсорна система спеціального призначення',
    description: 'Роботизована система моніторингу та розмінування (QS-система) з використанням ШІ для формування управлінських рішень.',
  },
  {
    number: 3,
    title: 'Забезпечення OSI-міжрівневої узгодженості',
    description: 'Моделі та методи забезпечення ідеальної узгодженості передачі даних між усіма рівнями мережевої моделі OSI.',
  },
];

// --- МОДАЛКА ---
const selectedImage = ref(null);
const selectedImageAlt = ref('');

const findAlt = (imgPath) => {
  const doc = officialDocs.find((d) => d.file === imgPath);
  if (doc) return doc.alt;
  const stand = hardwareStands.find((s) => s.file === imgPath);
  if (stand) return stand.title;
  return 'Збільшене зображення';
};

const openImageModal = (imgPath) => {
  selectedImage.value = imgPath;
  selectedImageAlt.value = findAlt(imgPath);
  if (import.meta.client) document.body.style.overflow = 'hidden';
};

const closeImageModal = () => {
  selectedImage.value = null;
  if (import.meta.client) document.body.style.overflow = 'auto';
};

const handleKeydown = (e) => {
  if (e.key === 'Escape' && selectedImage.value) closeImageModal();
};

// --- ГЛІТЧ МІТ ---
const GLITCH_TARGET = 'МІТ';
const GLITCH_CHARS = '01#@$%&*+=-/\\<>[]{}~^АБВГДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ';
const glitchText = ref(GLITCH_TARGET);
let glitchTimer = null;
let frame = 0;

const randomGlitchChar = () => GLITCH_CHARS[Math.floor(Math.random() * GLITCH_CHARS.length)];

const runGlitch = () => {
  const SCRAMBLE = 24;
  const LOCK_STEP = 7;
  const LOCK = GLITCH_TARGET.length * LOCK_STEP;
  const HOLD = 70;
  const CYCLE = SCRAMBLE + LOCK + HOLD;

  if (import.meta.client && window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    glitchText.value = GLITCH_TARGET;
    return;
  }

  glitchTimer = setInterval(() => {
    frame = (frame + 1) % CYCLE;
    if (frame < SCRAMBLE) {
      glitchText.value = GLITCH_TARGET.split('').map(() => randomGlitchChar()).join('');
    } else if (frame < SCRAMBLE + LOCK) {
      const locked = Math.floor((frame - SCRAMBLE) / LOCK_STEP) + 1;
      glitchText.value = GLITCH_TARGET.split('').map((ch, i) => (i < locked ? ch : randomGlitchChar())).join('');
    } else {
      glitchText.value = GLITCH_TARGET;
    }
  }, 65);
};

onMounted(() => {
  runGlitch();
  if (import.meta.client) window.addEventListener('keydown', handleKeydown);
});

onUnmounted(() => {
  if (glitchTimer) clearInterval(glitchTimer);
  if (import.meta.client) window.removeEventListener('keydown', handleKeydown);
});
</script>

<style scoped>
.glitch-text {
  position: relative;
  text-shadow:
    2px 0 rgba(239, 68, 68, 0.35),
    -2px 0 rgba(34, 211, 238, 0.35);
}

.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}
.modal-enter-active img,
.modal-leave-active img {
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
.modal-enter-from img,
.modal-leave-to img {
  transform: scale(0.95);
}

@media (prefers-reduced-motion: reduce) {
  .glitch-text {
    text-shadow: none;
  }
}
</style>