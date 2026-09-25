<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-blue-600 selection:text-white pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон -->
    <div class="absolute inset-0 opacity-10 bg-[linear-gradient(45deg,#000_25%,transparent_25%,transparent_75%,#000_75%,#000),linear-gradient(45deg,#000_25%,transparent_25%,transparent_75%,#000_75%,#000)] bg-[size:20px_20px] bg-[position:0_0,10px_10px] pointer-events-none"></div>

    <div class="max-w-[1200px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="text-center mb-16">
        <div class="font-pixel text-blue-600 text-sm md:text-base mb-4 uppercase tracking-widest font-bold">
          [ КАФЕДРА МЕРЕЖЕВИХ ТА ІНТЕРНЕТ ТЕХНОЛОГІЙ ]
        </div>
        <h1 class="text-3xl md:text-5xl lg:text-6xl font-black uppercase tracking-tighter leading-tight bg-black text-white inline-block px-6 py-4 shadow-[8px_8px_0px_0px_rgba(37,99,235,1)]">
          ОПИС ОСВІТНЬОЇ ПРОГРАМИ <br>ДЛЯ ОР "МАГІСТР" 2025
        </h1>
      </div>

      <!-- PDF VIEWER -->
      <div class="border-8 border-black bg-zinc-200 shadow-[16px_16px_0px_0px_rgba(0,0,0,1)] mb-20 relative flex flex-col h-[70vh] md:h-[85vh]">
        
        <!-- Панель інструментів плеєра -->
        <div class="bg-black text-white p-3 flex justify-between items-center border-b-4 border-black shrink-0">
          <div class="flex items-center gap-4">
            <span class="font-pixel text-xs text-blue-500 animate-pulse">● SECURE_DOC</span>
            <span class="font-mono text-xs hidden md:inline">ID_98214_MASTER_DEGREE</span>
          </div>
          <!-- Увага: шлях до файлу магістратури -->
          <a href="/documentes/master-program-2025.pdf" download class="font-pixel text-[10px] bg-white text-black px-3 py-1 hover:bg-blue-600 hover:text-white transition-colors cursor-pointer border-2 border-white">
            [ ЗАВАНТАЖИТИ PDF ]
          </a>
        </div>
        
        <!-- Iframe для PDF -->
        <div class="flex-grow relative w-full h-full bg-white">
          <!-- Увага: шлях до файлу магістратури -->
          <iframe 
            src="/documentes/OOP_mag2025.pdf#toolbar=0" 
            class="absolute top-0 left-0 w-full h-full"
            frameborder="0"
          ></iframe>
        </div>
      </div>

      <!-- ФОРМА ЗВОРОТНОГО ЗВ'ЯЗКУ -->
      <div class="max-w-3xl mx-auto bg-white border-4 border-black p-8 md:p-12 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] relative">
        <!-- Декоративний елемент -->
        <div class="absolute -top-6 -left-6 bg-blue-600 text-white font-pixel text-4xl w-12 h-12 flex items-center justify-center border-4 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
          ?
        </div>

        <h2 class="text-xl md:text-2xl font-black uppercase mb-2">Залишити пропозицію</h2>
        <p class="font-mono text-sm text-gray-600 mb-8 border-b-2 border-dashed border-gray-300 pb-4">
          Якщо у Вас є пропозиції щодо покращення освітньої програми, надішліть нам Ваші пропозиції/зауваження.
        </p>

        <form @submit.prevent="submitFeedback" class="flex flex-col gap-6">
          
          <div class="flex flex-col gap-2">
            <label class="font-pixel text-xs text-gray-500 uppercase">ПІБ</label>
            <input 
              v-model="form.name" 
              type="text" 
              required
              placeholder="Name" 
              class="w-full border-2 border-black p-4 font-mono focus:outline-none focus:border-blue-600 focus:shadow-[4px_4px_0px_0px_rgba(37,99,235,1)] transition-all bg-[#F4F4F0]"
            />
          </div>

          <div class="flex flex-col gap-2">
            <label class="font-pixel text-xs text-gray-500 uppercase">Email</label>
            <input 
              v-model="form.email" 
              type="email" 
              required
              placeholder="name@example.com" 
              class="w-full border-2 border-black p-4 font-mono focus:outline-none focus:border-blue-600 focus:shadow-[4px_4px_0px_0px_rgba(37,99,235,1)] transition-all bg-[#F4F4F0]"
            />
          </div>

          <div class="flex flex-col gap-2">
            <label class="font-pixel text-xs text-gray-500 uppercase">Повідомлення</label>
            <textarea 
              v-model="form.message" 
              required
              placeholder="Text" 
              rows="5"
              class="w-full border-2 border-black p-4 font-mono focus:outline-none focus:border-blue-600 focus:shadow-[4px_4px_0px_0px_rgba(37,99,235,1)] transition-all bg-[#F4F4F0] resize-y"
            ></textarea>
          </div>

          <!-- Повідомлення про статус -->
          <div v-if="statusMessage" :class="statusClass" class="p-4 border-2 border-black font-mono font-bold text-sm uppercase">
            {{ statusMessage }}
          </div>

          <button 
            type="submit" 
            :disabled="isSubmitting"
            class="bg-blue-600 text-white font-pixel text-lg md:text-xl uppercase py-5 px-8 border-4 border-black hover:bg-black transition-colors shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:shadow-none hover:translate-x-1 hover:translate-y-1 mt-4 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ isSubmitting ? 'ВІДПРАВКА...' : 'ВІДПРАВИТИ' }}
          </button>
        </form>

      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const form = ref({
  name: '',
  email: '',
  message: ''
});

const isSubmitting = ref(false);
const statusMessage = ref('');
const statusClass = ref('');

const submitFeedback = async () => {
  isSubmitting.value = true;
  statusMessage.value = '';
  
  try {
    const response = await $fetch('http://127.0.0.1:8000/api/v1/feedback/', {
      method: 'POST',
      body: form.value
    });
    
    // Успіх
    statusMessage.value = '[ СИСТЕМА ] ПРОПОЗИЦІЮ УСПІШНО ВІДПРАВЛЕНО НА СЕРВЕР!';
    statusClass.value = 'bg-green-400 text-black';
    
    // Очищаємо форму
    form.value = { name: '', email: '', message: '' };
    
    // Прибираємо повідомлення через 5 секунд
    setTimeout(() => { statusMessage.value = ''; }, 5000);
    
  } catch (error) {
    statusMessage.value = '[ ПОМИЛКА ] НЕ ВДАЛОСЯ ВІДПРАВИТИ ДАНІ. ПЕРЕВІРТЕ ЗВ\'ЯЗОК АБО ФОРМАТ EMAIL.';
    statusClass.value = 'bg-red-200 text-red-700';
  } finally {
    isSubmitting.value = false;
  }
};
</script>