<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-red-500 selection:text-white pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Технічна сітка + точки) -->
    <div class="absolute inset-0 opacity-20 bg-[linear-gradient(rgba(0,0,0,0.2)_1px,transparent_1px),linear-gradient(90deg,rgba(0,0,0,0.2)_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-12 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-red-600 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(220,38,38,1)]">[ BACHELOR_DEGREE ]</div>
          <h1 class="text-5xl md:text-7xl lg:text-8xl font-black uppercase tracking-tighter leading-none">
            МЕРЕЖЕВІ ТА <br>
            <span class="text-white bg-black px-4 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">ІНТЕРНЕТ ТЕХНОЛОГІЇ</span>
          </h1>
        </div>
        
        <div class="flex flex-col gap-2 shrink-0">
          <NuxtLink to="/education" class="font-pixel text-xs bg-white text-black px-6 py-3 uppercase border-4 border-black hover:bg-red-600 hover:text-white transition-colors shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] text-center">
            ← НАЗАД ДО БАЗИ
          </NuxtLink>
        </div>
      </div>

      <!-- ГОЛОВНИЙ БЛОК (ІНТРО ТА СПЕЦИФІКАЦІЯ) -->
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 mb-8">
        
        <!-- Ліва частина: Основний опис -->
        <div class="lg:col-span-8 bg-white border-4 border-black p-8 md:p-12 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] flex flex-col justify-center relative overflow-hidden group">
          <div class="absolute -right-10 -bottom-10 text-[200px] opacity-5 font-black pointer-events-none group-hover:scale-110 transition-transform text-black">172</div>
          
          <div class="font-pixel text-xs text-gray-500 mb-6 border-b-2 border-dashed border-gray-300 pb-2 uppercase">
            // PROGRAM_OVERVIEW
          </div>
          
          <p class="text-xl md:text-2xl font-bold leading-relaxed mb-6 relative z-10">
            Кафедра Мережевих та інтернет технологій проводить навчання студентів за освітнім ступенем <span class="bg-red-500 text-white px-2">«бакалавр»</span> за новою освітньою програмою «Мережеві та інтернет технології» на денну форму навчання.
          </p>
          
          <p class="font-mono text-base md:text-lg text-gray-700 leading-relaxed relative z-10 border-l-4 border-red-500 pl-4">
            Мережеві та інтернет технології – побудова та експлуатація телекомунікаційних систем та мереж: систем широкосмугового абонентського доступу з використанням перспективних технологічних рішень, технічне та програмне забезпечення роботи операторів мобільного зв'язку, інтернет провайдерів, створення, супровід і використання сучасних інтернет технологій, соціальних мереж, інтернет речей.
          </p>
        </div>

        <!-- Права частина: Системні вимоги (Коди спеціальностей) -->
        <div class="lg:col-span-4 flex flex-col gap-8">
          
          <!-- Спеціальність -->
          <div class="bg-black text-white border-4 border-black p-8 shadow-[8px_8px_0px_0px_rgba(220,38,38,1)] hover:-translate-y-1 transition-transform flex flex-col justify-center h-1/2">
            <div class="font-pixel text-[10px] text-red-500 mb-2 uppercase">СПЕЦІАЛЬНІСТЬ</div>
            <div class="text-6xl font-black mb-2 text-white">172</div>
            <div class="font-mono font-bold text-lg uppercase text-zinc-300">
              Телекомунікації та радіотехніка
            </div>
          </div>

          <!-- Галузь -->
          <div class="bg-zinc-200 border-4 border-black p-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-1 transition-transform flex flex-col justify-center h-1/2">
            <div class="font-pixel text-[10px] text-gray-600 mb-2 uppercase">ГАЛУЗЬ ЗНАНЬ</div>
            <div class="text-5xl font-black mb-2 text-black">17</div>
            <div class="font-mono font-bold text-lg uppercase text-black">
              Електроніка та телекомунікації
            </div>
          </div>

        </div>
      </div>

      <!-- ДРУГИЙ РЯД (BENTO GRID: Практика, Партнери, Викладачі) -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 mb-16">
        
        <!-- Блок 1: Викладачі та матеріали -->
        <div class="border-4 border-black bg-white p-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] hover:bg-black hover:text-white transition-colors group flex flex-col justify-between">
          <div>
            <div class="font-pixel text-xl mb-4 group-hover:text-red-500">📚 ACADEMIC_CORE</div>
            <p class="font-mono font-medium text-sm md:text-base leading-relaxed">
              На кафедрі розроблено навчальні, навчально-методичні посібники та електронні навчально-методичні комплекси з навчальних дисциплін.
            </p>
          </div>
          <div class="mt-6 pt-4 border-t-2 border-dashed border-gray-400 group-hover:border-zinc-700">
            <p class="font-bold text-sm md:text-base">
              Заняття проводять досвідчені викладачі, професори, доценти та провідні спеціалісти фірм-розробників сучасних інформаційних систем і технологій.
            </p>
          </div>
        </div>

        <!-- Блок 2: Партнери (LIFECELL & CISCO) -->
        <div class="border-4 border-black bg-red-600 text-white p-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] flex flex-col justify-center relative overflow-hidden">
          <div class="absolute -right-6 -bottom-6 font-pixel text-[150px] opacity-10 pointer-events-none text-black">!</div>
          <div class="font-pixel text-xl mb-6 text-black bg-white px-2 py-1 w-fit shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
            INDUSTRY_INTEGRATION
          </div>
          
          <div class="flex flex-col gap-6 relative z-10">
            <div class="bg-black p-4 border-2 border-black flex flex-col gap-2">
              <span class="font-black text-2xl tracking-widest text-white">LIFECELL</span>
              <span class="font-mono text-xs text-red-400">Практичні заняття проходять в навчальному центрі компанії.</span>
            </div>
            
            <div class="bg-white text-black p-4 border-2 border-black flex flex-col gap-2">
              <span class="font-black text-2xl tracking-widest text-blue-600">CISCO ACADEMY</span>
              <span class="font-mono text-xs text-gray-700 font-bold">В навчальний процес впроваджені офіційні курси академії.</span>
            </div>
          </div>
        </div>

        <!-- Блок 3: Обладнання (Термінал) -->
        <div class="border-4 border-black bg-zinc-900 text-green-400 p-8 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] flex flex-col justify-between">
          <div class="font-mono text-xs mb-4 border-b-2 border-zinc-700 pb-4">
            <span class="text-white">root@mit-lab:~$</span> scan_hardware <br>
            <span class="text-zinc-500">> detecting devices...</span><br>
            <span class="text-green-500 animate-pulse">STATUS: LABS_ONLINE</span>
          </div>
          <div>
            <h3 class="text-2xl font-black uppercase text-white mb-4">Реальне залізо</h3>
            <p class="font-mono text-sm leading-relaxed text-zinc-300">
              Студенти кафедри під час навчання знайомляться з обладнанням різноманітних об'єктів інформаційної діяльності. Ніякої сухої теорії — лише практика на діючій інфраструктурі.
            </p>
          </div>
        </div>

      </div>

      <!-- КНОПКА ЗАЯВКИ (CALL TO ACTION) -->
      <div class="flex justify-center mt-12">
        <a href="https://vstup.edbo.gov.ua/" target="_blank" class="group flex items-center bg-black text-white font-pixel text-xl md:text-2xl px-10 py-6 border-4 border-black uppercase tracking-widest shadow-[8px_8px_0px_0px_rgba(220,38,38,1)] hover:-translate-y-2 hover:translate-x-2 hover:shadow-none active:translate-y-4 active:translate-x-4 transition-all">
          > ПОДАТИ ЗАЯВКУ НА ВСТУП
          <svg class="w-8 h-8 ml-4 group-hover:rotate-45 group-hover:text-red-500 transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
        </a>
      </div>

    </div>
  </div>
</template>

<script setup>
// Сторінка статична, дані інтегровані з наданого тексту. 
// Спеціальних запитів до API тут не потрібно.
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