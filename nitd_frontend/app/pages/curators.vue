<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-red-500 selection:text-white pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Хрестики) -->
    <div class="absolute inset-0 opacity-20 bg-[radial-gradient(#000_1px,transparent_1px)] bg-[size:24px_24px] pointer-events-none"></div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-16 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-red-600 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(220,38,38,1)]">[ MENTORSHIP_PROGRAM ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter">
            КУРАТОРИ <br><span class="text-white bg-black px-3 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">АКАДЕМГРУП</span>
          </h1>
        </div>
        
        <div class="flex flex-col gap-2">
          <NuxtLink to="/" class="font-pixel text-xs bg-white text-black px-6 py-3 uppercase border-4 border-black hover:bg-red-600 hover:text-white transition-colors shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] text-center">
            ← НА ГОЛОВНУ
          </NuxtLink>
        </div>
      </div>

      <!-- Статус завантаження -->
      <div v-if="pending" class="w-full border-4 border-dashed border-gray-400 py-32 flex flex-col items-center justify-center text-gray-500 bg-white mb-12">
        <div class="font-pixel text-3xl mb-4 animate-pulse text-red-600">[ LOADING_PERSONNEL_DATA... ]</div>
      </div>

      <!-- Помилка -->
      <div v-else-if="error" class="w-full border-4 border-black py-32 flex flex-col items-center justify-center text-red-500 bg-red-100 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] mb-12">
        <div class="font-pixel text-3xl mb-4">[ ACCESS_DENIED ]</div>
        <p class="font-bold text-xl text-black">Не вдалося завантажити список кураторів.</p>
      </div>

      <!-- СПИСОК КУРАТОРІВ -->
      <div v-else class="flex flex-col gap-20">
        
        <div v-if="dbCurators.length === 0" class="border-4 border-dashed border-gray-400 p-12 text-center bg-white">
          <span class="font-pixel text-gray-400 text-xl">[ DATABASE_EMPTY ]</span>
          <p class="font-mono text-gray-500 mt-2">Кураторів ще не призначено.</p>
        </div>

        <!-- Ітерація по рівнях освіти (Бакалаври / Магістри) -->
        <div v-for="(group, levelName) in groupedCurators" :key="levelName" class="flex flex-col gap-8">
          
          <!-- ЗАГОЛОВОК КАТЕГОРІЇ -->
          <div class="flex items-center gap-6">
            <h2 class="text-4xl md:text-5xl font-black uppercase tracking-tighter text-black">
              {{ levelName }}
            </h2>
            <div class="flex-grow h-2 bg-black"></div>
            <div class="font-pixel text-red-500 text-sm hidden md:block">/// {{ group.length }} ASSIGNED</div>
          </div>

          <!-- СІТКА КАРТОК (ПРАВИЛЬНІ ПРОПОРЦІЇ) -->
          <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-8">
            
            <div 
              v-for="curator in group" 
              :key="curator.id"
              class="relative bg-white border-4 border-black shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-2 hover:shadow-[12px_12px_0px_0px_rgba(220,38,38,1)] hover:border-red-600 transition-all duration-300 flex flex-col group cursor-crosshair"
            >
              <!-- ДЕКОРАТИВНИЙ ЕЛЕМЕНТ "БЕЙДЖИК" (Отвір для шнурка) -->
              <div class="absolute -top-5 left-1/2 -translate-x-1/2 w-12 h-6 bg-[#F4F4F0] border-4 border-black border-b-0 rounded-t-full flex items-center justify-center z-10">
                <div class="w-6 h-1.5 bg-black rounded-full"></div>
              </div>

              <!-- ШАПКА КАРТКИ -->
              <div class="bg-black text-white p-3 pt-5 flex justify-between items-center border-b-4 border-black group-hover:bg-red-600 transition-colors">
                <span class="font-pixel text-[8px] text-zinc-400 group-hover:text-white uppercase">ID: {{ String(curator.id).padStart(5, '0') }}</span>
                <span class="font-pixel text-[8px] text-green-400 uppercase animate-pulse">● ACTIVE</span>
              </div>

              <div class="flex flex-col flex-grow">
                
                <!-- НАЗВА ГРУПИ (Яскрава плашка) -->
                <div class="bg-[repeating-linear-gradient(45deg,transparent,transparent_10px,rgba(0,0,0,0.03)_10px,rgba(0,0,0,0.03)_20px)] border-b-4 border-black p-4 text-center">
                  <div class="font-pixel text-[10px] text-red-600 mb-1 uppercase">ASSIGNED GROUP</div>
                  <h3 class="text-3xl md:text-4xl font-black uppercase tracking-tighter text-black">
                    {{ curator.group_name || curator.course_name }}
                  </h3>
                </div>

                <!-- ФОТОГРАФІЯ (КОМПАКТНА ТА КОЛЬОРОВА) -->
                <div class="w-full flex justify-center py-6 bg-zinc-50 border-b-4 border-black relative overflow-hidden">
                  <div class="w-32 h-32 md:w-40 md:h-40 rounded-full border-4 border-black bg-zinc-200 overflow-hidden relative z-10 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] group-hover:shadow-[4px_4px_0px_0px_rgba(220,38,38,1)] transition-shadow">
                    <img 
                      v-if="curator.teacher_photo" 
                      :src="curator.teacher_photo" 
                      :alt="curator.teacher_name" 
                      class="w-full h-full object-cover group-hover:scale-110 transition-transform duration-500"
                    />
                    <div v-else class="w-full h-full flex flex-col items-center justify-center text-zinc-500">
                      <svg class="w-10 h-10 mb-1" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                      <span class="font-pixel text-[8px]">[ NO_IMG ]</span>
                    </div>
                  </div>
                  <!-- Фонова лінія за фотографією -->
                  <div class="absolute top-1/2 left-0 w-full h-1 bg-black -translate-y-1/2 z-0 opacity-20"></div>
                </div>

                <!-- ІНФОРМАЦІЯ ПРО ВИКЛАДАЧА -->
                <div class="p-4 flex-grow flex flex-col justify-center items-center text-center bg-white">
                  <h4 class="text-lg md:text-xl font-black uppercase leading-tight mb-2 group-hover:text-red-600 transition-colors">
                    {{ curator.teacher_name }}
                  </h4>
                  <div class="w-8 h-1 bg-black mb-3"></div>
                  <p class="font-mono text-[10px] text-gray-500 uppercase font-bold">
                    [ АКАДЕМІЧНИЙ КУРАТОР ]
                  </p>
                </div>

                <!-- НИЖНІЙ ШТРИХКОД -->
                <div class="h-8 border-t-4 border-black bg-zinc-100 flex items-center justify-center overflow-hidden">
                  <div class="font-pixel text-[16px] text-black tracking-widest scale-y-150 transform opacity-50 group-hover:opacity-100 transition-opacity">
                    ||||||||||||||||||||||||
                  </div>
                </div>

              </div>
            </div>

          </div>
        </div>

      </div>

    </div>
  </div>
</template>

<script setup>
import { computed } from 'vue';

const { data: dbCurators, pending, error } = await useFetch('http://127.0.0.1:8000/api/v1/curators/', {
  default: () => []
});

const groupedCurators = computed(() => {
  const groups = {
    'Бакалаврат': [],
    'Магістратура': []
  };

  dbCurators.value.forEach(curator => {
    if (curator.course.startsWith('c')) {
      groups['Бакалаврат'].push(curator);
    } else if (curator.course.startsWith('m')) {
      groups['Магістратура'].push(curator);
    }
  });

  if (groups['Бакалаврат'].length === 0) delete groups['Бакалаврат'];
  if (groups['Магістратура'].length === 0) delete groups['Магістратура'];

  return groups;
});
</script>

<style scoped>
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