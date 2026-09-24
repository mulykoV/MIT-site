<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-yellow-400 selection:text-black pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Хвилі/ТБ-шум) -->
    <div class="absolute inset-0 opacity-10 bg-[repeating-linear-gradient(0deg,transparent,transparent_2px,#000_2px,#000_4px)] pointer-events-none"></div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-16 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-blue-600 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(37,99,235,1)]">[ VIDEO_LOGS_ARCHIVE ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter">
            СТУДЕНТИ <br><span class="text-white bg-black px-3 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">ПРО НАС</span>
          </h1>
        </div>
        
        <div class="flex flex-col gap-2 shrink-0">
          <NuxtLink to="/" class="font-pixel text-xs bg-white text-black px-6 py-3 uppercase border-4 border-black hover:bg-yellow-400 hover:text-black transition-colors shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] text-center">
            ← НА ГОЛОВНУ
          </NuxtLink>
        </div>
      </div>

      <!-- СІТКА ВІДЕО-ЛОГІВ -->
      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-10 auto-rows-auto">
        
        <div 
          v-for="(item, index) in mediaItems" 
          :key="index"
          class="flex flex-col border-4 border-black bg-white shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-2 hover:translate-x-2 transition-all duration-300 relative group cursor-pointer"
          :class="`hover:shadow-[4px_4px_0px_0px_${item.shadowColor}]`"
          @click="openMedia(item)"
        >
          <!-- ШАПКА "ПЛЕЄРА" -->
          <div class="bg-black text-white p-2 md:p-3 flex justify-between items-center border-b-4 border-black">
            <span class="font-pixel text-[10px] text-zinc-400 uppercase">TAPE_{{ String(index + 1).padStart(2, '0') }}</span>
            <div class="flex items-center gap-3">
              <span class="font-pixel text-[10px] animate-pulse" :class="item.type === 'terminal' ? 'text-green-400' : 'text-red-500'">
                ● {{ item.type === 'terminal' ? 'EXECUTING' : 'REC' }}
              </span>
              <span class="font-pixel text-[10px] text-white">00:00:00:00</span>
            </div>
          </div>

          <!-- ЗОНА ОБКЛАДИНКИ -->
          <div class="relative w-full aspect-video border-b-4 border-black bg-zinc-900 overflow-hidden">
            
            <!-- ТИП 1: YOUTUBE ВІДЕО -->
            <template v-if="item.type === 'youtube'">
              <img 
                :src="`https://img.youtube.com/vi/${extractYouTubeId(item.url)}/maxresdefault.jpg`" 
                :alt="item.title"
                class="w-full h-full object-cover filter grayscale contrast-125 brightness-75 group-hover:grayscale-0 group-hover:brightness-100 group-hover:scale-105 transition-all duration-500"
                onerror="this.src='https://img.youtube.com/vi/'+this.getAttribute('data-id')+'/hqdefault.jpg'"
                :data-id="extractYouTubeId(item.url)"
              />
              <div class="absolute inset-0 flex items-center justify-center z-20">
                <div class="bg-red-600 border-4 border-black w-16 h-12 md:w-20 md:h-14 flex items-center justify-center shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] group-hover:scale-110 group-hover:bg-white transition-all duration-300">
                  <svg class="w-8 h-8 text-white group-hover:text-red-600 ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                </div>
              </div>
            </template>

            <!-- ТИП 2: FACEBOOK ВІДЕО -->
            <template v-else-if="item.type === 'facebook'">
              <div class="w-full h-full bg-blue-600 flex flex-col items-center justify-center text-white border-8 border-blue-800 border-dashed group-hover:bg-blue-500 transition-colors">
                <span class="font-black text-6xl mb-2">f</span>
                <span class="font-pixel text-[10px] bg-black px-2 py-1">[ SECURE_FB_STREAM ]</span>
              </div>
              <div class="absolute inset-0 flex items-center justify-center z-20">
                <div class="bg-black border-4 border-white w-16 h-12 md:w-20 md:h-14 flex items-center justify-center shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] group-hover:scale-110 transition-all duration-300 mt-16">
                  <svg class="w-8 h-8 text-white ml-1" fill="currentColor" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>
                </div>
              </div>
            </template>

            <!-- ТИП 3: PYTHON TERMINAL -->
            <template v-else-if="item.type === 'terminal'">
              <div class="w-full h-full bg-black p-4 text-green-400 font-mono text-[10px] md:text-xs overflow-hidden flex flex-col relative z-20">
                <div class="text-zinc-500 mb-2 font-bold">root@mit-server:~/lessons# python3 basics.py</div>
                <div class="whitespace-pre text-green-400 font-bold tracking-tight">
                  {{ typedText }}<span class="animate-pulse bg-green-400 text-black">_</span>
                </div>
              </div>
            </template>
            
            <!-- Ефект телевізійних смуг (лише для відео) -->
            <div v-if="item.type !== 'terminal'" class="absolute inset-0 bg-[linear-gradient(rgba(0,0,0,0)_50%,rgba(0,0,0,0.25)_50%)] bg-[length:100%_4px] pointer-events-none z-10 opacity-30"></div>
            
            <!-- Нижня плашка -->
            <div class="absolute bottom-2 right-2 bg-black text-white font-pixel text-[8px] md:text-[10px] px-2 py-1 border-2 border-white z-20">
              {{ item.type === 'terminal' ? 'VIEW_CONSOLE' : 'PLAY_MEDIA' }}
            </div>
          </div>

          <!-- ІНФОРМАЦІЯ (Різнобарвні блоки) -->
          <div :class="`p-6 flex-grow flex flex-col justify-between border-b-8 ${item.bgClass}`">
            <div>
              <!-- Теги -->
              <div class="flex flex-wrap gap-2 mb-4">
                <span class="font-pixel text-[8px] bg-black text-white px-2 py-1 uppercase border border-black shadow-[2px_2px_0px_0px_rgba(0,0,0,0.3)]">#PROJECT</span>
                <span class="font-pixel text-[8px] bg-white text-black px-2 py-1 uppercase border border-black shadow-[2px_2px_0px_0px_rgba(0,0,0,0.3)]">{{ item.subject }}</span>
              </div>
              
              <h2 class="text-xl md:text-2xl font-black uppercase tracking-tight leading-tight mb-4 group-hover:underline decoration-4 underline-offset-4">
                {{ item.title }}
              </h2>
              
              <p class="text-black font-mono text-sm md:text-base font-medium leading-relaxed line-clamp-4">
                {{ item.description }}
              </p>
            </div>
          </div>
          
          <!-- НИЖНЯ ПАНЕЛЬКА (Автор) -->
          <div class="bg-white p-4 flex items-center gap-3">
            <div class="w-10 h-10 bg-zinc-200 border-2 border-black rounded-full overflow-hidden shrink-0 flex items-center justify-center">
              <svg class="w-6 h-6 text-zinc-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
            </div>
            <div>
              <div class="font-pixel text-[8px] text-gray-500 uppercase">CREATOR</div>
              <div class="font-bold text-sm uppercase">{{ item.author }}</div>
            </div>
          </div>

        </div>

      </div>
    </div>

    <!-- МОДАЛЬНИЙ ВІДЕОПЛЕЄР / ТЕРМІНАЛ -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedItem" class="fixed inset-0 z-[9999] flex items-center justify-center p-2 md:p-6">
          
          <div class="absolute inset-0 bg-black/95 backdrop-blur-md cursor-pointer" @click="closeMedia"></div>
          
          <!-- ГЛОБАЛЬНА КНОПКА ЗАКРИТТЯ -->
          <button @click="closeMedia" class="absolute top-4 right-4 z-[10000] bg-red-600 text-white font-pixel text-xl w-12 h-12 flex items-center justify-center border-4 border-black shadow-[4px_4px_0px_0px_rgba(255,255,255,1)] hover:translate-y-1 hover:translate-x-1 hover:shadow-none transition-all cursor-pointer">
            X
          </button>

          <div class="relative w-full max-w-6xl flex flex-col lg:flex-row bg-[#F4F4F0] border-8 border-black shadow-[16px_16px_0px_0px_rgba(255,255,255,0.2)] max-h-[95vh] overflow-hidden">
            
            <!-- ПЛЕЄР (ЛІВА/ВЕРХНЯ ЧАСТИНА) -->
            <div class="w-full lg:w-3/4 bg-black border-b-8 lg:border-b-0 lg:border-r-8 border-black relative">
              
              <!-- Декоративна рамка плеєра -->
              <div class="absolute top-0 left-0 w-full p-2 flex justify-between z-10 pointer-events-none">
                <span class="font-pixel text-[10px] text-white bg-black/50 px-2 py-1">SYS_STREAM_ACTIVE</span>
                <span class="font-pixel text-[10px] bg-black/50 px-2 py-1 animate-pulse" :class="selectedItem.type === 'terminal' ? 'text-green-400' : 'text-red-500'">
                  ● {{ selectedItem.type === 'terminal' ? 'RUNNING' : 'LIVE' }}
                </span>
              </div>
              
              <div class="w-full aspect-video flex items-center justify-center bg-zinc-900">
                <!-- YouTube -->
                <iframe 
                  v-if="selectedItem.type === 'youtube'"
                  class="w-full h-full"
                  :src="`https://www.youtube.com/embed/${extractYouTubeId(selectedItem.url)}?autoplay=1`" 
                  title="YouTube video player" 
                  frameborder="0" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                  allowfullscreen>
                </iframe>
                
                <!-- Facebook -->
                <iframe 
                  v-else-if="selectedItem.type === 'facebook'"
                  class="w-full h-full"
                  :src="selectedItem.url" 
                  style="border:none;overflow:hidden" 
                  scrolling="no" 
                  frameborder="0" 
                  allowfullscreen="true" 
                  allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share">
                </iframe>

                <!-- Terminal -->
                <div v-else-if="selectedItem.type === 'terminal'" class="w-full h-full bg-black p-8 text-green-400 font-mono text-sm md:text-lg overflow-y-auto">
                   <div class="text-zinc-500 mb-4 font-bold">> SYSTEM INITIATED...</div>
                   <div class="text-zinc-500 mb-6 font-bold">root@mit-server:~/lessons# python3 basics.py</div>
                   <div class="whitespace-pre text-green-400 font-bold leading-relaxed">
                     {{ typedText }}<span class="animate-pulse bg-green-400 text-black">_</span>
                   </div>
                </div>
              </div>
            </div>

            <!-- ІНФОРМАЦІЯ ПРО ПРОЄКТ (ПРАВА/НИЖНЯ ЧАСТИНА) -->
            <div class="w-full lg:w-1/4 p-6 md:p-8 flex flex-col bg-white overflow-y-auto">
              <div class="font-pixel text-[10px] text-gray-500 uppercase mb-2 border-b-2 border-dashed border-gray-300 pb-2">
                PROJECT_DETAILS
              </div>
              
              <h2 class="text-2xl md:text-3xl font-black uppercase leading-tight mb-4">
                {{ selectedItem.title }}
              </h2>
              
              <div class="bg-zinc-100 border-l-4 border-black p-4 mb-6">
                <div class="font-pixel text-[8px] text-gray-500 uppercase mb-1">AUTHOR</div>
                <div class="font-bold text-lg uppercase">{{ selectedItem.author }}</div>
                <div class="font-mono text-xs text-gray-600 mt-1">{{ selectedItem.subject }}</div>
              </div>

              <div class="flex-grow">
                <p class="font-mono text-sm md:text-base text-gray-800 leading-relaxed whitespace-pre-line">
                  {{ selectedItem.description }}
                </p>
              </div>
              
              <div class="mt-8 border-t-4 border-black pt-4 font-pixel text-[10px] text-center text-gray-400">
                [ END_OF_FILE ]
              </div>
            </div>

          </div>
        </div>
      </Transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

// РОЗУМНИЙ ПАРСЕР YOUTUBE ID (Приймає і повні лінки, і просто ID)
const extractYouTubeId = (url) => {
  if (!url) return '';
  if (url.length === 11 && !url.includes('/')) return url; // Це вже ID
  const regExp = /^.*(youtu.be\/|v\/|u\/\w\/|embed\/|watch\?v=|\&v=)([^#\&\?]*).*/;
  const match = url.match(regExp);
  return (match && match[2].length === 11) ? match[2] : '';
};

// АНІМАЦІЯ ДРУКУ ТЕКСТУ ДЛЯ ПАЙТОНУ
const pythonCode = `import time
from mit import student

def start_semester():
    skills = ['Python', 'Networks', 'DevOps']
    
    print("Loading curriculum...")
    for skill in skills:
        time.sleep(0.5)
        print(f"[*] Module acquired: {skill}")
        
    print("\\n> STUDENT STATUS: READY TO CODE!")

if __name__ == '__main__':
    start_semester()`;

const typedText = ref('');
let charIndex = 0;
let typingInterval = null;

const startTyping = () => {
  if (typingInterval) clearInterval(typingInterval);
  typedText.value = '';
  charIndex = 0;
  
  typingInterval = setInterval(() => {
    if (charIndex < pythonCode.length) {
      typedText.value += pythonCode.charAt(charIndex);
      charIndex++;
    } else {
      // Пауза перед перезапуском
      clearInterval(typingInterval);
      setTimeout(startTyping, 4000); 
    }
  }, 40); // Швидкість друку
};

onMounted(() => {
  startTyping();
});

onUnmounted(() => {
  if (typingInterval) clearInterval(typingInterval);
});


// ДАНІ 
const mediaItems = ref([
  {
    type: 'youtube',
    title: 'Бази даних та інформаційні системи',
    description: 'Вивчаються основи застосування баз даних в інформаційних системах, здійснюється набуття навичок у проектуванні та практичній роботі з базами даних.',
    author: 'Роман Миколайчук',
    subject: 'Дисципліна',
    url: 'https://www.youtube.com/embed/Jr3OLGWtO5o', 
    bgClass: 'bg-lime-400',
    shadowColor: 'rgba(132,204,22,1)'
  },
  {
    type: 'facebook',
    title: 'Захист інформації в інформаційних системах',
    description: 'Інформаційна безпека - багатогранна, багатовимірна область діяльності, в якій успіх може принести тільки системний, комплексний підхід. Спектр інтересів суб\'єктів, пов\'язаних з використанням інформаційних систем.',
    author: 'Студенти 4 курсу',
    subject: 'Кібербезпека',
    url: 'https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2F102787031309371%2Fvideos%2F735920867148846%2F&show_text=0&width=560', 
    bgClass: 'bg-cyan-400',
    shadowColor: 'rgba(6,182,212,1)'
  },
  {
    type: 'youtube',
    title: 'Обробка даних в інформаційних технологіях',
    description: 'На базі використання сучасних програмних засобів (Java, Spring, PostgreSQL) вивчаються основи розробки інформаційних систем для обробки даних.',
    author: 'Роман Миколайчук',
    subject: 'Розробка',
    url: 'https://www.youtube.com/embed/mMwcgFQyF7U', 
    bgClass: 'bg-yellow-400',
    shadowColor: 'rgba(250,204,21,1)'
  },
  {
    type: 'youtube',
    title: 'Електроніка та електротехніка',
    description: 'Мета викладання дисципліни - розкриття сучасних наукових концепцій, методів та технологій використання технічних рішень в області електротехніки і електроніки, побудови електричних кіл та їх розрахунок.',
    author: 'Роман Миколайчук',
    subject: 'Апаратне забезпечення',
    url: 'https://www.youtube.com/embed/RjY4qUsH_xk', 
    bgClass: 'bg-fuchsia-500 text-white',
    shadowColor: 'rgba(217,70,239,1)'
  },
  {
    type: 'terminal', // ОСЬ ТУТ КІБЕР-МАГІЯ!
    title: 'Основи програмування',
    description: 'Перші знайомства з мовою Python. Метою вивчення дисципліни є отримання теоретичних знань та практичних навичок програмування мовою Python, що дозволить розв\'язувати складні алгоритмічні задачі.',
    author: 'Студенти 1 курсу',
    subject: 'Програмування',
    url: '', // Лінку немає, бо це термінал
    bgClass: 'bg-red-500 text-white',
    shadowColor: 'rgba(239,68,68,1)'
  },
  {
    type: 'youtube',
    title: 'Програмно-апаратне забезпечення дисциплін',
    description: 'Розглядається програмно-апаратне забезпечення, яке використовується в мережах реальних підприємств. Мережеві інженери та адміністратори використовують ці продукти для перевірки роботи мережі, розгортки мережі, аналізу трафіка.',
    author: 'Наталія Дахно',
    subject: 'Мережеві технології',
    url: 'https://www.youtube.com/embed/HTx1RA356ok', 
    bgClass: 'bg-blue-500 text-white',
    shadowColor: 'rgba(59,130,246,1)'
  }
]);

const selectedItem = ref(null);

const openMedia = (item) => {
  selectedItem.value = item;
  if (import.meta.client) {
    document.body.style.overflow = 'hidden';
  }
};

const closeMedia = () => {
  selectedItem.value = null;
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