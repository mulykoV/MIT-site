<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-blue-600 selection:text-white pb-32 pt-32 lg:pt-40">
    
    <!-- HEADER -->
    <div class="px-6 max-w-[1400px] mx-auto border-b-4 border-black pb-8 mb-12">
      <div class="flex flex-col md:flex-row justify-between items-end gap-8 relative z-10">
        <div class="max-w-4xl">
          <div class="font-pixel text-blue-600 text-xl mb-4 uppercase tracking-widest">[ TIMETABLE_SYNC ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter leading-[0.9] mb-4">
            РОЗКЛАД <br><span class="text-white bg-black px-3 mt-2 inline-block">ЗАНЯТЬ</span>
          </h1>
          <p class="text-xl font-bold text-gray-800 border-l-4 border-black pl-4">
            Синхронізація з навчальним процесом. Система автоматично відслідковує поточний час (за Києвом) та підсвічує активні лекції.
          </p>
        </div>
        
        <!-- Live Clock (Kyiv Time) -->
        <div class="bg-black text-green-400 border-4 border-black p-4 shadow-[8px_8px_0px_0px_rgba(59,130,246,1)] font-pixel text-center w-full md:w-auto">
          <div class="text-xs text-gray-500 mb-1">// KYIV_TIME</div>
          <div class="text-3xl animate-pulse">{{ currentTimeFormatted }}</div>
        </div>
      </div>
    </div>

    <!-- MAIN DASHBOARD -->
    <div class="max-w-[1400px] mx-auto px-6">
      
      <!-- Фільтр курсів (Tabs) -->
      <div class="flex flex-wrap gap-4 mb-12 border-b-4 border-black pb-6">
        <button 
          v-for="course in courses" 
          :key="course.id"
          @click="activeCourse = course.id"
          class="font-pixel text-sm md:text-base uppercase px-6 py-3 border-4 border-black transition-all shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] cursor-crosshair"
          :class="activeCourse === course.id ? 'bg-blue-600 text-white translate-x-1 translate-y-1 shadow-none' : 'bg-white hover:bg-gray-200 text-black'"
        >
          [ {{ course.name }} ]
        </button>
      </div>

      <!-- Статус завантаження з API -->
      <div v-if="pending" class="w-full border-4 border-dashed border-gray-400 py-32 flex flex-col items-center justify-center text-gray-500 bg-white mb-12">
        <div class="font-pixel text-3xl mb-4 animate-pulse">[ SYNCING_TIMETABLE... ]</div>
      </div>

      <!-- Помилка підключення до API -->
      <div v-else-if="error" class="w-full border-4 border-black py-32 flex flex-col items-center justify-center text-red-500 bg-red-100 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] mb-12">
        <div class="font-pixel text-3xl mb-4">[ CONNECTION_FAILED ]</div>
        <p class="font-bold text-xl text-black">Не вдалося завантажити розклад з сервера.</p>
      </div>

      <!-- Основний контент (якщо дані завантажено) -->
      <div v-else class="flex flex-col gap-12">
        
        <!-- ІНДИКАТОР СТАТУСУ РОЗКЛАДУ (Винесено сюди, ОДИН РАЗ на сторінку) -->
        <div v-if="Object.keys(filteredSchedule).length > 0">
          <div v-if="currentScheduleStatus !== 'permanent'" class="border-4 border-black bg-yellow-400 p-4 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] flex items-center gap-4 animate-pulse-slow">
            <div class="bg-black text-yellow-400 font-pixel text-xl px-3 py-2 flex items-center justify-center">
              !
            </div>
            <div>
              <h3 class="font-black uppercase text-xl tracking-tight leading-none mb-1">
                Увага: Тимчасовий розклад
              </h3>
              <p class="font-mono text-sm font-bold text-gray-800">
                Зараз відображається розклад на: <span class="uppercase text-black underline">[{{ currentScheduleStatus === 'week_1' ? 'Перший тиждень' : 'Другий тиждень' }}]</span>. Після затвердження він буде автоматично оновлений системою.
              </p>
            </div>
          </div>
          
          <div v-else class="border-4 border-black bg-green-400 p-4 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] flex items-center gap-4">
            <div class="bg-black text-green-400 font-pixel text-xl px-2 py-2 flex items-center justify-center">
              OK
            </div>
            <div>
              <h3 class="font-black uppercase text-xl tracking-tight leading-none mb-1">
                Постійний розклад
              </h3>
              <p class="font-mono text-sm font-bold text-gray-800">
                Система використовує затверджений стабільний розклад на семестр.
              </p>
            </div>
          </div>
        </div>

        <!-- Якщо пар для курсу ще не додано в базу -->
        <div v-if="Object.keys(filteredSchedule).length === 0" class="border-4 border-dashed border-gray-400 p-12 flex flex-col items-center justify-center bg-white text-center">
          <span class="font-pixel text-gray-400 text-xl mb-2">[ NO_PROCESSES_SCHEDULED ]</span>
          <p class="font-mono text-gray-500">Пар для цього курсу ще не додано. Перевірте панель адміністратора Django.</p>
        </div>

        <!-- Розклад по днях -->
        <div v-else class="flex flex-col gap-16">
          
          <div v-for="(daySchedule, dayName) in filteredSchedule" :key="dayName" class="relative">
            
            <!-- Назва дня -->
            <div class="sticky top-20 z-30 bg-[#F4F4F0] py-2 mb-6">
              <h2 class="font-pixel text-3xl md:text-4xl font-black uppercase tracking-widest text-black border-l-8 border-blue-600 pl-4">
                {{ dayName }}
              </h2>
            </div>

            <!-- Сітка пар -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
              
              <div 
                v-for="lesson in daySchedule" 
                :key="lesson.id"
                class="border-4 border-black bg-white p-6 relative transition-all"
                :class="isLive(lesson.timeStart, lesson.timeEnd) ? 'shadow-[8px_8px_0px_0px_rgba(74,222,128,1)] bg-green-50 scale-[1.02] border-green-500 z-10' : 'shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-1'"
              >
                <!-- Індикатор LIVE -->
                <div v-if="isLive(lesson.timeStart, lesson.timeEnd)" class="absolute -top-4 -right-4 bg-green-500 text-black border-4 border-black font-pixel text-xs px-3 py-1 uppercase shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] animate-bounce z-20">
                  ● LIVE_NOW
                </div>

                <!-- Тип пари -->
                <div class="absolute top-0 left-0 bg-black text-white font-pixel text-[10px] px-2 py-1 uppercase border-r-4 border-b-4 border-black">
                  {{ lesson.type }}
                </div>

                <!-- БЕЙДЖ ПІДГРУПИ -->
                <div v-if="lesson.subgroup && lesson.subgroup !== 'Загальна'" class="absolute top-0 right-0 bg-blue-600 text-white font-pixel text-[10px] px-2 py-1 uppercase border-l-4 border-b-4 border-black">
                  {{ lesson.subgroup }}
                </div>

                <div class="flex flex-col md:flex-row justify-between gap-6 pt-4">
                  
                  <!-- Час та Аудиторія -->
                  <div class="flex flex-col gap-2 min-w-[120px]">
                    <div class="font-pixel text-xl md:text-2xl text-blue-600">
                      {{ lesson.timeStart }} <br>
                      <span class="text-gray-400 text-sm">{{ lesson.timeEnd }}</span>
                    </div>
                    <div class="font-mono text-xs font-bold bg-gray-200 px-2 py-1 mt-auto w-fit uppercase border border-gray-400">
                      Ауд: {{ lesson.room }}
                    </div>
                  </div>

                  <!-- Інформація про предмет -->
                  <div class="flex-grow flex flex-col justify-between">
                    <div>
                      <h3 class="text-2xl font-black uppercase tracking-tight leading-none mb-2">
                        {{ lesson.subject }}
                      </h3>
                      <p class="font-mono text-sm text-gray-600 mb-4">
                        Викладач: <span class="font-bold text-black">{{ lesson.teacher }}</span>
                      </p>
                    </div>
                    
                    <div class="flex justify-end">
                      <a v-if="lesson.link" :href="lesson.link" target="_blank" class="font-pixel text-[10px] bg-blue-600 text-white px-3 py-2 uppercase hover:bg-black transition-colors shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
                        JOIN_MEETING ↗
                      </a>
                    </div>
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
import { ref, computed, onMounted, onUnmounted } from 'vue';

// 1. ГОДИННИК ТА ЛОГІКА "LIVE" (ЖОРСТКА ПРИВ'ЯЗКА ДО КИЄВА)
const currentTime = ref(new Date());
let timerInterval = null;

onMounted(() => {
  timerInterval = setInterval(() => {
    currentTime.value = new Date();
  }, 1000);
});

onUnmounted(() => {
  clearInterval(timerInterval);
});

// Форматуємо час на екрані суто за Києвом
const currentTimeFormatted = computed(() => {
  return currentTime.value.toLocaleTimeString('uk-UA', { 
    timeZone: 'Europe/Kyiv', 
    hour: '2-digit', 
    minute: '2-digit', 
    second: '2-digit' 
  });
});

const isLive = (startStr, endStr) => {
  if (!startStr || !endStr) return false;
  
  // Отримуємо години і хвилини саме Київського часу
  const kyivTimeStr = currentTime.value.toLocaleString('en-US', { timeZone: 'Europe/Kyiv' });
  const kyivDateObj = new Date(kyivTimeStr);
  
  const currentMinutes = kyivDateObj.getHours() * 60 + kyivDateObj.getMinutes();

  const [startH, startM] = startStr.split(':').map(Number);
  const [endH, endM] = endStr.split(':').map(Number);
  
  const startMinutes = startH * 60 + startM;
  const endMinutes = endH * 60 + endM;

  return currentMinutes >= startMinutes && currentMinutes <= endMinutes;
};

// 2. ДАНІ ДЛЯ ФІЛЬТРАЦІЇ
const courses = [
  { id: 'c1', name: '1 Курс' },
  { id: 'c2', name: '2 Курс' },
  { id: 'c3', name: '3 Курс' },
  { id: 'c4', name: '4 Курс' },
  { id: 'm1', name: 'Магістратура 1' },
  { id: 'm2', name: 'Магістратура 2' }
];

const activeCourse = ref('c3');

// 3. ПІДКЛЮЧЕННЯ ДО DJANGO API
const { data: dbSchedule, pending, error } = await useFetch('https://mit-site-3t9h.vercel.app/api/v1/schedule/', {
  default: () => []
});

// 4. СОРТУВАННЯ ТА ГРУПУВАННЯ РОЗКЛАДУ
const filteredSchedule = computed(() => {
  if (!dbSchedule.value) return {};

  const filtered = dbSchedule.value.filter(lesson => lesson.course_id === activeCourse.value);
  
  const daysOrder = ['Понеділок', 'Вівторок', 'Середа', 'Четвер', "П'ятниця", 'Субота'];
  
  const grouped = {};
  daysOrder.forEach(day => {
    const lessonsForDay = filtered.filter(l => l.day === day).sort((a, b) => a.timeStart.localeCompare(b.timeStart));
    if (lessonsForDay.length > 0) {
      grouped[day] = lessonsForDay;
    }
  });
  
  return grouped;
});

// Визначаємо поточний статус розкладу для обраного курсу
const currentScheduleStatus = computed(() => {
  if (!dbSchedule.value) return 'permanent';
  const courseLessons = dbSchedule.value.filter(lesson => lesson.course_id === activeCourse.value);
  if (courseLessons.length > 0) {
    return courseLessons[0].status; // Беремо статус з першої пари (він однаковий для всього курсу)
  }
  return 'permanent';
});
</script>
