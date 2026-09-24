<template>
  <!-- Збільшили верхній відступ pt-40 для уникнення конфліктів з глобальним Navbar -->
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-blue-600 selection:text-white pb-32 pt-40 lg:pt-48">
    
    <!-- HEADER -->
    <div class="px-6 max-w-[1400px] mx-auto border-b-4 border-black pb-12 mb-12">
      <div class="flex flex-col md:flex-row justify-between items-end gap-8 relative z-10">
        <div class="max-w-3xl">
          <div class="font-pixel text-red-500 text-xl mb-4 uppercase tracking-widest">[ COMMUNICATION_PROTOCOLS ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter leading-[0.9] mb-4">
            ВСТАНОВИТИ <br><span class="text-white bg-blue-600 px-3 mt-2 inline-block">ЗВ'ЯЗОК</span>
          </h1>
          <p class="text-xl font-bold text-gray-800 border-l-4 border-black pl-4">
            Виберіть кінцеву точку (endpoint) для отримання контактних даних.
          </p>
        </div>
        
        <div class="bg-black text-green-400 border-4 border-black p-4 shadow-[8px_8px_0px_0px_rgba(239,68,68,1)] font-pixel text-xs text-center w-full md:w-auto">
          > SERVER_PING: {{ pingLatency }}ms <br>
          > CONNECTION: SECURE
        </div>
      </div>
    </div>

    <!-- MAIN GRID -->
    <div class="max-w-[1400px] mx-auto px-6 grid grid-cols-1 lg:grid-cols-12 gap-12">
      
      <!-- ЛІВА ЧАСТИНА: ІНТЕРАКТИВНИЙ API-ТЕРМІНАЛ -->
      <div class="lg:col-span-5 flex flex-col gap-6">
        <h2 class="font-pixel text-2xl uppercase">// 1. SELECT_ENDPOINT</h2>
        
        <!-- Кнопки вибору -->
        <div class="flex flex-col gap-3">
          <button 
            v-for="(data, key) in contactEndpoints" 
            :key="key"
            @click="activeEndpoint = key"
            class="text-left border-4 border-black p-4 font-bold uppercase transition-all flex justify-between items-center group cursor-crosshair"
            :class="activeEndpoint === key ? 'bg-black text-[#F4F4F0] shadow-none translate-x-1 translate-y-1' : 'bg-white shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:bg-blue-200'"
          >
            <span><span class="font-pixel text-xs text-gray-400 mr-2">GET</span> /api/{{ key.toLowerCase() }}</span>
            <span class="font-pixel" :class="activeEndpoint === key ? 'text-green-400' : 'text-black'">[ {{ activeEndpoint === key ? 'OK' : 'EXECUTE' }} ]</span>
          </button>
        </div>

        <!-- Термінал з результатом -->
        <div class="bg-black border-4 border-gray-800 shadow-[12px_12px_0px_0px_rgba(59,130,246,1)] mt-4 flex flex-col min-h-[380px] max-w-full overflow-hidden">
          <div class="bg-gray-900 border-b-2 border-gray-800 p-2 flex justify-between items-center font-pixel text-[10px] text-gray-500 flex-none">
            <span>> RESPONSE_PAYLOAD</span>
            <button @click="copyToClipboard" class="text-white hover:text-green-400 transition-colors uppercase px-2 bg-gray-800 border border-gray-700 cursor-pointer">
              {{ isCopied ? '[ COPIED! ]' : '[ COPY_JSON ]' }}
            </button>
          </div>
          <!-- ВИПРАВЛЕНО: overflow-x-hidden + break-words прибирають горизонтальний скролбар -->
          <div class="p-6 overflow-y-auto overflow-x-hidden min-h-0 font-mono text-sm leading-relaxed flex-grow max-w-full">
            <transition name="fade" mode="out-in">
              <pre :key="activeEndpoint" class="text-gray-300 whitespace-pre-wrap break-words max-w-full"><span class="text-blue-400">{</span>
  <span class="text-red-400">"status"</span>: <span class="text-green-400">200</span>,
  <span class="text-red-400">"data"</span>: {<span v-for="(value, field) in contactEndpoints[activeEndpoint]" :key="field">
    <span class="text-yellow-300">"{{ field }}"</span>: <span class="text-green-300 break-words">"{{ value }}"</span>,</span>
  }
<span class="text-blue-400">}</span></pre>
            </transition>
          </div>
        </div>

      </div>

      <!-- ПРАВА ЧАСТИНА: МОДУЛЬ ГЕОЛОКАЦІЇ (КАРТИ) -->
      <div class="lg:col-span-7 flex flex-col gap-6">
        <div class="flex justify-between items-end">
          <h2 class="font-pixel text-2xl uppercase">// 2. GEOLOCATION_UPLINK</h2>
          
          <!-- Перемикач карти/Street View -->
          <div class="flex bg-black border-4 border-black shadow-[6px_6px_0px_0px_rgba(250,204,21,1)]">
            <button 
              @click="mapMode = 'map'" 
              class="font-pixel text-[10px] uppercase px-4 py-2 transition-colors cursor-pointer"
              :class="mapMode === 'map' ? 'bg-yellow-400 text-black' : 'text-gray-400 hover:text-white'"
            >
              MAP_VIEW
            </button>
            <button 
              @click="mapMode = 'street'" 
              class="font-pixel text-[10px] uppercase px-4 py-2 transition-colors cursor-pointer"
              :class="mapMode === 'street' ? 'bg-yellow-400 text-black' : 'text-gray-400 hover:text-white'"
            >
              STREET_CAM
            </button>
          </div>
        </div>

        <!--
          ВИПРАВЛЕНО: висота карти задана через inline style="height: 500px"
          замість класу h-[500px]. Це гарантує коректну висоту незалежно від
          того, чи встиг Tailwind згенерувати/підхопити arbitrary-value клас
          (саме через це карта "сплющувалась" — h-[500px] інколи не потрапляв
          у зібраний CSS через кеш).
        -->
        <div 
          class="border-4 border-black bg-white p-2 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] relative w-full"
          style="height: 500px; min-height: 500px;"
        >
          
          <!-- Декоративний HUD (завжди поверх карти) -->
          <div class="absolute top-4 left-4 z-20 pointer-events-none flex flex-col gap-1">
            <div class="bg-black/80 text-green-400 font-pixel text-[10px] px-2 py-1 border border-green-400/50 backdrop-blur-sm w-fit">
              LAT: 50.4619, LON: 30.4705
            </div>
            <div class="bg-black/80 text-green-400 font-pixel text-[10px] px-2 py-1 border border-green-400/50 backdrop-blur-sm w-fit">
              TARGET: F.I.T. KNU
            </div>
          </div>
          <div class="absolute bottom-4 right-4 z-20 pointer-events-none">
            <div class="w-12 h-12 border-2 border-red-500 rounded-full animate-ping opacity-70 flex items-center justify-center">
              <div class="w-2 h-2 bg-red-500 rounded-full"></div>
            </div>
          </div>

          <!-- Відносний wrapper для абсолютно позиційованих iframe. h-full тут спирається на батьківський inline-height, тож завжди коректний. -->
          <div class="relative w-full h-full overflow-hidden">
            <transition name="glitch" mode="out-in">
              <iframe 
                v-if="mapMode === 'map'"
                key="map"
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2539.880461877685!2d30.47053531573177!3d50.4619934794769!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x40d4ce82eb2fb5b9%3A0x6b3a0e6fa39b3607!2z0LLRg9C70LjRhtGPINCR0L7Qs9C00LDQvdCwINCT0LDQstGA0LjQu9C40YjQuNC90LAsIDI0LCDQmtC40ZfQsiLCAwMjAwMA!5e0!3m2!1suk!2sua!4v1698240000000!5m2!1suk!2sua" 
                class="absolute inset-0 border-2 border-black filter contrast-125 grayscale"
                style="width: 100%; height: 100%;"
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
              </iframe>
              
              <iframe 
                v-else
                key="street"
                src="https://www.google.com/maps/embed?pb=!4v1698240000000!6m8!1m7!1sCAoSLEFGMVFpcE5VUG82ZmZyYV9TUzJLZTBUaEdhZ3Z2Qk1kSkl3ZlJqN1pQcTRM!2m2!1d50.4619935!2d30.472724!3f260.5!4f5!5f0.7820865974627469" 
                class="absolute inset-0 border-2 border-black filter contrast-125 sepia-[0.3]"
                style="width: 100%; height: 100%;"
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
              </iframe>
            </transition>
          </div>

        </div>
        
        <div class="font-pixel text-[10px] text-gray-500 uppercase text-right mt-2">
          [!] Satellite & Ground imagery provided by Google Protocols.
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

const activeEndpoint = ref('ADDRESS');
const mapMode = ref('map'); // 'map' або 'street'
const isCopied = ref(false);
const pingLatency = ref(12);

const contactEndpoints = {
  ADDRESS: {
    faculty: 'Факультет інформаційних технологій',
    department: 'Кафедра мережевих та інтернет технологій',
    zip_code: '04116',
    country: 'Україна',
    city: 'Київ',
    street: 'вул. Богдана Гаврилишина, 24'
  },
  PHONES: {
    head_of_department: '+380(68) 124 2846',
    admissions_office: '+380(44) 481 4582'
  },
  EMAIL: {
    primary_contact: 'nit.fit.knu@gmail.com',
    support_ticket: 'nit.fit.knu@gmail.com'
  },
  SOCIALS: {
    facebook: 'https://surl.li/drftfb',
    instagram: '@mit_fit_knu',
    tiktok: '@mit_fit_knu'
  }
};

const copyToClipboard = async () => {
  try {
    const dataString = JSON.stringify(contactEndpoints[activeEndpoint.value], null, 2);
    await navigator.clipboard.writeText(dataString);
    isCopied.value = true;
    setTimeout(() => {
      isCopied.value = false;
    }, 2000);
  } catch (err) {
    console.error('Failed to copy!', err);
  }
};

onMounted(() => {
  if (import.meta.client) {
    setInterval(() => {
      pingLatency.value = Math.floor(Math.random() * (45 - 12 + 1)) + 12;
    }, 3000);
  }
});
</script>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(5px);
}

.glitch-enter-active {
  animation: glitch-anim 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94) both;
}
.glitch-leave-active {
  opacity: 0;
}

@keyframes glitch-anim {
  0% { filter: contrast(200%) hue-rotate(90deg); transform: scale(1.02); opacity: 0; }
  50% { filter: contrast(150%) hue-rotate(-90deg); opacity: 0.8; }
  100% { filter: contrast(125%) hue-rotate(0deg); transform: scale(1); opacity: 1; }
}
</style>