<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-blue-600 selection:text-white pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Сітка) -->
    <div class="absolute inset-0 opacity-10 bg-[linear-gradient(#000_1px,transparent_1px),linear-gradient(90deg,#000_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-12 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-blue-600 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(37,99,235,1)]">[ ACADEMIC_HUB ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter">
            ОСВІТНІЙ <br><span class="text-white bg-black px-3 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">ПРОЦЕС</span>
          </h1>
        </div>
        
        <div class="flex flex-col gap-2 shrink-0">
          <NuxtLink to="/" class="font-pixel text-xs bg-white text-black px-6 py-3 uppercase border-4 border-black hover:bg-blue-600 hover:text-white transition-colors shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] text-center">
            ← НА ГОЛОВНУ
          </NuxtLink>
        </div>
      </div>

      <!-- СТАТУС ЗАВАНТАЖЕННЯ -->
      <div v-if="pending" class="w-full border-4 border-dashed border-gray-400 py-32 flex flex-col items-center justify-center text-gray-500 bg-white mb-12">
        <div class="font-pixel text-3xl mb-4 animate-pulse text-blue-600">[ MOUNTING_FILE_SYSTEM... ]</div>
      </div>

      <div v-else-if="error" class="w-full border-4 border-black py-32 flex flex-col items-center justify-center text-red-500 bg-red-100 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] mb-12">
        <div class="font-pixel text-3xl mb-4">[ CONNECTION_FAILED ]</div>
        <p class="font-bold text-xl text-black">Не вдалося завантажити академічну базу даних.</p>
      </div>

      <div v-else-if="!sections || sections.length === 0" class="border-4 border-dashed border-gray-400 p-12 text-center bg-white">
        <span class="font-pixel text-gray-400 text-xl">[ DIRECTORY_EMPTY ]</span>
        <p class="font-mono text-gray-500 mt-2">Розділи освітнього процесу ще не створені.</p>
      </div>

      <!-- ОСНОВНИЙ КОНТЕНТ (САЙДБАР + ДАНІ) -->
      <div v-else class="flex flex-col lg:flex-row gap-10">
        
        <!-- САЙДБАР (Навігація по розділах) -->
        <div class="w-full lg:w-1/4 shrink-0 flex flex-col gap-4">
          <div class="font-pixel text-xs text-gray-500 uppercase border-b-4 border-black pb-2 mb-2">
            // DIRECTORIES
          </div>
          
          <button 
            v-for="section in sections" 
            :key="section.id"
            @click="activeSectionId = section.id"
            class="text-left font-bold uppercase p-4 border-4 border-black transition-all cursor-pointer flex justify-between items-center group"
            :class="activeSectionId === section.id ? 'bg-black text-white shadow-none translate-x-1 translate-y-1' : 'bg-white text-black shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:bg-yellow-400'"
          >
            <span class="truncate pr-4">{{ section.title }}</span>
            <span v-if="activeSectionId === section.id" class="font-pixel text-yellow-400 text-sm animate-pulse">●</span>
            <span v-else class="font-pixel text-gray-400 text-sm group-hover:text-black">></span>
          </button>
        </div>

        <!-- ПРАВА ПАНЕЛЬ (Вміст вибраного розділу) -->
        <div class="w-full lg:w-3/4">
          <Transition name="fade-slide" mode="out-in">
            <div :key="activeSectionId" v-if="activeSection" class="flex flex-col gap-10">
              
              <!-- Заголовок та Інтро розділу -->
              <div class="bg-white border-4 border-black p-8 shadow-[8px_8px_0px_0px_rgba(37,99,235,1)] relative">
                <div class="absolute -top-4 -right-4 bg-yellow-400 text-black font-pixel text-[10px] px-3 py-1 border-2 border-black shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] z-10">
                  ID: {{ activeSection.slug }}
                </div>
                <h2 class="text-3xl md:text-5xl font-black uppercase tracking-tighter mb-4 text-black border-b-4 border-dashed border-gray-300 pb-4">
                  {{ activeSection.title }}
                </h2>
                <div v-if="activeSection.intro" class="prose prose-lg max-w-none font-mono font-medium text-gray-700 leading-relaxed whitespace-pre-line">
                  {{ activeSection.intro }}
                </div>
              </div>

              <!-- ГРУПИ ПОСИЛАНЬ -->
              <div v-if="activeSection.groups && activeSection.groups.length > 0" class="flex flex-col gap-12">
                <div v-for="group in activeSection.groups" :key="group.id" class="border-t-8 border-black pt-8">
                  
                  <h3 v-if="group.title" class="text-2xl font-black uppercase mb-6 flex items-center gap-4">
                    <span class="text-blue-600 font-pixel">#</span>
                    {{ group.title }}
                  </h3>
                  
                  <!-- СІТКА ПОСИЛАНЬ -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <a 
                      v-for="link in group.links" 
                      :key="link.id"
                      :href="link.href" 
                      target="_blank"
                      class="flex flex-col bg-white border-4 border-black p-5 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-1 hover:translate-x-1 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] transition-all group"
                    >
                      <div class="flex justify-between items-start mb-3 gap-4">
                        <div class="font-pixel text-[10px] text-white bg-black px-2 py-1 uppercase border border-black group-hover:bg-blue-600 transition-colors">
                          FILE_LINK
                        </div>
                        <div v-if="link.note" class="font-pixel text-[8px] text-black bg-yellow-300 px-2 py-1 border border-black uppercase text-right">
                          {{ link.note }}
                        </div>
                      </div>
                      
                      <h4 class="text-lg font-bold uppercase leading-tight group-hover:text-blue-600 transition-colors">
                        {{ link.title }}
                      </h4>
                      
                      <div class="mt-auto pt-4 flex justify-end">
                        <svg class="w-6 h-6 text-black group-hover:text-blue-600 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                      </div>
                    </a>
                  </div>
                  
                </div>
              </div>

              <!-- ГАЛЕРЕЯ / СЕРТИФІКАТИ -->
              <div v-if="activeSection.images && activeSection.images.length > 0" class="border-t-8 border-black pt-8">
                <h3 class="text-2xl font-black uppercase mb-6 flex items-center gap-4">
                  <span class="text-yellow-500 font-pixel">@</span>
                  ДОКУМЕНТИ ТА СЕРТИФІКАТИ
                </h3>
                <div class="grid grid-cols-2 md:grid-cols-3 gap-4">
                  <div 
                    v-for="img in activeSection.images" 
                    :key="img.id"
                    @click="openImageModal(img)"
                    class="relative aspect-[3/4] border-4 border-black bg-zinc-200 cursor-pointer shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-1 hover:shadow-[6px_6px_0px_0px_rgba(37,99,235,1)] transition-all group overflow-hidden"
                  >
                    <img 
                      :src="img.image.startsWith('http') ? img.image : `http://127.0.0.1:8000${img.image}`" 
                      :alt="img.caption"
                      class="w-full h-full object-cover grayscale opacity-80 group-hover:grayscale-0 group-hover:opacity-100 group-hover:scale-105 transition-all duration-300"
                    />
                    <div class="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-opacity flex items-center justify-center">
                      <span class="bg-white text-black font-pixel text-xs px-3 py-2 uppercase border-2 border-black">VIEW</span>
                    </div>
                    <div v-if="img.caption" class="absolute bottom-0 left-0 w-full bg-black text-white font-pixel text-[8px] p-2 truncate">
                      {{ img.caption }}
                    </div>
                  </div>
                </div>
              </div>

            </div>
          </Transition>
        </div>

      </div>
    </div>

    <!-- МОДАЛЬНЕ ВІКНО ДЛЯ СЕРТИФІКАТІВ -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selectedImage" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/90 p-4 md:p-8 cursor-pointer backdrop-blur-sm" @click="closeImageModal">
          <div class="relative max-w-5xl w-full max-h-[90vh] bg-[#F4F4F0] border-4 border-black p-4 shadow-[12px_12px_0px_0px_rgba(250,204,21,1)] cursor-default flex flex-col items-center" @click.stop>
            
            <button @click="closeImageModal" class="absolute -top-6 -right-6 md:-top-8 md:-right-8 bg-red-500 border-2 border-black text-white font-pixel px-4 py-2 text-lg md:text-2xl hover:bg-black transition-colors shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] z-10 cursor-pointer">
              X
            </button>
            
            <img 
              :src="selectedImage.image.startsWith('http') ? selectedImage.image : `http://127.0.0.1:8000${selectedImage.image}`" 
              class="max-w-full max-h-[75vh] object-contain border-2 border-black bg-white" 
            />
            
            <div v-if="selectedImage.caption" class="w-full mt-4 bg-black text-white font-mono text-center p-3 text-lg uppercase font-bold border-2 border-black">
              {{ selectedImage.caption }}
            </div>
            
          </div>
        </div>
      </Transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, watch } from 'vue';

// Увага: перевір свій URL до API. Зазвичай це щось типу /api/v1/edu-sections/
const { data: sections, pending, error } = await useFetch('http://127.0.0.1:8000/api/v1/edu-sections/');

// Стан активного розділу
const activeSectionId = ref(null);

// Коли дані завантажилися, робимо перший розділ активним за замовчуванням
watch(sections, (newSections) => {
  if (newSections && newSections.length > 0 && !activeSectionId.value) {
    activeSectionId.value = newSections[0].id;
  }
}, { immediate: true });

// Обчислюємо активний розділ
const activeSection = computed(() => {
  if (!sections.value) return null;
  return sections.value.find(s => s.id === activeSectionId.value) || null;
});

// Логіка модального вікна для зображень (сертифікатів)
const selectedImage = ref(null);

const openImageModal = (img) => {
  selectedImage.value = img;
  if (import.meta.client) document.body.style.overflow = 'hidden';
};

const closeImageModal = () => {
  selectedImage.value = null;
  if (import.meta.client) document.body.style.overflow = 'auto';
};
</script>

<style scoped>
/* Анімація перемикання вкладок */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

/* Анімація модального вікна */
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