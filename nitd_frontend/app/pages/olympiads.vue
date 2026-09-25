<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-purple-600 selection:text-white pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Шестикутники / Бджолині стільники) -->
    <div class="absolute inset-0 opacity-10 bg-[url('data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSI0OSIgdmlld0JveD0iMCAwIDI4IDQ5Ij48cGF0aCBkPSJNMzkgMjUuNUwzOSAzMi41TDE0IDQ3TDE0IDM5LjVMMzkgMjUuNVpNMCAyNS41TDAgMzIuNUwyNSA0N0wyNSAzOS41TDAgMjUuNVoiIGZpbGw9IiMwMDAiIGZpbGwtcnVsZT0iZXZlbm9kZCIvPjwvc3ZnPg==')] pointer-events-none"></div>

    <div class="max-w-[1200px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-16 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-purple-600 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(168,85,247,1)]">[ COMPETITIVE_ARENA ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter">
            СТУДЕНТСЬКІ <br><span class="text-white bg-black px-3 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">ОЛІМПІАДИ</span>
          </h1>
        </div>
        
      </div>

      <!-- Статус завантаження -->
      <div v-if="pending" class="w-full border-4 border-dashed border-gray-400 py-32 flex flex-col items-center justify-center text-gray-500 bg-white mb-12">
        <div class="font-pixel text-3xl mb-4 animate-pulse text-purple-600">[ SCANNING_FOR_MISSIONS... ]</div>
      </div>

      <!-- Помилка -->
      <div v-else-if="error" class="w-full border-4 border-black py-32 flex flex-col items-center justify-center text-red-500 bg-red-100 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] mb-12">
        <div class="font-pixel text-3xl mb-4">[ CONNECTION_FAILED ]</div>
        <p class="font-bold text-xl text-black">Не вдалося завантажити список змагань.</p>
      </div>

      <!-- СПИСОК ОЛІМПІАД (МІСІЇ / ЧЕЛЕНДЖІ) -->
      <div v-else class="flex flex-col gap-16">
        
        <div v-if="dbOlympiads.length === 0" class="border-4 border-dashed border-gray-400 p-12 text-center bg-white">
          <span class="font-pixel text-gray-400 text-xl">[ NO_ACTIVE_BOUNTIES ]</span>
          <p class="font-mono text-gray-500 mt-2">Наразі немає відкритих реєстрацій на олімпіади.</p>
        </div>

        <div 
          v-for="(olympiad, index) in dbOlympiads" 
          :key="olympiad.id"
          class="flex flex-col border-4 border-black bg-white shadow-[16px_16px_0px_0px_rgba(168,85,247,1)] hover:-translate-y-2 hover:translate-x-2 hover:shadow-[4px_4px_0px_0px_rgba(168,85,247,1)] transition-all duration-300 relative group"
        >
          <!-- HEADER ТЕРМІНАЛУ -->
          <div class="bg-black text-purple-400 font-pixel text-[10px] p-2 flex justify-between border-b-4 border-black">
            <span>root@mit_arena:~/challenges/mission_{{ String(olympiad.id).padStart(3, '0') }}$</span>
            <span class="animate-pulse">_</span>
          </div>

          <!-- ТІЛО КАРТКИ -->
          <div class="flex flex-col md:flex-row h-full">
            
            <!-- ДАТА (ВЕРТИКАЛЬНА ПАНЕЛЬ) -->
            <div class="bg-purple-600 text-white p-4 md:w-24 shrink-0 flex flex-row md:flex-col justify-center items-center border-b-4 md:border-b-0 md:border-r-4 border-black gap-2">
              <div class="font-pixel text-[8px] uppercase tracking-widest opacity-80 -rotate-90 hidden md:block mb-8">
                [ DEADLINE ]
              </div>
              <div class="text-4xl md:text-5xl font-black font-pixel text-yellow-400">
                {{ formatDay(olympiad.date_held) }}
              </div>
              <div class="text-sm font-bold uppercase tracking-widest text-center">
                {{ formatMonth(olympiad.date_held) }}<br class="hidden md:block">
                {{ formatYear(olympiad.date_held) }}
              </div>
            </div>

            <!-- ІНФОРМАЦІЯ -->
            <div class="p-6 md:p-8 flex-grow flex flex-col justify-between">
              <div>
                <h2 class="text-2xl md:text-4xl font-black uppercase tracking-tight leading-none mb-4 group-hover:text-purple-600 transition-colors">
                  {{ olympiad.title }}
                </h2>
                <div class="w-16 h-2 bg-black mb-6 group-hover:w-32 transition-all duration-500"></div>
                <p class="text-gray-700 text-sm md:text-lg font-bold whitespace-pre-line line-clamp-4 leading-relaxed">
                  {{ olympiad.content }}
                </p>
              </div>
              
              <!-- Кнопка -->
              <div class="mt-8">
                <a v-if="olympiad.link" :href="olympiad.link" target="_blank" class="inline-block bg-black text-white font-pixel text-xs px-6 py-4 uppercase border-4 border-black hover:bg-purple-600 hover:text-white transition-colors shadow-[6px_6px_0px_0px_rgba(0,0,0,0.3)] active:translate-y-1 active:translate-x-1 active:shadow-none">
                  > ПРИЙНЯТИ ВИКЛИК
                </a>
                <div v-else class="inline-block bg-gray-200 text-gray-500 font-pixel text-xs px-6 py-4 uppercase border-4 border-gray-400 cursor-not-allowed">
                  [ РЕЄСТРАЦІЮ ЗАКРИТО ]
                </div>
              </div>
            </div>

            <!-- ФОТО (INTEL) -->
            <div v-if="olympiad.photo" class="md:w-2/5 min-h-[250px] border-t-4 md:border-t-0 md:border-l-4 border-black shrink-0 relative overflow-hidden bg-black p-4 flex flex-col">
              <!-- Рамка як у видошукачі -->
              <div class="absolute inset-2 border-2 border-dashed border-white/20 pointer-events-none z-20"></div>
              
              <div class="w-full bg-zinc-900 text-green-400 font-pixel text-[8px] p-1 mb-2 border border-zinc-700 flex justify-between uppercase z-20 relative">
                <span>[ ATTACHED_INTEL ]</span>
                <span class="group-hover:text-red-500 transition-colors">{{ olympiad.photo ? 'IMG_FOUND' : 'NULL' }}</span>
              </div>
              
              <div class="relative flex-grow border-2 border-zinc-800 overflow-hidden group/img">
                <!-- Глітч-фото (Кольори інвертуються в кібер-стилі) -->
                <img 
                  :src="olympiad.photo" 
                  :alt="olympiad.title"
                  class="w-full h-full object-cover filter sepia hue-rotate-[-50deg] saturate-200 contrast-125 brightness-75 group-hover:filter-none group-hover:scale-110 transition-all duration-500"
                />
                <!-- Перехрестя (Target) при наведенні -->
                <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none z-20">
                  <svg class="w-16 h-16 text-red-500 animate-spin-slow" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1" d="M12 4v2m0 12v2m8-8h-2M6 12H4m12 0a6 6 0 11-12 0 6 6 0 0112 0z"></path></svg>
                </div>
                <!-- Сітка -->
                <div class="absolute inset-0 bg-[linear-gradient(rgba(0,0,0,0)_50%,rgba(0,0,0,0.4)_50%)] bg-[length:100%_4px] pointer-events-none z-10"></div>
              </div>
            </div>

          </div>
        </div>

      </div>

    </div>
  </div>
</template>

<script setup>
// Отримуємо дані з нашого нового ендпоінту Олімпіад
const { data: dbOlympiads, pending, error } = await useFetch('http://127.0.0.1:8000/api/v1/olympiads/', {
  default: () => []
});

// Форматування дат
const formatDay = (dateString) => {
  if (!dateString) return 'XX';
  return new Date(dateString).getDate().toString().padStart(2, '0');
};

const formatMonth = (dateString) => {
  if (!dateString) return 'XXX';
  return new Date(dateString).toLocaleDateString('uk-UA', { month: 'short' }).replace('.', '');
};

const formatYear = (dateString) => {
  if (!dateString) return 'XXXX';
  return new Date(dateString).getFullYear();
};
</script>

<style scoped>
/* Плавний перехід між сторінками */
.page-enter-active,
.page-leave-active {
  transition: opacity 0.3s ease, filter 0.3s ease;
}

.page-enter-from,
.page-leave-to {
  opacity: 0;
  filter: blur(10px) grayscale(100%);
}

.animate-spin-slow {
  animation: spin 8s linear infinite;
}
</style>