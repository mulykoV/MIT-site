<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-blue-600 selection:text-white pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Точки) -->
    <div class="absolute inset-0 opacity-20 bg-[radial-gradient(#000_1px,transparent_1px)] bg-[size:20px_20px] pointer-events-none"></div>

    <!-- Біжуча стрічка (Жовта стрічка) -->
    <div class="absolute top-20 left-0 w-full bg-yellow-400 border-y-4 border-black py-2 z-20 overflow-hidden transform -rotate-1 origin-left shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
      <div class="whitespace-nowrap font-pixel text-xl animate-marquee uppercase tracking-widest text-black font-bold">
        * RESEARCH & DEVELOPMENT * TOP SECRET * DO NOT DISTRIBUTE * CLASSIFIED * RESEARCH & DEVELOPMENT * TOP SECRET * DO NOT DISTRIBUTE *
      </div>
    </div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10 mt-12">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-16 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-blue-600 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(37,99,235,1)]">[ R&D_DEPARTMENT ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter">
            НАПРЯМКИ <br><span class="text-white bg-black px-3 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(220,38,38,1)]">НАУКОВОЇ ДІЯЛЬНОСТІ</span>
          </h1>
        </div>
      
      </div>

      <!-- СІТКА ПРОЄКТІВ -->
      <div class="grid grid-cols-1 gap-20">
        
        <!-- ==========================================
             ПРОЄКТ 1: СТІЙКІСТЬ (SERVER RACK SIMULATOR)
             ========================================== -->
        <div class="border-4 border-black bg-white shadow-[16px_16px_0px_0px_rgba(0,0,0,1)] transition-all grid grid-cols-1 lg:grid-cols-12 relative group" :class="simulating[0] ? 'border-red-500' : ''">
          
          <div class="absolute -top-5 -left-5 bg-red-500 text-white font-pixel text-sm px-4 py-2 uppercase border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] rotate-[-3deg] z-20" :class="simulating[0] ? 'animate-bounce' : ''">
            {{ simulating[0] ? 'CRITICAL_LOAD_TEST' : 'STABILITY_SYS' }}
          </div>
          
          <div class="lg:col-span-7 flex flex-col justify-center p-8 lg:p-12">
            <h2 class="text-3xl md:text-4xl font-black uppercase tracking-tight text-black font-pixel mb-6">
              Функціональна стійкість
            </h2>
            <p class="text-gray-700 text-lg leading-relaxed font-mono font-bold mb-8">
              Математичне та програмне забезпечення, яке дозволяє в умовах зовнішніх та внутрішніх негативних впливів (відмов, пошкоджень, помилок) забезпечити функціонування телекомунікаційних систем за рахунок виявлення та перерозподілу надмірності.
            </p>
            <button @click="triggerSimulation(0)" :disabled="simulating[0]" class="w-fit font-pixel border-4 border-black px-6 py-4 uppercase shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] transition-all flex items-center gap-3" :class="simulating[0] ? 'bg-zinc-300 text-gray-500 cursor-not-allowed shadow-none translate-y-[6px] translate-x-[6px]' : 'bg-red-500 text-white hover:bg-red-600 active:translate-y-[6px] active:translate-x-[6px] active:shadow-none'">
              <span class="w-3 h-3 rounded-full border-2 border-black" :class="simulating[0] ? 'bg-red-500 animate-pulse' : 'bg-white'"></span>
              {{ simulating[0] ? 'ВИКОНАННЯ...' : 'INITIATE_DDOS_TEST' }}
            </button>
          </div>

          <!-- ІНТЕРАКТИВНИЙ ВІДЖЕТ 1: SERVER LOGS & ROUTING -->
          <div class="lg:col-span-5 bg-black border-l-4 border-black p-4 flex flex-col relative overflow-hidden h-64 lg:h-auto">
            <div class="absolute inset-0 opacity-20 bg-[linear-gradient(transparent_50%,rgba(0,0,0,1)_50%)] bg-[size:100%_4px] z-10 pointer-events-none"></div>
            
            <div class="flex justify-between items-center border-b-2 border-zinc-800 pb-2 mb-2">
              <span class="text-red-500 font-pixel text-[10px]">TERMINAL_TTY1</span>
              <span class="text-white font-mono text-xs bg-red-600 px-1" v-if="simulating[0]">WARNING: ATTACK DETECTED</span>
            </div>

            <!-- Fake Logs -->
            <div class="flex-1 overflow-hidden flex flex-col justify-end">
              <div v-for="(log, idx) in logs" :key="idx" class="text-[10px] font-mono leading-tight mb-1" :class="log.includes('ERR') ? 'text-red-500 font-bold' : 'text-green-500'">
                > {{ log }}
              </div>
            </div>

            <!-- Server Node grid -->
            <div class="grid grid-cols-6 gap-1 mt-4">
              <div v-for="i in 18" :key="i" class="h-3 border border-zinc-800" :class="getServerColor(i, 0)"></div>
            </div>
          </div>
        </div>

        <!-- ==========================================
             ПРОЄКТ 2: СЕНСОРНА СИСТЕМА (RADAR)
             ========================================== -->
        <div class="border-4 border-black bg-white shadow-[16px_16px_0px_0px_rgba(0,0,0,1)] transition-all grid grid-cols-1 lg:grid-cols-12 relative group">
          
          <div class="absolute -top-5 -right-5 bg-green-500 text-black font-pixel text-sm px-4 py-2 uppercase border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] rotate-[3deg] z-20">
            QS_RADAR_ACTIVE
          </div>
          
          <!-- ІНТЕРАКТИВНИЙ ВІДЖЕТ 2: RADAR CSS ART -->
          <div class="lg:col-span-5 bg-[#0a1910] border-r-4 border-black flex flex-col items-center justify-center relative overflow-hidden h-80 lg:h-auto">
            <!-- Radar Base -->
            <div class="relative w-48 h-48 rounded-full border-2 border-green-500/50 flex items-center justify-center">
              <div class="absolute w-32 h-32 rounded-full border border-green-500/30"></div>
              <div class="absolute w-16 h-16 rounded-full border border-green-500/20"></div>
              <div class="absolute w-full h-[1px] bg-green-500/30"></div>
              <div class="absolute h-full w-[1px] bg-green-500/30"></div>
              
              <!-- Radar Scanner Sweep -->
              <div class="absolute w-full h-full rounded-full" 
                   :class="simulating[1] ? 'animate-spin-fast' : 'animate-spin-slow'"
                   style="background: conic-gradient(from 0deg, transparent 70%, rgba(34, 197, 94, 0.4) 100%);">
              </div>

              <!-- Targets (З'являються під час симуляції) -->
              <div v-if="simulating[1]" class="absolute w-2 h-2 bg-red-500 rounded-full animate-ping top-10 left-12"></div>
              <div v-if="simulating[1]" class="absolute w-2 h-2 bg-red-500 rounded-full animate-ping bottom-14 right-10" style="animation-delay: 0.5s"></div>
            </div>

            <!-- Radar HUD text -->
            <div class="absolute bottom-4 left-4 text-green-500 font-pixel text-[8px] flex flex-col">
              <span>LAT: 50.4016, LON: 30.4700</span>
              <span v-if="simulating[1]" class="text-red-500 mt-1 bg-black px-1">> MINES DETECTED: 2</span>
              <span v-else>> SCANNING SECTOR...</span>
            </div>
          </div>

          <div class="lg:col-span-7 flex flex-col justify-center p-8 lg:p-12">
            <h2 class="text-3xl md:text-4xl font-black uppercase tracking-tight text-black font-pixel mb-6">
              Сенсорна система СП
            </h2>
            <p class="text-gray-700 text-lg leading-relaxed font-mono font-bold mb-8">
              Створення роботизованої системи моніторингу та розмінування (QS-система). Використання нових принципів дозволить забезпечити функціональну стійкість та виконати завдання оперативного забезпечення стосовно розвідки та розмінування.
            </p>
            <button @click="triggerSimulation(1)" :disabled="simulating[1]" class="w-fit font-pixel border-4 border-black px-6 py-4 uppercase shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] transition-all flex items-center gap-3" :class="simulating[1] ? 'bg-zinc-300 text-gray-500 cursor-not-allowed shadow-none translate-y-[6px] translate-x-[6px]' : 'bg-green-500 text-black hover:bg-green-400 active:translate-y-[6px] active:translate-x-[6px] active:shadow-none'">
              <svg v-if="!simulating[1]" class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M12 8v4l3 3"></path></svg>
              <span v-else class="w-4 h-4 border-2 border-black border-t-transparent rounded-full animate-spin"></span>
              {{ simulating[1] ? 'SCANNING TERRAIN...' : 'RUN_SECTOR_SCAN' }}
            </button>
          </div>
        </div>

        <!-- ==========================================
             ПРОЄКТ 3: OSI LAYERS (STACK VISUALIZER)
             ========================================== -->
        <div class="border-4 border-black bg-white shadow-[16px_16px_0px_0px_rgba(0,0,0,1)] transition-all grid grid-cols-1 lg:grid-cols-12 relative group">
          
          <div class="absolute -top-5 -left-5 bg-blue-600 text-white font-pixel text-sm px-4 py-2 uppercase border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] rotate-[-3deg] z-20">
            OSI_PROTOCOLS
          </div>
          
          <div class="lg:col-span-7 flex flex-col justify-center p-8 lg:p-12">
            <h2 class="text-3xl md:text-4xl font-black uppercase tracking-tight text-black font-pixel mb-6">
              OSI-міжрівнева узгодженість
            </h2>
            <p class="text-gray-700 text-lg leading-relaxed font-mono font-bold mb-8">
              Моделі та методи забезпечення узгодженості між рівнями моделі OSI для досягнення максимальної ефективності передачі даних у гетерогенних мережах нового покоління.
            </p>
            <button @click="triggerSimulation(2)" :disabled="simulating[2]" class="w-fit font-pixel border-4 border-black px-6 py-4 uppercase shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] transition-all flex items-center gap-3" :class="simulating[2] ? 'bg-zinc-300 text-gray-500 cursor-not-allowed shadow-none translate-y-[6px] translate-x-[6px]' : 'bg-blue-600 text-white hover:bg-blue-700 active:translate-y-[6px] active:translate-x-[6px] active:shadow-none'">
              <div class="flex gap-1">
                <div class="w-2 h-4 bg-white" :class="simulating[2] ? 'animate-pulse' : ''"></div>
                <div class="w-2 h-4 bg-white" :class="simulating[2] ? 'animate-pulse delay-75' : ''"></div>
                <div class="w-2 h-4 bg-white" :class="simulating[2] ? 'animate-pulse delay-150' : ''"></div>
              </div>
              {{ simulating[2] ? 'TRANSMITTING PACKETS...' : 'SEND_DATA_PACKET' }}
            </button>
          </div>

          <!-- ІНТЕРАКТИВНИЙ ВІДЖЕТ 3: 7 OSI LAYERS -->
          <div class="lg:col-span-5 bg-[#050b14] border-l-4 border-black p-8 flex flex-col justify-end gap-2 relative h-80 lg:h-auto">
            
            <!-- Анімований пакет даних, що летить через шари -->
            <div v-if="simulating[2]" class="absolute left-[15%] w-2 h-4 bg-yellow-400 shadow-[0_0_10px_rgba(250,204,21,1)] z-10 animate-packet-drop"></div>

            <div v-for="(layer, index) in osiLayers" :key="index" class="w-full flex items-center gap-4 group/layer transition-all" :class="simulating[2] ? 'hover:translate-x-2' : ''">
              <div class="font-pixel text-[8px] text-blue-400 w-16 text-right">L-{{ 7 - index }}</div>
              <div class="flex-1 h-6 border-2 flex items-center px-2 transition-colors" 
                   :class="simulating[2] ? 'border-blue-500 bg-blue-900/40 animate-pulse' : 'border-blue-900 bg-transparent'"
                   :style="simulating[2] ? `animation-delay: ${index * 100}ms` : ''">
                <span class="font-mono text-[10px] text-blue-200">{{ layer }}</span>
              </div>
            </div>
          </div>
        </div>

      </div>

    </div>
  </div>
</template>

<style scoped>
@keyframes marquee {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-50%); }
}
.animate-marquee {
  display: inline-block;
  animation: marquee 20s linear infinite;
  min-width: 200%;
}

.animate-spin-slow {
  animation: spin 4s linear infinite;
}
.animate-spin-fast {
  animation: spin 0.5s linear infinite;
}

@keyframes packet-drop {
  0% { top: 10%; opacity: 0; }
  10% { opacity: 1; }
  90% { opacity: 1; }
  100% { top: 90%; opacity: 0; }
}
.animate-packet-drop {
  animation: packet-drop 1.5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
}
</style>

<script setup>
import { ref } from 'vue';

// Стан симуляцій для 3-х проєктів
const simulating = ref([false, false, false]);

// --- ЛОГІКА ДЛЯ ПРОЄКТУ 1 (ТЕРМІНАЛ) ---
const logs = ref([
  'SYSTEM_BOOT... OK',
  'MODULE_STABILITY... LOADED',
  'AWAITING INPUT...'
]);

const fakeErrorLogs = [
  'ERR: NODE_12 UNRESPONSIVE',
  'ERR: TRAFFIC SPIKE 400%',
  'REROUTING TRAFFIC -> NODE_04',
  'LOAD BALANCER: ACTIVE',
  'ERR: CONNECTION DROPPED',
  'RECOVERING... OK',
  'STABILITY METRIC: 99.9%'
];

let logInterval;

const triggerLogSimulation = () => {
  logs.value = ['INITIATING STRESS TEST...'];
  let count = 0;
  
  logInterval = setInterval(() => {
    // Тримаємо тільки останні 6 логів, щоб не переповнювати екран
    if (logs.value.length > 5) logs.value.shift();
    
    // Беремо випадковий лог
    const randomLog = fakeErrorLogs[Math.floor(Math.random() * fakeErrorLogs.length)];
    
    // Генеруємо фейковий хеш для реалістичності
    const hash = Math.random().toString(36).substring(2, 8).toUpperCase();
    logs.value.push(`[${hash}] ${randomLog}`);
    
    count++;
    if (count > 20) clearInterval(logInterval); // Зупиняємо через ~2 секунди
  }, 100);
};

// Блимання вузлів на сервері
const getServerColor = (i, projectIndex) => {
  if (!simulating.value[projectIndex]) return 'bg-green-900'; // Спокійний стан
  
  // Рандомно блимають червоним, жовтим і зеленим під час симуляції
  const r = Math.random();
  if (r > 0.8) return 'bg-red-500';
  if (r > 0.6) return 'bg-yellow-400';
  return 'bg-green-500';
};

// --- ДАНІ ДЛЯ ПРОЄКТУ 3 (OSI) ---
const osiLayers = [
  'APPLICATION',
  'PRESENTATION',
  'SESSION',
  'TRANSPORT',
  'NETWORK',
  'DATA_LINK',
  'PHYSICAL'
];

// --- ГЛОБАЛЬНА ФУНКЦІЯ ЗАПУСКУ ---
const triggerSimulation = (index) => {
  simulating.value[index] = true;
  
  if (index === 0) {
    triggerLogSimulation();
  }

  // Симуляція триває 3 секунди, потім кнопка "відтискається"
  setTimeout(() => {
    simulating.value[index] = false;
    if (index === 0) {
      clearInterval(logInterval);
      logs.value.push('TEST COMPLETE. SYS NORMAL.');
    }
  }, 3000);
};
</script>