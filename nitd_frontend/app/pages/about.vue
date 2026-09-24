<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black overflow-hidden font-mono selection:bg-blue-600 selection:text-white">

    <!-- HERO: ЗУМЕРСЬКИЙ ВАЙБ -->
    <div class="relative pt-40 pb-32 px-6 lg:px-12 border-b-4 border-black bg-blue-600 text-white overflow-hidden">
      <!-- Декоративний гріт-фон -->
      <div class="absolute inset-0 opacity-20 bg-[linear-gradient(#fff_2px,transparent_2px),linear-gradient(90deg,#fff_2px,transparent_2px)] bg-[size:60px_60px] transform rotate-3 scale-110"></div>
      
      <div class="relative z-10 max-w-[1400px] mx-auto flex flex-col items-center text-center">
        <div class="border-4 border-black bg-yellow-400 text-black px-6 py-2 font-pixel text-2xl uppercase mb-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] rotate-[-2deg]">
          [ NOT MASSACHUSETTS, BUT BETTER ]
        </div>
        
        <h1 class="text-6xl md:text-8xl lg:text-[140px] font-black uppercase tracking-tighter leading-[0.8] mix-blend-overlay">
          КАФЕДРА <br>
          <span class="text-transparent border-text-white">МІТ</span>
        </h1>
        
        <p class="mt-8 max-w-2xl text-xl md:text-3xl font-bold bg-black text-white p-4 shadow-[8px_8px_0px_0px_rgba(255,255,255,1)]">
          Ми хакаємо систему освіти з 2016. Тут не перевстановлюють вінду — тут розгортають нейронки та деплоять мікросервіси.
        </p>
      </div>

      <!-- Декоративні елементи -->
      <div class="absolute bottom-10 left-10 w-24 h-24 border-8 border-black rounded-full animate-ping opacity-50 hidden md:block"></div>
      <div class="absolute top-20 right-10 font-pixel text-6xl opacity-20">{"}"}</div>
    </div>

    <!-- БІЖУЧА СТРІЧКА ТЕХНОЛОГІЙ -->
    <div class="border-b-4 border-black bg-black text-white py-4 overflow-hidden">
      <div class="whitespace-nowrap font-pixel text-2xl animate-marquee uppercase tracking-widest text-green-400">
        * NO_BULLSHIT * PURE_HARDCORE * LINUX_ONLY * CLOUD_NATIVE * NO_BULLSHIT * PURE_HARDCORE * LINUX_ONLY * CLOUD_NATIVE *
      </div>
    </div>

    <!-- ІСТОРІЯ & СТЕК (LORE_v1.0.txt) -->
    <div class="py-24 px-6 max-w-[1400px] mx-auto grid grid-cols-1 lg:grid-cols-2 gap-16 items-start">
      
      <!-- Ліва колонка: Історія -->
      <div class="border-4 border-black p-8 bg-white shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] relative group mt-8 lg:mt-0">
        <div class="absolute -top-6 -left-6 bg-red-500 text-white font-pixel px-4 py-2 border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] group-hover:rotate-6 transition-transform">
          LORE_v1.0.txt
        </div>
        <h2 class="text-4xl font-black uppercase mb-6 mt-4">Як все почалося</h2>
        <div class="space-y-4 text-lg font-medium leading-relaxed">
          <p>У <span class="bg-yellow-300 font-bold px-1">2016 році</span> ми зрозуміли: академічна освіта застаріла ще до того, як студенти отримують диплом. Тому ми створили МІТ.</p>
          <p>Наша філософія проста: **менше конспектів, більше комітів**. Замість лекцій під запис — розгортання інфраструктури в AWS, налаштування Docker-контейнерів та хакатони.</p>
          <p>Ми не вчимо "комп'ютерної грамотності". Ми готуємо Network та DevOps інженерів, які з ноги відкривають двері в IT-компанії.</p>
        </div>
      </div>

      <!-- Права колонка: Дизайн сет / Технології (Tag Cloud) -->
      <div class="flex flex-col gap-6">
        <h2 class="text-4xl font-black uppercase text-left lg:text-right">Наш Tech-Стек</h2>
        <div class="flex flex-wrap gap-3 lg:justify-end">
          <div 
            v-for="tech in techStack" 
            :key="tech.name"
            class="border-4 border-black px-4 py-2 text-center hover:bg-black hover:text-white transition-colors cursor-crosshair shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] font-bold text-sm md:text-base uppercase"
            :class="tech.color"
          >
            {{ tech.name }}
          </div>
        </div>
      </div>

    </div>

    <!-- БЛОК НАУКИ (Секретні файли) -->
    <div class="w-full bg-black text-[#F4F4F0] border-y-4 border-black py-24 px-6 relative overflow-hidden">
      <!-- Декор -->
      <div class="absolute right-0 top-0 opacity-10 font-pixel text-[200px] leading-none text-red-500 pointer-events-none">R&D</div>
      
      <div class="max-w-[1400px] mx-auto relative z-10">
        <div class="mb-16 border-b-2 border-gray-700 pb-8 flex flex-col md:flex-row justify-between items-end gap-6">
          <div>
            <h4 class="font-pixel text-red-500 mb-2 uppercase tracking-widest">[ ФУНДАМЕНТАЛЬНІ ДОСЛІДЖЕННЯ ]</h4>
            <h2 class="text-5xl md:text-7xl font-black uppercase tracking-tighter">НАУКА</h2>
          </div>
          <div class="font-mono text-sm text-gray-400 bg-gray-900 border border-gray-700 p-3">
            > ACCESS_LEVEL: CLASSIFIED <br>
            > DECRYPTING_FILES... DONE
          </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
          
          <!-- Ліва частина: Список R&D -->
          <div class="lg:col-span-8 flex flex-col gap-8">
            
            <!-- Діяльність -->
            <div class="border-l-4 border-red-500 pl-6 hover:translate-x-2 transition-transform">
              <h3 class="text-2xl font-black uppercase text-white mb-3">Науково-дослідницька діяльність</h3>
              <p class="text-gray-400 font-mono mb-2">Основні напрями наукових досліджень кафедри мережевих та інтернет технологій:</p>
              <ul class="list-none font-mono text-blue-300 space-y-1">
                <li>[+] Функціональна стійкість телекомунікаційних систем.</li>
                <li>[+] Сенсорна система спеціального призначення.</li>
                <li>[+] Забезпечення OSI-міжрівневої узгодженості.</li>
              </ul>
            </div>

            <!-- Проєкт 1 -->
            <div class="border-2 border-gray-800 bg-gray-900 p-6 shadow-[8px_8px_0px_0px_rgba(239,68,68,1)] hover:bg-black transition-colors">
              <h3 class="text-xl font-bold uppercase text-red-400 mb-3 font-pixel">Проєкт "Функціональна стійкість телекомунікаційних систем"</h3>
              <p class="text-gray-300 font-mono text-sm leading-relaxed">
                Математичне та програмне забезпечення, яке дозволяє в умовах зовнішніх та внутрішніх негативних впливів (відмов, пошкоджень, помилок операторів, терористичних впливів та ін.) забезпечити функціонування телекомунікаційних систем за рахунок виявлення та перерозподілу існуючих видів надмірності (програмної, часової, енергетичної ті ін.)
              </p>
            </div>

            <!-- Проєкт 2 (Highlight) -->
            <div class="border-2 border-gray-800 bg-gray-900 p-6 shadow-[8px_8px_0px_0px_rgba(34,197,94,1)] hover:bg-black transition-colors relative overflow-hidden">
              <div class="absolute top-0 right-0 bg-green-500 text-black font-pixel text-[10px] px-2 py-1">TOP_PRIORITY</div>
              <h3 class="text-xl font-bold uppercase text-green-400 mb-3 font-pixel mt-2">Проєкт "Сенсорна система спеціального призначення"</h3>
              <p class="text-gray-300 font-mono text-sm leading-relaxed">
                Основною ідеєю є створення роботизованої системи моніторингу та розмінування демілітаризованої смуги з використанням принципово нових моделей, методів та методик (так звана QS-система). Робочою гіпотезою проєкту є те, що використання нових принципів дозволить забезпечити функціональну стійкість та виконати завдання бойового та оперативного забезпечення стосовно розвідки та розмінування.
              </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-8 mt-4">
              <!-- Проєкт 3 -->
              <div class="border-l-2 border-blue-500 pl-4">
                <h3 class="text-lg font-bold uppercase text-blue-400 mb-2 font-pixel">"Забезпечення OSI-міжрівневої узгодженості"</h3>
                <p class="text-gray-400 font-mono text-xs">Моделі та методи забезпечення узгодженості між рівнями моделі OSI.</p>
              </div>
              <!-- Міжнародні зв'язки -->
              <div class="border-l-2 border-yellow-500 pl-4">
                <h3 class="text-lg font-bold uppercase text-yellow-400 mb-2 font-pixel">Міжнародні зв'язки кафедри</h3>
                <p class="text-gray-400 font-mono text-xs line-clamp-4">
                  Кафедра плідне співпрацює з іноземними фірмами, товариствами, закордонними вищими навчальними закладами, що має за мету покращення навчального процесу і його наближення до відповідних світових стандартів освіти.
                </p>
              </div>
            </div>

          </div>

          <!-- Права частина: ІНТЕРАКТИВНИЙ 3D ASCII РАДАР -->
          <div class="lg:col-span-4 relative group flex flex-col justify-center">
            <div class="border-4 border-gray-700 bg-black p-2 shadow-[12px_12px_0px_0px_rgba(34,197,94,0.5)] transform rotate-1 group-hover:rotate-0 transition-transform duration-300 relative z-10 w-full">
              
              <!-- Заголовок ASCII Терміналу -->
              <div class="bg-gray-900 border-b-2 border-gray-800 p-2 flex justify-between items-center font-pixel text-[10px] text-green-500">
                <span>> QS_SENSOR_SIMULATION.exe</span>
                <span class="animate-pulse">RUNNING</span>
              </div>
              
              <!-- CANVAS для рендеру ASCII (З фіксованими пропорціями) -->
              <div class="w-full aspect-square bg-[#0a0a0a] flex items-center justify-center p-4 relative overflow-hidden">
                <pre class="font-mono text-green-500 text-[8px] sm:text-[10px] leading-none whitespace-pre relative z-10 font-bold" v-html="asciiFrame"></pre>
                
                <!-- Декоративна сітка на фоні радару -->
                <div class="absolute inset-0 opacity-10 bg-[linear-gradient(#22c55e_1px,transparent_1px),linear-gradient(90deg,#22c55e_1px,transparent_1px)] bg-[size:20px_20px]"></div>
                <!-- Лазер радара (світловий ефект) -->
                <div class="absolute top-1/2 left-1/2 w-full h-1 bg-green-500/20 origin-left animate-spin" style="animation-duration: 4s; animation-timing-function: linear;"></div>
              </div>
              
              <div class="mt-2 font-mono text-[10px] text-gray-500 flex justify-between px-2">
                <span>SENSOR: ACTIVE</span>
                <span>TARGET: IDENTIFIED</span>
              </div>
            </div>
            
            <pre class="absolute -bottom-10 -right-4 text-[8px] text-gray-800 font-mono z-0 pointer-events-none hidden md:block">
def init_qs_system():
  sensors = load_sensors()
  if mine_detected(sensors):
     deploy_drone()
     alert_hq()
     init_qs_system()
            </pre>
          </div>

        </div>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// МАСИВ ТЕХНОЛОГІЙ
const techStack = [
  { name: 'Docker', color: 'bg-[#c7d2fe]' },
  { name: 'K8s', color: 'bg-[#fca5a5]' },
  { name: 'Python / Django', color: 'bg-[#fef08a]' },
  { name: 'Vue.js + JS', color: 'bg-[#bbf7d0]' },
  { name: 'Oracle SQL', color: 'bg-[#fdba74]' },
  { name: 'PostgreSQL', color: 'bg-[#99f6e4]' },
  { name: 'MongoDB', color: 'bg-[#fbcfe8]' },
  { name: 'Java + Spring', color: 'bg-[#e9d5ff]' },
  { name: 'C# / .NET Core', color: 'bg-[#c7d2fe]' },
  { name: 'ASP.NET', color: 'bg-white' },
  { name: 'Angular', color: 'bg-[#fef08a]' },
  { name: 'Machine Learning', color: 'bg-[#fbcfe8]' },
  { name: 'Jupyter', color: 'bg-[#fdba74]' },
  { name: 'Terraform (IaC)', color: 'bg-[#99f6e4]' },
  { name: 'AWS', color: 'bg-white' },
  { name: 'Azure', color: 'bg-[#c7d2fe]' },
  { name: 'Arch Linux', color: 'bg-[#fca5a5]' },
  { name: 'Nginx', color: 'bg-[#bbf7d0]' },
  { name: 'GitHub Actions', color: 'bg-[#e9d5ff]' },
  { name: 'Cisco', color: 'bg-[#fef08a]' },
  { name: 'IoT', color: 'bg-[#99f6e4]' }
];

// ЛОГІКА 3D ASCII РАДАРА/КУБА
const asciiFrame = ref('');
let animationFrameId;

// Параметри обертання
let A = 0;
let B = 0;
let C = 0;

const renderAscii = () => {
  const width = 40;  // Кількість символів у ширину
  const height = 20; // Кількість символів у висоту
  const zBuffer = new Array(width * height).fill(0);
  const buffer = new Array(width * height).fill(' ');

  // Символи для створення ілюзії освітлення та глибини (від темного до світлого)
  const chars = '.,-~:;=!*#$@';

  // Оновлюємо кути обертання (A, B, C впливають на осі X, Y, Z)
  A += 0.05;
  B += 0.03;
  C += 0.01;

  // Попередньо обчислюємо синуси/косинуси для швидкодії
  const cA = Math.cos(A), sA = Math.sin(A);
  const cB = Math.cos(B), sB = Math.sin(B);
  const cC = Math.cos(C), sC = Math.sin(C);

  // Створюємо "фігуру" - набір точок у просторі (сфера/радар)
  for (let j = 0; j < 6.28; j += 0.2) { // j - кут навколо осі Z
    for (let i = 0; i < 6.28; i += 0.1) { // i - кут навколо осі X
      
      const cj = Math.cos(j), sj = Math.sin(j);
      const ci = Math.cos(i), si = Math.sin(i);

      // Радіус фігури (тора)
      const R1 = 1;
      const R2 = 2;
      
      // Координати точки до обертання
      const ox = (R2 + R1 * ci) * cj;
      const oy = (R2 + R1 * ci) * sj;
      const oz = R1 * si;

      // 3D Обертання
      const x = ox * (cB * cC) + oy * (sA * sB * cC - cA * sC) + oz * (cA * sB * cC + sA * sC);
      const y = ox * (cB * sC) + oy * (sA * sB * sC + cA * cC) + oz * (cA * sB * sC - sA * cC);
      const z = -ox * sB + oy * (sA * cB) + oz * (cA * cB);

      // Проєкція 3D на 2D екран
      const ooz = 1 / (z + 5); // Глибина (z-index)
      
      const xp = Math.floor(width / 2 + 15 * ooz * x);
      const yp = Math.floor(height / 2 + 7 * ooz * y); // 7 - коефіцієнт стиснення символів у висоту
      
      // Індекс у 1D масиві буфера
      const idx = xp + yp * width;

      // Обчислення яскравості (Luminance)
      const L = cj * ci * sB - cA * ci * sj - sA * si + cB * (cA * si - ci * sA * sj);
      
      // Якщо точка на екрані, ближче ніж попередня, і освітлена
      if (yp >= 0 && yp < height && xp >= 0 && xp < width && ooz > zBuffer[idx]) {
        zBuffer[idx] = ooz;
        const lumIndex = Math.floor(L * 8); // Нормалізуємо до індексу символу (0-11)
        buffer[idx] = lumIndex > 0 ? chars[lumIndex] : '.'; // Замість порожнечі малюємо фонові "крапки"
      }
    }
  }

  // Перетворюємо 1D масив у рядок з переносами
  let frame = '';
  for (let k = 0; k < buffer.length; k++) {
    frame += k % width === width - 1 ? buffer[k] + '\n' : buffer[k];
  }
  
  asciiFrame.value = frame;
  animationFrameId = requestAnimationFrame(renderAscii);
};

onMounted(() => {
  if (import.meta.client) {
    renderAscii();
  }
});

onUnmounted(() => {
  if (import.meta.client) {
    cancelAnimationFrame(animationFrameId);
  }
});
</script>

<style scoped>
.border-text-white {
  -webkit-text-stroke: 2px white;
}

@keyframes marquee {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-50%); }
}
.animate-marquee {
  display: inline-block;
  animation: marquee 15s linear infinite;
  min-width: 200%;
}
</style>