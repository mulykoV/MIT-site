<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-red-500 selection:text-white pb-32">
    
    <!-- ВЕРХНЯ СЕКЦІЯ: ТЕКСТ ТА СТАТУС -->
    <div class="pt-32 lg:pt-48 px-6 max-w-[1400px] mx-auto border-b-4 border-black pb-16 mb-16">
      <div class="flex flex-col lg:flex-row justify-between items-end gap-12">
        
        <!-- Ліва частина: Заголовок і текст -->
        <div class="max-w-3xl relative z-10">
          <div class="font-pixel text-blue-600 text-xl mb-4 uppercase tracking-widest">[ ACADEMIC_STAFF ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter leading-[0.9] mb-6">
            АКАДЕМІЧНИЙ <br><span class="text-black bg-blue-400 px-2 mt-2 inline-block">СКЛАД</span>
          </h1>
          <p class="text-xl font-bold text-gray-800 border-l-4 border-black pl-4">
            Державний університет — це міцний фундамент. А наші викладачі — це практики, архітектори систем та дослідники, які перетворюють теорію на реальний інженерний досвід.
          </p>
        </div>

        <!-- Права частина: Статус бази даних -->
        <div class="bg-white border-4 border-black p-4 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] w-full lg:w-auto relative z-10">
          <div class="font-pixel text-xs text-gray-500 mb-2">// SYSTEM_DB_STATUS</div>
          <div class="w-full lg:w-64 h-20 bg-black relative overflow-hidden flex items-center justify-center border-2 border-gray-800">
            <!-- Безпечний фон-сітка -->
            <div class="absolute inset-0 opacity-20 bg-[linear-gradient(#fff_1px,transparent_1px),linear-gradient(90deg,#fff_1px,transparent_1px)] bg-[size:10px_10px]"></div>
            <span class="font-pixel text-green-400 text-2xl relative z-10 flex items-center gap-3">
              <span class="w-3 h-3 bg-green-400 rounded-full animate-pulse"></span>
              ACTIVE: {{ teachersCount }}
            </span>
          </div>
        </div>

      </div>
    </div>

    <!-- НИЖНЯ СЕКЦІЯ: БАЗА ВИКЛАДАЧІВ (Сітка ID-карток) -->
    <div class="max-w-[1400px] mx-auto px-6">
      
      <div v-if="pending" class="w-full border-4 border-dashed border-gray-400 py-32 flex flex-col items-center justify-center text-gray-500 bg-white">
        <div class="font-pixel text-3xl mb-4 animate-pulse">[ DOWNLOADING_DOSSIERS... ]</div>
      </div>

      <div v-else-if="error" class="w-full border-4 border-black py-32 flex flex-col items-center justify-center text-red-500 bg-red-100 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)]">
        <div class="font-pixel text-3xl mb-4">[ FATAL_API_ERROR ]</div>
        <p class="font-bold text-xl text-black">Не вдалося підключитися до бази даних.</p>
      </div>

      <!-- Збільшено gap для більшого простору між картками -->
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
        
        <!-- Картка: ID Badge -->
        <div 
          v-for="teacher in teachers" 
          :key="teacher.id" 
          @click="openTeacherModal(teacher)"
          class="relative group border-4 border-black bg-white cursor-pointer shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:translate-x-1 hover:translate-y-1 hover:shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] transition-all flex flex-col"
        >
          <!-- Шапка картки з SVG-штрихкодом -->
          <div class="border-b-4 border-black px-4 py-3 flex justify-between items-center bg-[#F4F4F0] relative z-10">
            <div class="font-pixel text-[10px] text-gray-500 tracking-[0.1em]">ID:{{ String(teacher.id).padStart(4, '0') }}</div>
            <svg width="60" height="16" viewBox="0 0 100 20" preserveAspectRatio="none" class="opacity-80">
              <rect x="0" y="0" width="4" height="20" fill="black"/><rect x="6" y="0" width="2" height="20" fill="black"/><rect x="10" y="0" width="8" height="20" fill="black"/><rect x="20" y="0" width="2" height="20" fill="black"/><rect x="24" y="0" width="6" height="20" fill="black"/><rect x="34" y="0" width="4" height="20" fill="black"/><rect x="40" y="0" width="2" height="20" fill="black"/><rect x="46" y="0" width="10" height="20" fill="black"/><rect x="58" y="0" width="4" height="20" fill="black"/><rect x="64" y="0" width="2" height="20" fill="black"/><rect x="70" y="0" width="6" height="20" fill="black"/><rect x="80" y="0" width="4" height="20" fill="black"/><rect x="86" y="0" width="2" height="20" fill="black"/><rect x="90" y="0" width="6" height="20" fill="black"/><rect x="98" y="0" width="2" height="20" fill="black"/>
            </svg>
          </div>

          <!-- Зона фотографії: Кольорова, з правильним масштабом -->
          <!-- Використовуємо aspect-square для ідеального квадрата під фотографію -->
          <div class="relative w-full aspect-square border-b-4 border-black overflow-hidden flex-shrink-0 bg-white">
            <img 
              v-if="teacher.photo" 
              :src="teacher.photo.startsWith('http') ? teacher.photo : `https://mit-site-3t9h.vercel.app${teacher.photo}`" 
              :alt="teacher.last_name"
              class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500"
            />
            <div v-else class="w-full h-full flex items-center justify-center text-gray-500 font-pixel text-xs bg-gray-200">
              [ NO_PHOTO ]
            </div>

            <!-- Піксельна корона Завідувача -->
            <div v-if="teacher.position && teacher.position.toLowerCase().includes('завідувач')" class="absolute top-0 left-0 bg-yellow-400 border-r-4 border-b-4 border-black px-2 py-1 font-pixel text-[10px] flex items-center gap-1 z-10 shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
              <span>👑</span> <span class="font-bold text-black uppercase">HEAD_OF_DEPT</span>
            </div>
          </div>

          <!-- Інфо-блок -->
          <div class="p-5 flex-grow flex flex-col justify-between bg-white z-20">
            <div>
              <div class="font-pixel text-[9px] text-blue-600 mb-2 uppercase tracking-widest line-clamp-2 min-h-[24px]">
                {{ teacher.position }}
              </div>
              <h3 class="text-2xl font-black uppercase tracking-tight leading-[1.1]">
                {{ teacher.last_name }} <br> <span class="text-xl">{{ teacher.first_name }}</span>
              </h3>
            </div>
            
            <div class="flex items-center justify-between mt-6 pt-3 border-t-2 border-dashed border-gray-300 font-pixel text-[10px] uppercase text-gray-500 group-hover:text-blue-600 transition-colors">
              <span>[ OPEN_DOSSIER ]</span>
              <span class="group-hover:translate-x-2 transition-transform duration-300 text-lg leading-none">→</span>
            </div>
          </div>

        </div>

      </div>
    </div>

    <!-- МОДАЛЬНЕ ВІКНО ДОСЬЄ (CLASSIFIED) -->
    <div v-if="selectedTeacher" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/90 p-4 md:p-8 cursor-pointer backdrop-blur-md" @click="closeTeacherModal">
      <div class="relative max-w-4xl w-full bg-black border-4 border-blue-500 p-1 cursor-default max-h-[95vh] overflow-hidden flex flex-col shadow-[0_0_40px_rgba(59,130,246,0.3)]" @click.stop>
        
        <!-- Термінальна шапка модалки -->
        <div class="bg-blue-600 text-white border-b-4 border-blue-600 p-2 flex justify-between items-center font-pixel text-xs">
          <span>> DEPT_DATABASE/PERSONNEL_DOSSIER.exe</span>
          <button @click="closeTeacherModal" class="bg-black text-white px-3 hover:bg-white hover:text-black transition-colors cursor-pointer border border-transparent hover:border-black">
            [ X ]
          </button>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-12 bg-[#F4F4F0] p-6 md:p-8 gap-8 overflow-y-auto">
          
          <!-- Фото у модалці -->
          <div class="md:col-span-5 relative">
            <div class="border-4 border-black bg-white p-2 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
              <img 
                v-if="selectedTeacher.photo" 
                :src="selectedTeacher.photo.startsWith('http') ? selectedTeacher.photo : `https://mit-site-3t9h.vercel.app${selectedTeacher.photo}`" 
                class="w-full aspect-[3/4] object-cover object-top border-2 border-black" 
              />
              <div v-else class="w-full aspect-[3/4] bg-black text-green-400 font-pixel flex items-center justify-center text-xs">
                [ NO_PHOTO ]
              </div>
              
              <!-- Декоративний водяний знак ID -->
              <div class="absolute -bottom-2 -right-2 font-black text-6xl text-gray-300 opacity-50 font-pixel z-0 mix-blend-multiply pointer-events-none">
                {{ String(selectedTeacher.id).padStart(3, '0') }}
              </div>
            </div>
          </div>

          <!-- Повна інформація -->
          <div class="md:col-span-7 flex flex-col justify-start relative z-10">
            <div class="inline-block bg-black text-green-400 font-pixel text-[10px] px-3 py-1 mb-4 uppercase w-fit border border-green-400 shadow-[0_0_10px_rgba(74,222,128,0.2)]">
              ACCESS GRANTED
            </div>
            
            <h3 class="text-4xl md:text-6xl font-black uppercase mb-2 tracking-tighter leading-none">
              {{ selectedTeacher.last_name }} <br>{{ selectedTeacher.first_name }}
            </h3>
            
            <div class="flex flex-wrap items-center gap-2 mb-6 mt-2">
              <span class="border-2 border-black bg-blue-200 font-bold px-3 py-1 text-xs uppercase">{{ selectedTeacher.position }}</span>
              <span class="border-2 border-black bg-white font-bold px-3 py-1 text-xs uppercase">{{ selectedTeacher.degree || 'EXPERT' }}</span>
            </div>

            <!-- Блок біографії -->
            <div class="font-mono text-sm md:text-base text-gray-800 leading-relaxed whitespace-pre-line border-l-4 border-blue-600 pl-4 mb-8 bg-white p-4 border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
              <div class="font-pixel text-[10px] text-blue-600 mb-2">// BIOGRAPHY_DATA:</div>
              {{ selectedTeacher.bio }}
            </div>

            <!-- Кнопки контактів -->
            <div class="flex flex-wrap gap-4 font-pixel text-xs mt-auto pt-4 border-t-2 border-dashed border-gray-300">
              <a v-if="selectedTeacher.github" :href="selectedTeacher.github" target="_blank" class="border-2 border-black px-4 py-3 bg-black text-white hover:bg-white hover:text-black hover:-translate-y-1 transition-all shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
                > GITHUB ↗
              </a>
              <a v-if="selectedTeacher.linkedin" :href="selectedTeacher.linkedin" target="_blank" class="border-2 border-black px-4 py-3 bg-[#c7d2fe] text-black hover:bg-blue-600 hover:text-white hover:-translate-y-1 transition-all shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
                > LINKEDIN ↗
              </a>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';

const { data: teachers, pending, error } = await useFetch('https://mit-site-3t9h.vercel.app/api/v1/teachers/');

const teachersCount = computed(() => {
  return teachers.value ? teachers.value.length : 0;
});

const selectedTeacher = ref(null);

const openTeacherModal = (teacher) => {
  selectedTeacher.value = teacher;
  if (import.meta.client) { document.body.style.overflow = 'hidden'; }
};

const closeTeacherModal = () => {
  selectedTeacher.value = null;
  if (import.meta.client) { document.body.style.overflow = ''; }
};

const handleKeydown = (e) => {
  if (e.key === 'Escape' && selectedTeacher.value) {
    closeTeacherModal();
  }
};

onMounted(() => {
  if (import.meta.client) {
    window.addEventListener('keydown', handleKeydown);
  }
});

onUnmounted(() => {
  if (import.meta.client) {
    window.removeEventListener('keydown', handleKeydown);
  }
});
</script>
