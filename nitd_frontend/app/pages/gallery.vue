<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-sans selection:bg-yellow-400 selection:text-black pb-32 pt-20 lg:pt-32 relative overflow-hidden">
    
    <!-- Технічна сітка на фоні -->
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#e5e7eb_1px,transparent_1px),linear-gradient(to_bottom,#e5e7eb_1px,transparent_1px)] bg-[size:32px_32px] pointer-events-none z-0"></div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-4 border-black pb-8 mb-12 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-mono text-yellow-600 text-sm md:text-base mb-4 uppercase tracking-widest font-bold bg-black px-2 py-1 w-fit">
            [ MEDIA_ARCHIVE_CORE ]
          </div>
          <h1 class="text-6xl md:text-8xl font-black uppercase tracking-tighter leading-[0.85]">
            ГАЛЕРЕЯ <br>
            <span class="text-transparent bg-clip-text bg-gradient-to-r from-yellow-500 to-orange-500">КАФЕДРИ</span>
          </h1>
        </div>
      </div>

      <!-- БЛОК СПОГАДІВ: "ЗГАДАЙТЕ ЦЕЙ МОМЕНТ!!!" -->
      <div v-if="randomMemory" class="mb-12 bg-white border-4 border-black p-4 md:p-8 shadow-[8px_8px_0px_0px_rgba(234,179,8,1)] flex flex-col lg:flex-row gap-8 items-center cursor-pointer group hover:-translate-y-1 transition-transform duration-300" @click="openImageModal(randomMemory.image)">
        
        <!-- Велике фото -->
        <div class="w-full lg:w-2/3 border-4 border-black overflow-hidden relative bg-zinc-100">
          <img 
            :src="randomMemory.image" 
            :alt="randomMemory.title" 
            class="w-full h-auto max-h-[500px] object-contain md:object-cover transition-transform duration-700 group-hover:scale-105"
          />
          <div class="absolute top-4 left-4 bg-yellow-400 text-black font-mono font-bold text-xs px-3 py-1 uppercase tracking-widest border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
            #SPOTLIGHT
          </div>
          <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity bg-black/20 backdrop-blur-sm pointer-events-none">
            <span class="bg-black text-white font-mono font-bold px-6 py-3 uppercase tracking-widest border-4 border-black text-xl">
              Відкрити [ ↗ ]
            </span>
          </div>
        </div>
        
        <!-- Текст спогаду -->
        <div class="w-full lg:w-1/3 flex flex-col">
          <div class="font-mono text-gray-500 text-xs uppercase tracking-widest mb-4 flex items-center gap-2">
            <span class="w-3 h-3 rounded-full bg-red-500 animate-pulse"></span> Випадковий спогад
          </div>
          <h2 class="text-4xl md:text-5xl font-black uppercase mb-6 leading-[1.1] tracking-tight">
            Згадайте <br><span class="text-yellow-500">цей момент!!!</span>
          </h2>
          <p class="font-bold text-gray-800 mb-8 text-lg leading-snug">
            {{ randomMemory.title }}
          </p>
          <div class="font-mono text-xs uppercase tracking-widest border-t-4 border-black pt-4 flex flex-col gap-2">
            <div><span class="text-gray-500">ДАТА:</span> <span class="font-bold text-black">{{ formatDate(randomMemory.created_at) }}</span></div>
            <div><span class="text-gray-500">КАТЕГОРІЯ:</span> <span class="font-bold text-black">{{ getCategoryName(randomMemory.category) }}</span></div>
          </div>
        </div>
      </div>

      <!-- ФІЛЬТРИ (Категорії) - ЗБІЛЬШЕНІ КНОПКИ -->
      <div class="flex flex-wrap gap-4 md:gap-6 mb-12 border-b-4 border-black pb-8">
        <button 
          v-for="cat in categories" 
          :key="cat.id"
          @click="activeCategory = cat.id"
          class="font-mono font-bold text-sm md:text-lg px-6 py-3 md:px-8 md:py-4 border-4 border-black transition-all shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] uppercase"
          :class="activeCategory === cat.id ? 'bg-yellow-400 text-black shadow-none translate-y-1.5 translate-x-1.5' : 'bg-white hover:bg-black hover:text-white'"
        >
          {{ cat.name }}
        </button>
      </div>

      <!-- GRID СІТКА (Гнучка, не розтягується) -->
      <div v-if="filteredGallery && filteredGallery.length > 0" class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-6">
        <div 
          v-for="item in filteredGallery" 
          :key="item.id"
          @click="openImageModal(item.image)"
          class="bg-white border-4 border-black p-3 flex flex-col shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-1 hover:shadow-[8px_8px_0px_0px_rgba(234,179,8,1)] transition-all duration-300 group cursor-crosshair h-fit"
        >
          <!-- Контейнер для фото (зберігає пропорції) -->
          <div class="w-full border-2 border-black mb-3 overflow-hidden bg-zinc-200 relative">
            <img 
              :src="item.image" 
              :alt="item.title"
              class="w-full h-auto object-cover transition-transform duration-500 group-hover:scale-105"
            />
            <div class="absolute top-2 right-2 bg-yellow-400 text-black font-mono font-bold text-[10px] px-2 py-1 uppercase tracking-widest opacity-0 group-hover:opacity-100 transition-opacity border-2 border-black shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
              [ ↗ ]
            </div>
          </div>
          
          <div class="flex flex-col">
            <h4 class="font-black text-sm uppercase leading-tight mb-3 group-hover:text-yellow-600 transition-colors">{{ item.title }}</h4>
            <div class="font-mono text-[9px] text-gray-500 uppercase tracking-widest border-t-2 border-dashed border-gray-300 pt-2 flex justify-between items-end">
              <span>CAT:<br><span class="font-bold text-black">{{ getCategoryName(item.category) }}</span></span>
              <span class="text-right">DATE:<br><span class="font-bold text-black">{{ formatDate(item.created_at) }}</span></span>
            </div>
          </div>
        </div>
      </div>

      <!-- ЯКЩО ФОТОК НЕМАЄ АБО ЗАВАНТАЖЕННЯ -->
      <div v-else class="border-4 border-dashed border-gray-400 p-16 text-center bg-white/50 backdrop-blur-sm flex flex-col items-center justify-center mt-8">
        <span v-if="pending" class="text-4xl animate-spin mb-4">⚙️</span>
        <span v-else class="text-5xl mb-4">📭</span>
        <span class="font-mono font-bold text-gray-500 text-lg uppercase tracking-widest">
          {{ pending ? '[ ЗАВАНТАЖЕННЯ АРХІВУ... ]' : '[ АРХІВ ПОРОЖНІЙ ]' }}
        </span>
      </div>

    </div>

    <!-- МОДАЛЬНЕ ВІКНО ДЛЯ ПОВНОЕКРАННОГО ПЕРЕГЛЯДУ -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedImage" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/95 p-4 md:p-8 cursor-pointer backdrop-blur-md" @click="closeImageModal">
          <div class="relative w-full max-w-7xl h-full flex justify-center items-center" @click.stop>
            <button @click="closeImageModal" class="absolute top-4 right-4 md:top-8 md:right-8 bg-white border-4 border-black text-black font-mono font-bold px-4 py-2 hover:bg-yellow-400 transition-colors shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] z-10 cursor-pointer uppercase">
              Закрити [x]
            </button>
            <img 
              :src="selectedImage" 
              class="max-w-full max-h-full object-contain border-8 border-black bg-white shadow-[16px_16px_0px_0px_rgba(234,179,8,1)] pointer-events-none" 
            />
          </div>
        </div>
      </Transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onUnmounted } from 'vue';

// --- ДАНІ ТА ФІЛЬТРАЦІЯ ---
const activeCategory = ref('all');

const categories = [
  { id: 'all', name: 'Всі файли' },
  { id: 'science', name: 'Наука' },
  { id: 'education', name: 'Навчання' },
  { id: 'students', name: 'Студентське життя' },
  { id: 'events', name: 'Івенти та Хакатони' }
];

// Отримуємо дані з Django API
const { data: galleryItems, pending } = await useFetch('http://127.0.0.1:8000/api/v1/gallery/');

// --- ЛОГІКА РАНДОМНОГО СПОГАДУ (SPOTLIGHT) ---
const randomMemory = ref(null);

// Функція для вибору випадкового фото
const pickRandomMemory = (items) => {
  if (items && items.length > 0) {
    const randomIndex = Math.floor(Math.random() * items.length);
    randomMemory.value = items[randomIndex];
  }
};

// Спостерігаємо за galleryItems, щоб вибрати фото одразу як прийдуть дані з сервера
watch(galleryItems, (newItems) => {
  pickRandomMemory(newItems);
}, { immediate: true });


// Фільтрація галереї (повертаємо пустий масив, якщо даних ще немає)
const filteredGallery = computed(() => {
  if (!galleryItems.value) return [];
  
  if (activeCategory.value === 'all') {
    return galleryItems.value;
  }
  return galleryItems.value.filter(item => item.category === activeCategory.value);
});


// --- ДОПОМІЖНІ ФУНКЦІЇ ДЛЯ ДАНИХ З DJANGO ---
// Форматування дати з "2025-10-12T14:30..." у "12.10.2025"
const formatDate = (dateString) => {
  if (!dateString) return 'N/A';
  const date = new Date(dateString);
  return date.toLocaleDateString('uk-UA');
};

// Конвертація ID категорії в людську назву
const getCategoryName = (catId) => {
  const category = categories.find(c => c.id === catId);
  return category ? category.name : catId;
};


// --- ЛОГІКА МОДАЛЬНОГО ВІКНА ---
const selectedImage = ref(null);

const openImageModal = (imgPath) => {
  selectedImage.value = imgPath;
  if (import.meta.client) document.body.style.overflow = 'hidden';
};

const closeImageModal = () => {
  selectedImage.value = null;
  if (import.meta.client) document.body.style.overflow = 'auto';
};

const handleKeydown = (e) => {
  if (e.key === 'Escape' && selectedImage.value) {
    closeImageModal();
  }
};

onMounted(() => {
  if (import.meta.client) window.addEventListener('keydown', handleKeydown);
});

onUnmounted(() => {
  if (import.meta.client) window.removeEventListener('keydown', handleKeydown);
});
</script>

<style scoped>
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
</style>