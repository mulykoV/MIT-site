<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-blue-600 selection:text-white pb-32">
    
    <!-- ВЕРХНЯ СЕКЦІЯ: НАВІГАЦІЯ ТА СТАТУС ГРИ -->
    <div class="pt-32 lg:pt-48 px-6 max-w-[1400px] mx-auto border-b-4 border-black pb-16 mb-16">
      <div class="flex flex-col lg:flex-row justify-between items-end gap-12">
        
        <!-- Заголовок -->
        <div class="max-w-3xl relative z-10">
          <div class="font-pixel text-red-500 text-xl mb-4 uppercase tracking-widest">[ ALLIANCE_NETWORK ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter leading-[0.9] mb-6">
            НАШІ <br><span class="text-black bg-yellow-400 px-2 mt-2 inline-block">ПАРТНЕРИ</span>
          </h1>
          <p class="text-xl font-bold text-gray-800 border-l-4 border-black pl-4">
            З ким ми співпрацюємо. Щоб отримати доступ до даних корпоративних вузлів, ініціюйте протокол дешифрування (клікніть на закриті блоки).
          </p>
        </div>

        <!-- Ігровий статус-борд -->
        <div class="bg-black text-[#F4F4F0] border-4 border-black p-6 shadow-[8px_8px_0px_0px_rgba(239,68,68,1)] w-full lg:w-80 relative z-10">
          <div class="font-pixel text-xs text-gray-400 mb-4">// DECRYPTION_PROGRESS</div>
          
          <div class="w-full h-6 border-2 border-gray-600 bg-gray-900 mb-2 relative overflow-hidden">
            <div 
              class="h-full bg-red-500 transition-all duration-500 ease-out"
              :style="{ width: `${(decryptedCount / partners.length) * 100}%` }"
            ></div>
          </div>
          
          <div class="flex justify-between items-center font-pixel text-lg">
            <span :class="decryptedCount === partners.length ? 'text-green-400 animate-pulse' : 'text-white'">
              {{ decryptedCount }} / {{ partners.length }} UNLOCKED
            </span>
          </div>

          <button 
            v-if="decryptedCount === partners.length"
            @click="resetGame" 
            class="mt-4 w-full border-2 border-green-400 bg-green-400/20 text-green-400 font-pixel text-xs py-2 hover:bg-green-400 hover:text-black transition-colors"
          >
            > REBOOT_SYSTEM
          </button>
        </div>

      </div>
    </div>

    <!-- МІНІ-ГРА: СІТКА ПАРТНЕРІВ -->
    <div class="max-w-[1400px] mx-auto px-6 relative">
      
      <!-- Секретне повідомлення при перемозі -->
      <div v-if="decryptedCount === partners.length" class="absolute -top-10 left-1/2 -translate-x-1/2 font-pixel text-green-500 text-xl lg:text-3xl text-center z-50 animate-bounce w-full pointer-events-none drop-shadow-[0_0_10px_rgba(74,222,128,0.8)]">
        *** ALL PEERS CONNECTED. INTERNSHIPS UNLOCKED. ***
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-8">
        
        <div 
          v-for="(partner, index) in partners" 
          :key="partner.id" 
          @click="decryptNode(index)"
          class="relative border-4 border-black transition-all duration-300 min-h-[300px] flex flex-col"
          :class="[
            partner.decrypted 
              ? 'bg-white shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-2' 
              : 'bg-zinc-900 cursor-crosshair hover:bg-black shadow-[8px_8px_0px_0px_rgba(239,68,68,0.5)]'
          ]"
        >
          
          <!-- СТАН 1: ЗАШИФРОВАНО -->
          <div v-if="!partner.decrypted" class="absolute inset-0 flex flex-col items-center justify-center p-6 text-center z-10">
            <div class="w-16 h-16 border-4 border-red-500 rounded-full flex items-center justify-center mb-4" :class="{ 'animate-spin': partner.isDecrypting }">
              <span class="font-pixel text-red-500 text-2xl">?</span>
            </div>
            <h3 class="font-pixel text-xl md:text-2xl text-red-500 break-all mb-2">
              {{ partner.isDecrypting ? partner.scrambledName : 'ENCRYPTED_NODE' }}
            </h3>
            <p class="font-mono text-xs text-gray-500 uppercase">
              {{ partner.isDecrypting ? '>> BRUTEFORCING_KEY...' : 'Click to initialize decryption protocol' }}
            </p>
          </div>

          <!-- СТАН 2: РОЗШИФРОВАНО (Вміст картки партнера) -->
          <div v-else class="flex flex-col h-full opacity-0 animate-fade-in relative z-20">
            <!-- Кольорова стрічка-ідентифікатор компанії -->
            <div class="h-3 w-full border-b-4 border-black" :class="partner.color"></div>
            
            <div class="p-8 flex-grow flex flex-col">
              <div class="flex justify-between items-start mb-6">
                <!-- Назва / Логотип текстом -->
                <h2 class="text-4xl font-black uppercase tracking-tighter" :class="partner.textColor">
                  {{ partner.name }}
                </h2>
                <div class="font-pixel text-[10px] bg-green-100 text-green-700 border border-green-700 px-2 py-1">
                  SECURE
                </div>
              </div>
              
              <div class="font-mono text-sm leading-relaxed text-gray-800 border-l-4 pl-4 flex-grow" :class="`border-${partner.borderColor}`">
                {{ partner.desc }}
              </div>
            </div>

            <!-- Нижній термінальний рядок -->
            <div class="bg-gray-100 border-t-4 border-black px-6 py-3 font-pixel text-[10px] text-gray-500 flex justify-between uppercase">
              <span>STATUS: ESTABLISHED</span>
              <span>ID: 0x{{ Math.floor(Math.random() * 10000) }}</span>
            </div>
          </div>

        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed } from 'vue';

// Дані партнерів з твого скриншоту
const partners = ref([
  { 
    id: 'cisco', 
    name: 'CISCO', 
    desc: 'Американська транснаціональна компанія, що розробляє і продає мережеве обладнання, призначене в основному для великих організацій і телекомунікаційних підприємств. Одна з найбільших в світі компаній, що спеціалізуються в області високих технологій.',
    color: 'bg-blue-500', textColor: 'text-blue-600', borderColor: 'blue-500',
    decrypted: false, isDecrypting: false, scrambledName: ''
  },
  { 
    id: 'huawei', 
    name: 'HUAWEI', 
    desc: 'Світовий лідер у сфері телекомунікацій. Забезпечує інтегровані рішення для мереж та створює всі умови для швидкого старту кар\'єри — включаючи потужну індустріальну практику для студентів на базі реальних процесів.',
    color: 'bg-red-600', textColor: 'text-red-600', borderColor: 'red-600',
    decrypted: false, isDecrypting: false, scrambledName: ''
  },
  { 
    id: 'ieee', 
    name: 'IEEE', 
    desc: 'Найбільша в світі технічна професійна організація з просування технологій. Відкриває студентам доступ до глобальних наукових публікацій, стандартів та світового інженерного ком\'юніті.',
    color: 'bg-cyan-600', textColor: 'text-cyan-700', borderColor: 'cyan-600',
    decrypted: false, isDecrypting: false, scrambledName: ''
  },
  { 
    id: 'nuou', 
    name: 'НУОУ', 
    desc: 'Національний університет оборони України імені Івана Черняховського. Сучасний військовий освітній і науковий заклад, з яким ми ведемо спільні фундаментальні дослідження.',
    color: 'bg-yellow-500', textColor: 'text-yellow-600', borderColor: 'yellow-500',
    decrypted: false, isDecrypting: false, scrambledName: ''
  },
  { 
    id: 'lifecell', 
    name: 'LIFECELL', 
    desc: 'Діджитал оператор, який завжди був драйвером телеком-ринку України. Пропонує абонентам передові послуги і розвиває інноваційну екосистему телеком індустрії спільно з нами.',
    color: 'bg-blue-800', textColor: 'text-blue-800', borderColor: 'blue-800',
    decrypted: false, isDecrypting: false, scrambledName: ''
  }
]);

const decryptedCount = computed(() => partners.value.filter(p => p.decrypted).length);

// Логіка хакерського дешифрування
const decryptNode = (index) => {
  const node = partners.value[index];
  if (node.decrypted || node.isDecrypting) return;
  
  node.isDecrypting = true;
  
  let iterations = 0;
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*<>/?';
  
  const interval = setInterval(() => {
    // Генеруємо випадковий рядок
    node.scrambledName = Array(12).fill(0).map(() => chars[Math.floor(Math.random() * chars.length)]).join('');
    iterations++;
    
    // Після 15 ітерацій (~750мс) "зламуємо" вузол
    if (iterations > 15) {
      clearInterval(interval);
      node.decrypted = true;
      node.isDecrypting = false;
    }
  }, 50);
};

const resetGame = () => {
  partners.value.forEach(p => {
    p.decrypted = false;
    p.isDecrypting = false;
    p.scrambledName = '';
  });
};
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}
.animate-fade-in {
  animation: fadeIn 0.4s ease-out forwards;
}
</style>