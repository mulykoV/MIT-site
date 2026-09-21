<template>
  <div class="min-h-screen bg-[#F4F4F0] text-black selection:bg-black selection:text-[#F4F4F0]">
    
    <header class="border-b-2 border-black sticky top-0 bg-[#F4F4F0] z-50">
      <div class="flex justify-between items-center px-6 py-4 max-w-[1400px] mx-auto">
        
        <!-- Вставляємо наш новий багаторазовий компонент логотипа -->
        <MitLogo />

        <!-- Навігація (Desktop) -->
        <nav class="hidden md:flex gap-4 lg:gap-8 font-bold uppercase text-xs lg:text-sm tracking-widest relative z-50 items-center">
          
          <!-- Дропдаун: ПРО НАС -->
          <div class="group relative">
            <button class="flex items-center gap-1.5 py-2 hover:text-blue-600 transition-colors">
              <span>Про нас</span>
              <span class="font-pixel text-base mt-0.5">▼</span>
            </button>
            <div class="absolute top-full left-0 w-full h-2"></div>
            <div class="absolute top-[calc(100%+8px)] left-0 hidden group-hover:flex flex-col bg-[#F4F4F0] border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] w-60 z-50">
              <NuxtLink to="/about" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Про нас</NuxtLink>
              <NuxtLink to="/teachers" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Викладачі</NuxtLink>
              <NuxtLink to="/partners" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Наші партнери</NuxtLink>
              <NuxtLink to="/achievements" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Досягнення</NuxtLink>
              <NuxtLink to="/contacts" class="block px-4 py-3 hover:bg-blue-600 hover:text-[#F4F4F0]">Контакти</NuxtLink>
            </div>
          </div>

          <!-- Дропдаун: СТУДЕНТАМ -->
          <div class="group relative">
            <button class="flex items-center gap-1.5 py-2 hover:text-blue-600 transition-colors">
              <span>Студентам</span>
              <span class="font-pixel text-base mt-0.5">▼</span>
            </button>
            <div class="absolute top-full left-0 w-full h-2"></div>
            <div class="absolute top-[calc(100%+8px)] left-0 hidden group-hover:flex flex-col bg-[#F4F4F0] border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] w-64 z-50">
              <NuxtLink to="/schedule" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Розклад 2026-2027</NuxtLink>
              <NuxtLink to="/conferences" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Конференції</NuxtLink>
              <NuxtLink to="/olympiads" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Олімпіади</NuxtLink>
              <NuxtLink to="/science-activity" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Наукова діяльність</NuxtLink>
              <NuxtLink to="/manuals" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Навчальні посібники</NuxtLink>
              <NuxtLink to="/curators" class="block px-4 py-3 hover:bg-blue-600 hover:text-[#F4F4F0]">Куратори</NuxtLink>
            </div>
          </div>

          <!-- Дропдаун: ВСТУПНИКАМ -->
          <div class="group relative">
            <button class="flex items-center gap-1.5 py-2 hover:text-blue-600 transition-colors">
              <span>Вступникам</span>
              <span class="font-pixel text-base mt-0.5">▼</span>
            </button>
            <div class="absolute top-full left-0 w-full h-2"></div>
            <div class="absolute top-[calc(100%+8px)] left-0 hidden group-hover:flex flex-col bg-[#F4F4F0] border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] w-72 z-50">
              <NuxtLink to="/invite" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Запрошуємо на навчання</NuxtLink>
              <NuxtLink to="/student-reviews" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Студенти про нас</NuxtLink>
              <NuxtLink to="/study-with-us" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Вивчимо разом</NuxtLink>
              <NuxtLink to="/admission-rules" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Правила вступу 2026</NuxtLink>
              <NuxtLink to="/exam-program" class="block px-4 py-3 hover:bg-blue-600 hover:text-[#F4F4F0]">Програма випробування</NuxtLink>
            </div>
          </div>

          <!-- Звичайне посилання: НОВИНИ -->
          <NuxtLink to="/news" class="py-2 hover:text-blue-600 transition-colors">Новини</NuxtLink>

          <!-- Дропдаун: ОСВІТНІЙ ПРОЦЕС -->
          <div class="group relative">
            <button class="flex items-center gap-1.5 py-2 hover:text-blue-600 transition-colors">
              <span>Освітній процес</span>
              <span class="font-pixel text-base mt-0.5">▼</span>
            </button>
            <div class="absolute top-full left-0 w-full h-2"></div>
            <div class="absolute top-[calc(100%+8px)] left-0 hidden group-hover:flex flex-col bg-[#F4F4F0] border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] w-[320px] z-50">
              <NuxtLink to="/educational-process" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Освітній процес</NuxtLink>
              <NuxtLink to="/surveys" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Опитування</NuxtLink>
              <NuxtLink to="/documents" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Нормативно-правові документи</NuxtLink>
              <NuxtLink to="/qualification-works" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Кваліфікаційні роботи</NuxtLink>
              <NuxtLink to="/accreditation-masters" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Акредитація магістрів 2023</NuxtLink>
              <NuxtLink to="/accreditation-bachelors" class="block px-4 py-3 hover:bg-blue-600 hover:text-[#F4F4F0]">Акредитація бакалаврів 2024</NuxtLink>
            </div>
          </div>

          <!-- Дропдаун: НАУКОВА ДІЯЛЬНІСТЬ -->
          <div class="group relative">
            <button class="flex items-center gap-1.5 py-2 hover:text-blue-600 transition-colors">
              <span>Наукова діяльність</span>
              <span class="font-pixel text-base mt-0.5">▼</span>
            </button>
            <div class="absolute top-full left-0 w-full h-2"></div>
            <div class="absolute top-[calc(100%+8px)] right-0 hidden group-hover:flex flex-col bg-[#F4F4F0] border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] w-72 z-50">
              <NuxtLink to="/science-directions" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Напрямки наукової діяльності</NuxtLink>
              <NuxtLink to="/laboratory" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Лабораторія сенсорного моніторингу</NuxtLink>
              <NuxtLink to="/research-projects" class="block px-4 py-3 hover:bg-blue-600 hover:text-[#F4F4F0]">Науково дослідні проєкти</NuxtLink>
            </div>
          </div>

          <!-- Звичайне посилання: ГАЛЕРЕЯ -->
          <NuxtLink to="/gallery" class="py-2 hover:text-blue-600 transition-colors">Галерея</NuxtLink>
          
        </nav>

        <!-- Гамбургер для мобілки -->
        <button class="md:hidden border-2 border-black p-2 hover:bg-black hover:text-[#F4F4F0]">
          <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square" stroke-linejoin="miter"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
        </button>

      </div>
    </header>

    <main>
      <slot />
    </main>

    <!-- НОВИЙ БРУТАЛЬНИЙ ФУТЕР -->
    <footer class="mt-20 border-t-2 border-black bg-[#F4F4F0] text-black">
      
      <!-- Стрічка партнерів (Marquee) -->
      <div class="border-b-2 border-black bg-blue-600 text-[#F4F4F0] py-3 overflow-hidden flex whitespace-nowrap font-pixel text-xl uppercase tracking-widest">
        <div class="animate-marquee inline-block min-w-full">
          [ ПАРТНЕРИ ] IEEE * НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ОБОРОНИ * LIFECELL * HUAWEI * 
          [ ПАРТНЕРИ ] IEEE * НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ОБОРОНИ * LIFECELL * HUAWEI * 
        </div>
      </div>

      <!-- Основна сітка футера -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 divide-y-2 md:divide-y-0 md:divide-x-2 divide-black">
        
        <!-- 1. Бренд та Університет -->
        <div class="p-8 flex flex-col justify-between bg-black text-[#F4F4F0]">
          <div>
            <div class="font-pixel text-4xl text-blue-500 mb-6">[MIT_DEPT]</div>
            <p class="font-bold text-sm uppercase leading-relaxed text-gray-300">
              Київський національний<br/>університет імені Тараса Шевченка
            </p>
            <p class="font-bold text-sm uppercase leading-relaxed mt-4">
              Факультет інформаційних технологій
            </p>
          </div>
        </div>

        <!-- 2. Локація (замість важких Google Maps) -->
        <div class="p-8 flex flex-col justify-between">
          <div>
            <h4 class="font-pixel text-xl text-gray-500 mb-6">// ЛОКАЦІЯ</h4>
            <p class="font-bold text-lg uppercase leading-tight mb-2">
              Україна, м. Київ
            </p>
            <p class="font-bold text-lg uppercase leading-tight">
              вул. Богдана<br/>Гаврилишина, 24
            </p>
            <p class="font-pixel text-sm text-gray-500 mt-4">Індекс: 04116</p>
          </div>
          <!-- Кнопка замість iframe карти -->
          <a href="https://maps.google.com/?q=Богдана+Гаврилишина+24+Київ" target="_blank" class="mt-8 inline-block border-2 border-black bg-[#c7d2fe] text-center py-3 font-bold uppercase hover:bg-black hover:text-[#F4F4F0] transition-colors shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
            Відкрити Мапу ↗
          </a>
        </div>

        <!-- 3. Контакти -->
        <div class="p-8">
          <h4 class="font-pixel text-xl text-gray-500 mb-6">// ЗВ'ЯЗОК</h4>
          <ul class="space-y-6 font-bold text-sm uppercase">
            <li class="flex flex-col group">
              <span class="font-pixel text-xs text-gray-500 mb-1">Email_Address:</span>
              <a href="mailto:nit.fit.knu@gmail.com" class="text-base group-hover:text-blue-600 transition-colors">nit.fit.knu@gmail.com</a>
            </li>
            <li class="flex flex-col">
              <span class="font-pixel text-xs text-gray-500 mb-1">Завідувач кафедри:</span>
              <span class="text-base">+380 (68) 124 2846</span>
            </li>
            <li class="flex flex-col">
              <span class="font-pixel text-xs text-gray-500 mb-1">Приймальна комісія:</span>
              <span class="text-base">+380 (44) 481 4582</span>
            </li>
          </ul>
        </div>

        <!-- 4. Соцмережі -->
        <div class="p-8 flex flex-col justify-between bg-[#F4F4F0]">
          <div>
            <h4 class="font-pixel text-xl text-gray-500 mb-6">// МЕРЕЖА</h4>
            <div class="flex flex-col gap-4 font-black text-2xl uppercase">
              <a href="https://www.instagram.com/mit_fit_knu?igsh=dXpvZnFqcTNhMXY2" class="flex items-center gap-2 hover:text-blue-600 transition-colors group">
                <span class="opacity-0 group-hover:opacity-100 font-pixel text-blue-600 transition-opacity">></span>
                Instagram
              </a>
              <a href="https://www.facebook.com/people/%D0%9A%D0%B0%D1%84%D0%B5%D0%B4%D1%80%D0%B0-%D0%BC%D0%B5%D1%80%D0%B5%D0%B6%D0%B5%D0%B2%D0%B8%D1%85-%D1%82%D0%B0-%D1%96%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82-%D1%82%D0%B5%D1%85%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D1%96%D0%B9/100028971204854/" class="flex items-center gap-2 hover:text-blue-600 transition-colors group">
                <span class="opacity-0 group-hover:opacity-100 font-pixel text-blue-600 transition-opacity">></span>
                Facebook
              </a>
              <a href="https://www.tiktok.com/@mit_fit_knu?_r=1&_t=ZS-95iAT1dQ1sw&fbclid=PAT01DUARmpcRleHRuA2FlbQIxMABzcnRjBmFwcF9pZA81NjcwNjczNDMzNTI0MjcAAac7U2gp4mPQSdys8pjlM_GSygX-vJvd-VT6wrsMd_Pg7-a-OV81tUyau5fCOw_aem_QOeThlIRXYHrMI5WA6Z-_Q%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%D0%A2%D1%96%D0%BA%20%D1%82%D0%BE%D0%BA" class="flex items-center gap-2 hover:text-blue-600 transition-colors group">
                <span class="opacity-0 group-hover:opacity-100 font-pixel text-blue-600 transition-opacity">></span>
                TikTok
              </a>
            </div>
          </div>
        </div>

      </div>

      <!-- Копірайт (Термінальний рядок) -->
      <div class="border-t-2 border-black px-6 py-3 flex justify-between items-center font-pixel text-sm uppercase bg-black text-[#F4F4F0]">
        <span>© 2026 MIT_DEPT. Всі права захищено.</span>
        <span class="animate-pulse">SYS_HALTED _</span>
      </div>
    </footer>
  </div>
</template>
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700;900&family=VT323&display=swap');

body { 
  font-family: 'Space Grotesk', sans-serif; 
}
.font-pixel { 
  font-family: 'VT323', monospace; 
}
</style>