<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-cyan-400 selection:text-black pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Креслення / Blueprint) -->
    <div class="absolute inset-0 opacity-20 bg-[linear-gradient(#cbd5e1_1px,transparent_1px),linear-gradient(90deg,#cbd5e1_1px,transparent_1px)] bg-[size:30px_30px] pointer-events-none"></div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-16 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-cyan-600 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(6,182,212,1)]">[ DIGITAL_LIBRARY ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter">
            НАВЧАЛЬНІ <br><span class="text-white bg-black px-3 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">ПОСІБНИКИ</span>
          </h1>
        </div>
      </div>

      <!-- Статус завантаження -->
      <div v-if="pending" class="w-full border-4 border-dashed border-gray-400 py-32 flex flex-col items-center justify-center text-gray-500 bg-white mb-12">
        <div class="font-pixel text-3xl mb-4 animate-pulse text-cyan-600">[ FETCHING_ARCHIVES... ]</div>
      </div>

      <!-- Помилка -->
      <div v-else-if="error" class="w-full border-4 border-black py-32 flex flex-col items-center justify-center text-red-500 bg-red-100 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] mb-12">
        <div class="font-pixel text-3xl mb-4">[ DATABASE_ERROR ]</div>
        <p class="font-bold text-xl text-black">Не вдалося підключитися до бібліотечного сервера.</p>
      </div>

      <!-- СІТКА ПОСІБНИКІВ -->
      <div v-else class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-10">
        
        <div v-if="dbTextbooks.length === 0" class="col-span-full border-4 border-dashed border-gray-400 p-12 text-center bg-white">
          <span class="font-pixel text-gray-400 text-xl">[ ARCHIVE_EMPTY ]</span>
          <p class="font-mono text-gray-500 mt-2">Посібників ще не завантажено у систему.</p>
        </div>

        <div 
          v-for="(book, index) in dbTextbooks" 
          :key="book.id"
          class="flex flex-col border-4 border-black bg-white shadow-[12px_12px_0px_0px_rgba(6,182,212,1)] hover:-translate-y-2 hover:translate-x-2 hover:shadow-[4px_4px_0px_0px_rgba(6,182,212,1)] transition-all duration-300 relative group cursor-pointer"
          @click="openModal(book)"
        >
          <!-- КОРІНЕЦЬ КНИГИ -->
          <div class="bg-cyan-400 text-black font-pixel text-[10px] p-3 flex justify-between items-center border-b-4 border-black uppercase">
            <span>VOL.{{ String(index + 1).padStart(2, '0') }} // {{ book.publication_year || 'N/A' }}</span>
            <span class="bg-black text-cyan-400 px-2 py-1">MANUAL</span>
          </div>

          <!-- ОБКЛАДИНКА -->
          <div class="relative w-full aspect-[3/4] border-b-4 border-black bg-zinc-900 overflow-hidden flex items-center justify-center">
            <template v-if="book.cover_image">
              <img 
                :src="book.cover_image" 
                :alt="book.title"
                class="w-full h-full object-cover filter contrast-125 brightness-95 group-hover:scale-105 transition-transform duration-500"
              />
            </template>
            <template v-else>
              <div class="absolute inset-4 border-4 border-dashed border-zinc-700 flex flex-col items-center justify-center p-4 text-center z-10">
                <svg class="w-16 h-16 text-zinc-600 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                <span class="font-pixel text-zinc-500 text-xs">[ NO_COVER_DATA ]</span>
              </div>
            </template>
            
            <div class="absolute bottom-0 left-0 w-full bg-cyan-400 text-black font-pixel text-sm p-3 uppercase border-t-4 border-black translate-y-full group-hover:translate-y-0 transition-transform duration-300 z-20 flex justify-between items-center">
              <span>READ_FILE</span>
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
            </div>
          </div>

          <!-- ІНФОРМАЦІЯ -->
          <div class="p-6 flex-grow flex flex-col justify-between bg-white relative">
            <div class="absolute bottom-0 right-0 w-6 h-6 bg-cyan-400 border-t-4 border-l-4 border-black"></div>
            <div>
              <h2 class="text-xl md:text-2xl font-black uppercase tracking-tight leading-tight mb-4 group-hover:text-cyan-600 transition-colors line-clamp-3">
                {{ book.title }}
              </h2>
              <div class="mb-2">
                <div class="font-pixel text-[8px] text-gray-500 mb-1 uppercase">AUTHORS:</div>
                <div class="font-bold text-sm text-black border-l-4 border-cyan-500 pl-3">
                  {{ book.authors_list }}
                </div>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

    <!-- МОДАЛЬНЕ ВІКНО (READING ROOM) -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedBook" class="fixed inset-0 z-[9999] flex items-center justify-center p-4 md:p-6">
          
          <div class="absolute inset-0 bg-black/90 backdrop-blur-sm cursor-pointer" @click="closeModal"></div>
          
          <div class="relative w-full max-w-6xl bg-[#F4F4F0] border-8 border-black shadow-[16px_16px_0px_0px_rgba(6,182,212,1)] max-h-[95vh] h-full md:h-auto flex flex-col md:flex-row overflow-hidden">
            
            <!-- ГЛОБАЛЬНА КНОПКА ЗАКРИТТЯ В ПРАВОМУ ВЕРХНЬОМУ КУТІ -->
            <button @click="closeModal" class="absolute top-4 right-4 z-[100] bg-red-500 text-black font-pixel text-xl w-12 h-12 flex items-center justify-center border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-y-1 hover:translate-x-1 hover:shadow-none transition-all cursor-pointer">
              X
            </button>

            <!-- ЛІВА ПАНЕЛЬ: ОБКЛАДИНКА -->
            <div class="md:w-2/5 bg-black border-b-8 md:border-b-0 md:border-r-8 border-black p-6 flex flex-col items-center justify-center shrink-0">
              <div class="w-full font-pixel text-cyan-400 text-xs mb-6 uppercase flex justify-between items-center hidden md:flex">
                <span>[ TERMINAL_READER ]</span>
                <span class="animate-pulse">● REC</span>
              </div>

              <div class="w-full max-w-sm aspect-[3/4] border-4 border-zinc-700 bg-zinc-900 flex items-center justify-center overflow-hidden relative shadow-[8px_8px_0px_0px_rgba(6,182,212,0.5)]">
                <img v-if="selectedBook.cover_image" :src="selectedBook.cover_image" :alt="selectedBook.title" class="w-full h-full object-contain" />
                <div v-else class="text-zinc-600 text-center p-4">
                   <svg class="w-16 h-16 mx-auto mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"></path></svg>
                   <span class="font-pixel text-[10px]">[ NO_COVER ]</span>
                </div>
              </div>
            </div>

            <!-- ПРАВА ПАНЕЛЬ -->
            <div class="md:w-3/5 flex flex-col bg-[#F4F4F0] h-full relative overflow-hidden">
              
              <!-- Зона, яка скролиться (Текст) -->
              <div class="flex-grow overflow-y-auto p-6 md:p-10 relative">
                
                <div class="absolute -right-10 top-20 font-black text-[120px] text-black opacity-5 font-mono pointer-events-none select-none rotate-90 origin-right">
                  {{ selectedBook.publication_year || 'MANUAL' }}
                </div>

                <div class="relative z-10 pr-12"> <!-- pr-12 залишає місце для кнопки X -->
                  <div class="inline-block bg-black text-white font-pixel text-[10px] px-3 py-2 border-4 border-cyan-400 mb-6 uppercase w-fit">
                    INDEX: {{ selectedBook.publication_year ? selectedBook.publication_year : 'UNDEFINED_YEAR' }}
                  </div>
                  
                  <h2 class="text-3xl md:text-5xl font-black uppercase tracking-tight leading-none text-black mb-6">
                    {{ selectedBook.title }}
                  </h2>

                  <div class="bg-white border-4 border-black p-4 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] mb-8">
                    <div class="font-pixel text-xs text-gray-500 mb-2 uppercase">АВТОРСЬКИЙ КОЛЕКТИВ:</div>
                    <div class="font-bold text-lg text-black leading-tight">
                      {{ selectedBook.authors_list }}
                    </div>
                  </div>

                  <div class="border-t-4 border-dashed border-black pt-6 pb-4">
                    <div class="font-pixel text-cyan-600 text-sm mb-4 uppercase">
                      > АНОТАЦІЯ ТА ОПИС:
                    </div>
                    <p class="text-gray-800 text-base md:text-lg font-medium whitespace-pre-line leading-relaxed font-mono">
                      {{ selectedBook.description }}
                    </p>
                  </div>
                </div>
              </div>

              <!-- НОВА ПЕРЕРОБЛЕНА КНОПКА ЗАВАНТАЖЕННЯ (ФІКСОВАНА ВНИЗУ) -->
              <div class="shrink-0 p-6 md:px-10 md:pb-10 pt-4 border-t-4 border-black bg-[#F4F4F0] z-20">
                <a v-if="selectedBook.link" :href="selectedBook.link" target="_blank" class="group flex w-full border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:translate-y-2 hover:translate-x-2 hover:shadow-none transition-all cursor-pointer bg-cyan-400">
                  <div class="flex-grow flex items-center justify-center font-pixel text-lg md:text-xl text-black py-4 px-4 uppercase tracking-widest font-black text-center leading-tight">
                    > ВІДКРИТИ МАТЕРІАЛИ
                  </div>
                  <div class="w-16 md:w-20 border-l-4 border-black bg-black text-cyan-400 flex items-center justify-center group-hover:bg-white group-hover:text-black transition-colors shrink-0">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                  </div>
                </a>
                
                <div v-else class="flex w-full border-4 border-zinc-400 bg-zinc-200 cursor-not-allowed">
                  <div class="flex-grow flex items-center justify-center font-pixel text-sm md:text-base text-zinc-500 py-4 px-4 uppercase tracking-widest font-black text-center leading-tight">
                    [ ФАЙЛ НЕДОСТУПНИЙ ]
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </Transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref } from 'vue';

const { data: dbTextbooks, pending, error } = await useFetch('https://mit-site-3t9h.vercel.app/api/v1/textbooks/', {
  default: () => []
});

const selectedBook = ref(null);

const openModal = (book) => {
  selectedBook.value = book;
  if (import.meta.client) {
    document.body.style.overflow = 'hidden';
  }
};

const closeModal = () => {
  selectedBook.value = null;
  if (import.meta.client) {
    document.body.style.overflow = 'auto';
  }
};
</script>

<style scoped>
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
