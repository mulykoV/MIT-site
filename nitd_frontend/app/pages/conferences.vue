<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-blue-600 selection:text-white pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Сітка) -->
    <div class="absolute inset-0 opacity-10 bg-[linear-gradient(#000_1px,transparent_1px),linear-gradient(90deg,#000_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>

    <div class="max-w-[1200px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-16 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-yellow-500 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(234,179,8,1)]">[ KNOWLEDGE_EXCHANGE ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter">
            НАУКОВІ <br><span class="text-white bg-black px-3 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">КОНФЕРЕНЦІЇ</span>
          </h1>
        </div>
        
      </div>

      <!-- Статус завантаження -->
      <div v-if="pending" class="w-full border-4 border-dashed border-gray-400 py-32 flex flex-col items-center justify-center text-gray-500 bg-white mb-12">
        <div class="font-pixel text-3xl mb-4 animate-pulse">[ INITIATING_DATA_TRANSFER... ]</div>
      </div>

      <!-- Помилка -->
      <div v-else-if="error" class="w-full border-4 border-black py-32 flex flex-col items-center justify-center text-red-500 bg-red-100 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] mb-12">
        <div class="font-pixel text-3xl mb-4">[ CONNECTION_FAILED ]</div>
        <p class="font-bold text-xl text-black">Не вдалося завантажити архів конференцій.</p>
      </div>

      <!-- СПИСОК КОНФЕРЕНЦІЙ (КВИТКИ) -->
      <div v-else class="flex flex-col gap-12">
        
        <div v-if="dbConferences.length === 0" class="border-4 border-dashed border-gray-400 p-12 text-center bg-white">
          <span class="font-pixel text-gray-400 text-xl">[ DATABASE_EMPTY ]</span>
          <p class="font-mono text-gray-500 mt-2">Конференцій ще не додано.</p>
        </div>

        <div 
          v-for="(conf, index) in dbConferences" 
          :key="conf.id"
          class="relative group cursor-crosshair"
          @click="openModal(conf)"
        >
          <!-- Декоративна скріпка/бірка -->
          <div class="absolute -top-4 -left-4 bg-yellow-400 text-black font-pixel text-[10px] px-3 py-1 uppercase border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] rotate-[-5deg] z-20 transition-transform group-hover:rotate-0">
            EVENT_ID: #{{ String(conf.id).padStart(4, '0') }}
          </div>

          <!-- ТІЛО КВИТКА -->
          <div class="flex flex-col md:flex-row border-4 border-black bg-white shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] group-hover:-translate-y-2 group-hover:translate-x-2 group-hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all duration-300">
            
            <!-- ДАТА (ЛІВА ЧАСТИНА КВИТКА) -->
            <div class="bg-black text-white p-6 md:w-48 shrink-0 flex flex-col justify-center items-center border-b-4 md:border-b-0 md:border-r-4 border-black relative overflow-hidden">
              <div class="text-5xl font-black font-pixel text-yellow-400 mb-1">
                {{ formatDay(conf.date_held) }}
              </div>
              <div class="text-xl font-bold uppercase tracking-widest">
                {{ formatMonthYear(conf.date_held) }}
              </div>
              
              <!-- Декоративний ASCII штрихкод -->
              <div class="mt-6 text-[8px] sm:text-[10px] text-gray-500 font-pixel tracking-tighter opacity-70">
                || | ||| || || | | ||
              </div>
            </div>

            <!-- ІНФОРМАЦІЯ (ЦЕНТРАЛЬНА ЧАСТИНА) -->
            <div class="p-6 md:p-8 flex-grow flex flex-col justify-between">
              <div>
                <h2 class="text-2xl md:text-3xl font-black uppercase tracking-tight leading-none mb-4 group-hover:text-blue-600 transition-colors">
                  {{ conf.title }}
                </h2>
                <!-- Текст конференції (Згорнутий) -->
                <p class="text-gray-700 text-sm md:text-base font-bold whitespace-pre-line line-clamp-3 leading-relaxed mb-4">
                  {{ conf.content }}
                </p>
              </div>
              
              <!-- Кнопка розгортання -->
              <div class="mt-4 flex justify-start">
                <button class="bg-blue-600 text-white font-pixel text-xs px-6 py-3 uppercase border-4 border-black group-hover:bg-yellow-400 group-hover:text-black transition-colors shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] active:translate-y-1 active:translate-x-1 active:shadow-none flex items-center gap-2">
                  <span>РОЗГОРНУТИ ДЕТАЛІ</span>
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M19 9l-7 7-7-7"></path></svg>
                </button>
              </div>
            </div>

            <!-- ФОТОГРАФІЯ (ПРАВА ЧАСТИНА) -->
            <div v-if="conf.photo" class="md:w-1/3 min-h-[200px] md:min-h-[250px] border-t-4 md:border-t-0 md:border-l-4 border-black shrink-0 relative overflow-hidden bg-black p-2">
              <div class="absolute top-4 right-4 z-10 bg-red-500 text-white font-pixel text-[8px] px-2 py-1 uppercase border-2 border-black">
                [ VISUAL_RECORD ]
              </div>
              <img 
                :src="conf.photo" 
                :alt="conf.title"
                class="w-full h-full object-cover border-2 border-zinc-800 filter grayscale contrast-125 brightness-90 group-hover:grayscale-0 group-hover:contrast-100 group-hover:brightness-100 group-hover:scale-105 transition-all duration-500"
              />
              <div class="absolute inset-0 bg-[linear-gradient(rgba(0,0,0,0)_50%,rgba(0,0,0,0.25)_50%)] bg-[length:100%_4px] pointer-events-none z-10 opacity-30"></div>
            </div>

          </div>
        </div>

      </div>
    </div>

    <!-- МОДАЛЬНЕ ВІКНО (FULL ACCESS DOSSIER) -->
    <Teleport to="body">
      <Transition name="modal">
        <!-- Додано z-[9999] щоб перекрити будь-який Layout/Header -->
        <div v-if="selectedConf" class="fixed inset-0 z-[9999] flex items-center justify-center p-4 md:p-6">
          <!-- Затемнення фону -->
          <div class="absolute inset-0 bg-black/80 backdrop-blur-sm cursor-pointer" @click="closeModal"></div>
          
          <!-- Контейнер Досьє -->
          <div class="relative w-full max-w-5xl bg-[#F4F4F0] border-8 border-black shadow-[16px_16px_0px_0px_rgba(234,179,8,1)] max-h-[95vh] overflow-y-auto flex flex-col">
            
            <!-- Хедер модалки -->
            <div class="bg-black text-white p-4 flex justify-between items-center sticky top-0 z-20 border-b-8 border-black">
              <div class="font-pixel text-yellow-400 text-sm md:text-base flex items-center gap-4">
                <span class="animate-pulse">●</span>
                <span>[ DECLASSIFIED_FILE // ID: {{ String(selectedConf.id).padStart(4, '0') }} ]</span>
              </div>
              <button @click="closeModal" class="bg-red-600 text-white font-pixel text-xl px-4 py-2 border-4 border-white hover:bg-white hover:text-red-600 transition-colors">
                X
              </button>
            </div>

            <!-- Тіло модалки -->
            <div class="p-6 md:p-12 flex flex-col gap-8">
              
              <div class="flex flex-col gap-2 border-l-8 border-yellow-400 pl-6">
                <div class="font-pixel text-gray-500 text-lg uppercase">
                  Дата фіксації: {{ formatFullDate(selectedConf.date_held) }}
                </div>
                <h2 class="text-4xl md:text-6xl font-black uppercase tracking-tighter leading-none text-black">
                  {{ selectedConf.title }}
                </h2>
              </div>

              <!-- Велике фото у модалці (ОНОВЛЕНЕ МАСШТАБУВАННЯ) -->
              <div v-if="selectedConf.photo" class="w-full border-8 border-black relative bg-black p-4 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] flex justify-center items-center min-h-[30vh]">
                <div class="absolute top-4 left-4 z-10 bg-black text-green-400 font-pixel text-[10px] px-3 py-2 uppercase border-2 border-green-400 shadow-[2px_2px_0px_0px_rgba(74,222,128,1)]">
                  > ENHANCED_VISUAL
                </div>
                <!-- Замінено object-cover на object-contain, щоб фото не обрізалось, і встановлено ліміт висоти 60vh -->
                <img :src="selectedConf.photo" :alt="selectedConf.title" class="max-w-full h-auto max-h-[60vh] object-contain border-2 border-zinc-800" />
              </div>

              <!-- Повний текст -->
              <div class="bg-white border-4 border-black p-6 md:p-10 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
                <div class="font-pixel text-red-500 text-sm mb-6 border-b-2 border-dashed border-gray-300 pb-2">
                  [ DATA_STREAM_START ]
                </div>
                <p class="text-gray-800 text-lg md:text-xl font-medium whitespace-pre-line leading-relaxed font-mono">
                  {{ selectedConf.content }}
                </p>
                <div class="font-pixel text-red-500 text-sm mt-6 border-t-2 border-dashed border-gray-300 pt-2 text-right">
                  [ EOF ]
                </div>
              </div>

              <!-- Лінк на матеріали -->
              <div v-if="selectedConf.link" class="flex justify-center mt-4 mb-4">
                <a :href="selectedConf.link" target="_blank" class="bg-blue-600 text-white font-pixel text-lg px-8 py-4 uppercase border-4 border-black hover:bg-yellow-400 hover:text-black transition-colors shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] active:translate-y-2 active:translate-x-2 active:shadow-none flex items-center gap-4">
                  <span>ПЕРЕЙТИ ДО МАТЕРІАЛІВ</span>
                  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path></svg>
                </a>
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

// Підключення до API
const { data: dbConferences, pending, error } = await useFetch('https://mit-site-3t9h.vercel.app/api/v1/conferences/', {
  default: () => []
});

// Логіка модального вікна
const selectedConf = ref(null);

const openModal = (conf) => {
  selectedConf.value = conf;
  // Блокуємо скрол сторінки під модалкою
  if (import.meta.client) {
    document.body.style.overflow = 'hidden';
  }
};

const closeModal = () => {
  selectedConf.value = null;
  // Відновлюємо скрол
  if (import.meta.client) {
    document.body.style.overflow = 'auto';
  }
};

// Форматування дат
const formatDay = (dateString) => {
  if (!dateString) return 'XX';
  return new Date(dateString).getDate().toString().padStart(2, '0');
};

const formatMonthYear = (dateString) => {
  if (!dateString) return 'XXXX';
  const date = new Date(dateString);
  const month = date.toLocaleDateString('uk-UA', { month: 'short' });
  const year = date.getFullYear();
  return `${month} ${year}`;
};

const formatFullDate = (dateString) => {
  if (!dateString) return 'НЕВІДОМО';
  return new Date(dateString).toLocaleDateString('uk-UA', { 
    day: '2-digit', 
    month: 'long', 
    year: 'numeric' 
  });
};
</script>

<style scoped>
/* Анімація появи модального вікна */
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
</style>
