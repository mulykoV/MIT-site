<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-lime-400 selection:text-black pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Матрична сітка) -->
    <div class="absolute inset-0 opacity-20 bg-[linear-gradient(#cbd5e1_1px,transparent_1px),linear-gradient(90deg,#cbd5e1_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-12 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-lime-600 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(132,204,22,1)]">[ SKILL_MATRIX ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter leading-none">
            ПРОФЕСІЙНІ <br><span class="text-white bg-black px-3 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">ДИСЦИПЛІНИ</span>
          </h1>
        </div>
        
      </div>

      <!-- НАВІГАЦІЯ (ФІЛЬТРИ ПО КАТЕГОРІЯХ) -->
      <div class="flex flex-wrap gap-4 mb-12 border-b-4 border-black pb-8">
        <button 
          v-for="cat in categories" 
          :key="cat.id"
          @click="activeCategory = cat.id"
          class="font-pixel text-sm md:text-base px-6 py-3 uppercase border-4 border-black transition-all shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] active:translate-y-1 active:translate-x-1 active:shadow-none"
          :class="activeCategory === cat.id ? `bg-${cat.color} text-${cat.textColor}` : 'bg-white text-gray-500 hover:bg-gray-100'"
        >
          > {{ cat.name }}
        </button>
      </div>

      <!-- СІТКА ДИСЦИПЛІН (SKILL MODULES) -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        <TransitionGroup name="list">
          <div 
            v-for="(mod, index) in filteredModules" 
            :key="mod.title"
            class="flex flex-col border-4 border-black bg-white shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-2 hover:shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] transition-all duration-300 relative group cursor-pointer h-[280px]"
            @click="openModule(mod)"
          >
            <!-- ШАПКА МОДУЛЯ -->
            <div class="bg-black text-white p-3 flex justify-between items-center border-b-4 border-black">
              <span class="font-pixel text-[10px] text-zinc-400 uppercase">PKG_{{ String(index + 1).padStart(3, '0') }}</span>
              <span class="font-pixel text-[10px] uppercase" :class="`text-${getCategoryColor(mod.category)}`">
                ● INSTALL
              </span>
            </div>

            <!-- ТІЛО КАРТКИ -->
            <div class="p-6 flex-grow flex flex-col relative overflow-hidden">
              <!-- Фоновий водяний знак (іконка або цифра) -->
              <div class="absolute -right-4 -bottom-4 text-[100px] opacity-5 font-black pointer-events-none group-hover:scale-110 transition-transform">
                { }
              </div>
              
              <div class="font-pixel text-[10px] mb-4 uppercase border-2 border-black px-2 py-1 w-fit" :class="`bg-${getCategoryColor(mod.category)}`">
                {{ getCategoryName(mod.category) }}
              </div>
              
              <h2 class="text-xl md:text-2xl font-black uppercase tracking-tight leading-tight mb-2 group-hover:underline decoration-4 underline-offset-4 line-clamp-3">
                {{ mod.title }}
              </h2>
              
              <div class="mt-auto border-t-2 border-dashed border-gray-300 pt-4 flex items-center justify-between">
                <span class="font-mono text-xs text-gray-500 font-bold uppercase">> Read Docs</span>
                <svg class="w-5 h-5 group-hover:translate-x-2 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
              </div>
            </div>
            
            <!-- ДЕКОРАТИВНИЙ КУТОЧОК -->
            <div class="absolute bottom-0 right-0 w-6 h-6 border-t-4 border-l-4 border-black" :class="`bg-${getCategoryColor(mod.category)}`"></div>
          </div>
        </TransitionGroup>
      </div>

    </div>

    <!-- МОДАЛЬНЕ ВІКНО ДОКУМЕНТАЦІЇ -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedModule" class="fixed inset-0 z-[9999] flex items-center justify-center p-4 md:p-6">
          
          <div class="absolute inset-0 bg-black/90 backdrop-blur-sm cursor-pointer" @click="closeModule"></div>
          
          <button @click="closeModule" class="absolute top-4 right-4 z-[10000] bg-red-600 text-white font-pixel text-xl w-12 h-12 flex items-center justify-center border-4 border-black shadow-[4px_4px_0px_0px_rgba(255,255,255,1)] hover:translate-y-1 hover:translate-x-1 hover:shadow-none transition-all cursor-pointer">
            X
          </button>

          <div class="relative w-full max-w-5xl bg-[#F4F4F0] border-8 border-black shadow-[16px_16px_0px_0px_rgba(255,255,255,0.2)] max-h-[90vh] flex flex-col md:flex-row overflow-hidden">
            
            <!-- ЛІВА ПАНЕЛЬ (Термінальний лог) -->
            <div class="w-full md:w-1/3 bg-black border-b-8 md:border-b-0 md:border-r-8 border-black p-6 flex flex-col">
              <div class="font-pixel text-[10px] text-zinc-500 uppercase mb-6 border-b-2 border-dashed border-zinc-700 pb-2">
                SYSTEM_LOG
              </div>
              <div class="font-mono text-[10px] md:text-xs text-green-400 opacity-80 leading-relaxed overflow-hidden break-all">
                > Initializing module package...<br>
                > Loading dependencies for {{ selectedModule.title }}...<br>
                > Validating skill tree requirements... [OK]<br>
                > Extracting theoretical base... [OK]<br>
                > Allocating practical memory...<br>
                <br>
                <span v-for="i in 15" :key="i">{{ Math.random().toString(36).substring(2, 10) }} {{ Math.random().toString(36).substring(2, 8) }}<br></span>
                <br>
                <span class="animate-pulse">> _</span>
              </div>
            </div>

            <!-- ПРАВА ПАНЕЛЬ (Контент) -->
            <div class="w-full md:w-2/3 flex flex-col bg-white overflow-y-auto">
              
              <div class="p-8 md:p-12 relative flex-grow">
                <div class="inline-block border-4 border-black font-pixel text-xs px-3 py-2 uppercase mb-6" :class="`bg-${getCategoryColor(selectedModule.category)} text-${getCategoryTextColor(selectedModule.category)}`">
                  CATEGORY: {{ getCategoryName(selectedModule.category) }}
                </div>
                
                <h2 class="text-3xl md:text-5xl font-black uppercase tracking-tighter leading-tight mb-8">
                  {{ selectedModule.title }}
                </h2>
                
                <div class="border-t-4 border-dashed border-black pt-6 relative">
                  <div class="absolute -top-4 left-4 bg-white px-2 font-pixel text-xs text-gray-500 uppercase">ОПИС ДИСЦИПЛІНИ</div>
                  <p class="font-mono text-base md:text-lg text-black font-medium leading-relaxed whitespace-pre-line">
                    {{ selectedModule.description }}
                  </p>
                </div>
              </div>
              
              <div class="bg-[#F4F4F0] border-t-8 border-black p-6 md:p-8 shrink-0 flex items-center justify-between">
                <span class="font-pixel text-xs text-gray-500 uppercase">[ END_OF_DOCUMENTATION ]</span>
                <button @click="closeModule" class="font-pixel text-lg bg-black text-white px-8 py-4 border-4 border-black hover:bg-white hover:text-black hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all">
                  > ЗАКРИТИ
                </button>
              </div>

            </div>
          </div>
        </div>
      </Transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const categories = [
  { id: 'all', name: 'ВСІ МОДУЛІ', color: 'black', textColor: 'white' },
  { id: 'telecom', name: 'Телекомунікації', color: 'cyan-400', textColor: 'black' },
  { id: 'programming', name: 'Програмування', color: 'fuchsia-500', textColor: 'white' },
  { id: 'general', name: 'Загальні IT дисципліни', color: 'yellow-400', textColor: 'black' }
];

const activeCategory = ref('all');

// Всі 18 дисциплін з офіційного списку
const modules = ref([
  // ТЕЛЕКОМУНІКАЦІЇ
  {
    title: "Комп'ютерні мережі",
    category: "telecom",
    description: "Основні напрямки вивчення:\n- закономірності функціонування та побудови комп'ютерних мереж для забезпечення функціонування інформаційних систем;\n- принципи побудови комп'ютерних мереж, їх технічного та програмного забезпечення;\n- критерії вибору та застосування інформаційно-комунікаційних мереж у забезпеченні управлінської та адміністративної діяльності."
  },
  {
    title: "Технології та протоколи мультисервісних мереж",
    category: "telecom",
    description: "Дисципліна присвячена основам мережних протоколів та технологій, що дає студентам розуміння того, за якими принципами організовані мережі. Також основну увагу приділено одній з основних характеристик сучасних мереж – мультисервісності."
  },
  {
    title: "Оптичні транспортні системи та мережі",
    category: "telecom",
    description: "Вивчення принципів побудови, функціонування та експлуатації сучасних волоконно-оптичних ліній зв'язку та транспортних мереж. Розглядаються технології мультиплексування та передачі даних на великі швидкості та відстані."
  },
  {
    title: "Інфраструктура мереж майбутнього",
    category: "telecom",
    description: "Дослідження новітніх архітектур мереж, програмно-конфігурованих мереж (SDN), віртуалізації мережевих функцій (NFV) та концепцій автоматизації керування інфраструктурою сучасного підприємства."
  },
  {
    title: "Основи інформаційної безпеки",
    category: "telecom",
    description: "Знання, здобуті в сфері інформаційної безпеки, дозволять студенту зрозуміти природу інформації та її властивостей, усвідомити сутність загроз інформаційній безпеці і шляхів їх запобігання та усунення."
  },
  {
    title: "Кібернетична безпека підприємства",
    category: "telecom",
    description: "Дисципліна присвячена основним поняттям у сфері інформаційної безпеки в цілому та кібербезпеки мережі та інформаційних ресурсів підприємства зокрема. Студенти знайомляться з інструментами для впровадження систем безпеки."
  },
  
  // ПРОГРАМУВАННЯ
  {
    title: "Основи програмування",
    category: "programming",
    description: "Метою вивчення дисципліни є отримання теоретичних знань та практичних навичок програмування мовою Python, що дозволить розв'язувати складні алгоритмічні задачі, виконувати наукові дослідження."
  },
  {
    title: "Теорія алгоритмів",
    category: "programming",
    description: "Вивчення фундаментальних структур даних та методів побудови алгоритмів. Аналіз складності алгоритмів, оптимізація коду та розв'язання нестандартних обчислювальних задач різного класу складності."
  },
  {
    title: "Об'єктно-орієнтоване програмування",
    category: "programming",
    description: "Дисципліна знайомить студентів з парадигмою об'єктно-орієнтованого програмування та її основними поняттями і принципами, висвітлює особливості реалізації ООП в різних мовах програмування (Python, Java, C++)."
  },
  {
    title: "Організація баз даних",
    category: "programming",
    description: "Вивчаються основи застосування баз даних в інформаційних системах, здійснюється набуття навичок у проектуванні, нормалізації та практичній роботі з реляційними (SQL) та нереляційними базами даних."
  },
  {
    title: "Інтелектуальний аналіз даних",
    category: "programming",
    description: "Теорія та практика аналізу великого обсягу інформації на основі сучасних методів науки про дані (Data Science). Вивчаються методи обробки масивів даних та пошук прихованих закономірностей."
  },
  {
    title: "Веб-дизайн та веб-програмування",
    category: "programming",
    description: "Основи теорії та практичне застосування сучасних програмних засобів (HTML, CSS, JavaScript, PHP, Node.js) для створення сучасних, адаптивних веб-додатків."
  },

  // ЗАГАЛЬНІ IT ДИСЦИПЛІНИ
  {
    title: "Архітектура комп'ютерів",
    category: "general",
    description: "Метою викладання навчальної дисципліни є: надання системних відомостей про будову та принципи функціонування сучасних апаратних засобів обчислювальних систем. Формування знань щодо побудови комп'ютерної техніки."
  },
  {
    title: "Операційні системи",
    category: "general",
    description: "Архітектура; методи і алгоритми керування локальними ресурсами комп'ютерів та мереж; системи організації віддаленого виклику процедур і розподілених файлових систем."
  },
  {
    title: "Хмарні технології",
    category: "general",
    description: "Розглядаються питання ефективного використання технологій розподілених обчислень, систем віртуалізації, застосування надпродуктивних обчислень та створення баз даних на основі технологій хмарних платформ."
  },
  {
    title: "Технології штучного інтелекту",
    category: "general",
    description: "Ознайомлення з базовими алгоритмами машинного навчання, штучними нейронними мережами та побудовою систем штучного інтелекту для автоматизації рутинних задач та розпізнавання образів."
  },
  {
    title: "Побудова систем інтернету речей",
    category: "general",
    description: "Проектування та програмування розумних пристроїв. Інтеграція сенсорів, мікроконтролерів та мережевих модулів в єдину екосистему збору та обробки даних (IoT)."
  },
  {
    title: "Дискретна математика",
    category: "general",
    description: "«Дискретна математика» включає важливий матеріал з таких областей як теорія множин, логіка, теорія графів. Відомості широко використовуються в структурах даних й алгоритмах."
  }
]);

const filteredModules = computed(() => {
  if (activeCategory.value === 'all') return modules.value;
  return modules.value.filter(m => m.category === activeCategory.value);
});

const getCategoryColor = (catId) => {
  const cat = categories.find(c => c.id === catId);
  return cat ? cat.color : 'white';
};

const getCategoryTextColor = (catId) => {
  const cat = categories.find(c => c.id === catId);
  return cat ? cat.textColor : 'black';
};

const getCategoryName = (catId) => {
  const cat = categories.find(c => c.id === catId);
  return cat ? cat.name : 'Unknown';
};

const selectedModule = ref(null);

const openModule = (mod) => {
  selectedModule.value = mod;
  if (import.meta.client) document.body.style.overflow = 'hidden';
};

const closeModule = () => {
  selectedModule.value = null;
  if (import.meta.client) document.body.style.overflow = 'auto';
};
</script>

<style scoped>
.list-enter-active,
.list-leave-active {
  transition: all 0.4s ease;
}
.list-enter-from,
.list-leave-to {
  opacity: 0;
  transform: translateY(20px) scale(0.95);
}
.list-leave-active {
  position: absolute;
}

.modal-enter-active,
.modal-leave-active {
  transition: opacity 0.3s ease;
}
.modal-enter-active .relative,
.modal-leave-active .relative {
  transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.modal-enter-from,
.modal-leave-to {
  opacity: 0;
}
.modal-enter-from .relative,
.modal-leave-to .relative {
  transform: scale(0.95) translateY(20px);
}

.page-enter-active,
.page-leave-active {
  transition: opacity 0.3s ease, filter 0.3s ease;
}
.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(10px) grayscale(100%);
}
</style>