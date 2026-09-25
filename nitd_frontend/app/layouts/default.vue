<template>
  <div class="min-h-screen bg-[#F4F4F0] text-black selection:bg-black selection:text-[#F4F4F0] overflow-x-hidden">
    
    <!-- ДЕСКТОПНИЙ ХЕДЕР -->
    <header class="border-b-4 border-black sticky top-0 bg-[#F4F4F0] z-40">
      <div class="flex justify-between items-center px-6 py-4 max-w-[1400px] mx-auto">
        
        <MitLogo />

        <!-- Навігація (Desktop) -->
        <nav class="hidden md:flex gap-4 lg:gap-8 font-bold uppercase text-xs lg:text-sm tracking-widest relative items-center">
          <!-- ПРО НАС -->
          <div class="group relative">
            <button class="flex items-center gap-1.5 py-2 hover:text-blue-600 transition-colors">
              <span>Про нас</span><span class="font-pixel text-base mt-0.5">▼</span>
            </button>
            <div class="absolute top-full left-0 w-full h-2"></div>
            <div class="absolute top-[calc(100%+8px)] left-0 hidden group-hover:flex flex-col bg-[#F4F4F0] border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] w-60 z-50">
              <NuxtLink to="/about" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Про нас</NuxtLink>
              <NuxtLink to="/teachers" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Викладачі</NuxtLink>
              <NuxtLink to="/partners" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Наші партнери</NuxtLink>
              <NuxtLink to="/contacts" class="block px-4 py-3 hover:bg-blue-600 hover:text-[#F4F4F0]">Контакти</NuxtLink>
            </div>
          </div>
          
          <!-- СТУДЕНТАМ -->
          <div class="group relative">
            <button class="flex items-center gap-1.5 py-2 hover:text-blue-600 transition-colors">
              <span>Студентам</span><span class="font-pixel text-base mt-0.5">▼</span>
            </button>
            <div class="absolute top-[calc(100%+8px)] left-0 hidden group-hover:flex flex-col bg-[#F4F4F0] border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] w-64 z-50">
              <NuxtLink to="/schedule" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Розклад занять</NuxtLink>
              <NuxtLink to="/conferences" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Конференції</NuxtLink>
              <NuxtLink to="/olympiads" class="block px-4 py-3 hover:bg-blue-600 hover:text-[#F4F4F0]">Олімпіади</NuxtLink>
            </div>
          </div>
          
          <!-- ВСТУПНИКАМ -->
          <div class="group relative">
            <button class="flex items-center gap-1.5 py-2 hover:text-blue-600 transition-colors">
              <span>Вступникам</span><span class="font-pixel text-base mt-0.5">▼</span>
            </button>
            <div class="absolute top-[calc(100%+8px)] left-0 hidden group-hover:flex flex-col bg-[#F4F4F0] border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] w-72 z-50">
              <NuxtLink to="/invite" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Запрошуємо на навчання</NuxtLink>
              <NuxtLink to="/student-reviews" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Студенти про нас</NuxtLink>
              <NuxtLink to="/study-with-us" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Вивчимо разом</NuxtLink>
              <a href="https://vstup.knu.ua/admission-rules" target="_blank" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Правила вступу</a>
              <a href="https://drive.google.com/file/d/1ajsZQdVVL51n4AoA751qRbuLlXduAFPb/view" target="_blank" class="block px-4 py-3 border-b-2 border-black hover:bg-blue-600 hover:text-[#F4F4F0]">Програма фахового вступного випробовування G5</a>
            </div>
          </div>

          <!-- Інші лінки -->
          <NuxtLink to="/news" class="py-2 hover:text-blue-600 transition-colors">Новини</NuxtLink>
          <NuxtLink to="/education-process" class="py-2 hover:text-blue-600 transition-colors">Освітній процес</NuxtLink>
          <NuxtLink to="/science-edu-process" class="py-2 hover:text-blue-600 transition-colors">Наукова діяльність</NuxtLink>
          <NuxtLink to="/gallery" class="py-2 hover:text-blue-600 transition-colors">Галерея</NuxtLink>
        </nav>

        <!-- Кнопка відкриття мобільного меню -->
        <button 
          @click="isMenuOpen = true" 
          class="md:hidden border-2 border-black bg-black text-white px-4 py-2 hover:bg-blue-600 transition-colors active:translate-y-1 shadow-[4px_4px_0px_0px_rgba(0,0,0,0.2)]"
        >
          <span class="font-mono font-bold text-lg">MENU_</span>
        </button>

      </div>
    </header>

    <!-- ПОВНОЕКРАННЕ МОБІЛЬНЕ МЕНЮ (Command Center) -->
    <div 
      v-show="isMenuOpen" 
      class="md:hidden fixed inset-0 z-[100] bg-black text-[#F4F4F0] flex flex-col overflow-y-auto"
    >
      <!-- Шапка оверлею -->
      <div class="flex justify-between items-center p-6 border-b-2 border-gray-800 bg-gray-900 sticky top-0 z-10">
        <div class="font-pixel text-2xl text-green-400">~/navigation $</div>
        <button 
          @click="isMenuOpen = false" 
          class="border-2 border-red-500 text-red-500 px-4 py-2 font-mono font-bold hover:bg-red-500 hover:text-black transition-colors"
        >
          [ ESC ]
        </button>
      </div>

      <!-- Тіло меню -->
      <nav class="flex-1 p-6 font-mono text-lg space-y-2">
        
        <!-- Категорія: Про нас -->
        <div>
          <button 
            @click="toggleSection('about')" 
            class="w-full text-left font-black uppercase text-xl py-3 flex items-center gap-3 hover:text-blue-400 transition-colors"
            :class="activeSection === 'about' ? 'text-blue-500' : 'text-white'"
          >
            <span class="font-pixel text-2xl">{{ activeSection === 'about' ? '[-]' : '[+]' }}</span> ПРО НАС
          </button>
          
          <div v-show="activeSection === 'about'" class="flex flex-col pl-6 border-l-2 border-gray-700 ml-3 space-y-4 py-2">
            <NuxtLink @click="isMenuOpen = false" to="/about" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">├──</span> Про нас
            </NuxtLink>
            <NuxtLink @click="isMenuOpen = false" to="/teachers" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">├──</span> Викладачі
            </NuxtLink>
            <NuxtLink @click="isMenuOpen = false" to="/partners" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">├──</span> Наші партнери
            </NuxtLink>
            <NuxtLink @click="isMenuOpen = false" to="/contacts" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">└──</span> Контакти
            </NuxtLink>
          </div>
        </div>

        <!-- Категорія: Студентам -->
        <div>
          <button 
            @click="toggleSection('students')" 
            class="w-full text-left font-black uppercase text-xl py-3 flex items-center gap-3 hover:text-blue-400 transition-colors"
            :class="activeSection === 'students' ? 'text-blue-500' : 'text-white'"
          >
            <span class="font-pixel text-2xl">{{ activeSection === 'students' ? '[-]' : '[+]' }}</span> СТУДЕНТАМ
          </button>
          
          <div v-show="activeSection === 'students'" class="flex flex-col pl-6 border-l-2 border-gray-700 ml-3 space-y-4 py-2">
            <NuxtLink @click="isMenuOpen = false" to="/schedule" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">├──</span> Розклад занять
            </NuxtLink>
            <NuxtLink @click="isMenuOpen = false" to="/conferences" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">├──</span> Конференції
            </NuxtLink>
            <NuxtLink @click="isMenuOpen = false" to="/olympiads" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">└──</span> Олімпіади
            </NuxtLink>
          </div>
        </div>

        <!-- Категорія: Вступникам -->
        <div>
          <button 
            @click="toggleSection('entrants')" 
            class="w-full text-left font-black uppercase text-xl py-3 flex items-center gap-3 hover:text-blue-400 transition-colors"
            :class="activeSection === 'entrants' ? 'text-blue-500' : 'text-white'"
          >
            <span class="font-pixel text-2xl">{{ activeSection === 'entrants' ? '[-]' : '[+]' }}</span> ВСТУПНИКАМ
          </button>
          
          <div v-show="activeSection === 'entrants'" class="flex flex-col pl-6 border-l-2 border-gray-700 ml-3 space-y-4 py-2">
            <NuxtLink @click="isMenuOpen = false" to="/invite" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">├──</span> Запрошуємо на навчання
            </NuxtLink>
            <NuxtLink @click="isMenuOpen = false" to="/student-reviews" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">├──</span> Студенти про нас
            </NuxtLink>
            <a @click="isMenuOpen = false" href="https://vstup.knu.ua/admission-rules" target="_blank" class="flex items-center gap-2 text-gray-400 hover:text-white">
              <span class="text-gray-600">└──</span> Правила вступу ↗
            </a>
          </div>
        </div>

        <!-- Одиночні посилання -->
        <NuxtLink @click="isMenuOpen = false" to="/news" class="block font-black uppercase text-xl py-3 flex items-center gap-3 hover:text-blue-400 transition-colors">
          <span class="font-pixel text-2xl text-gray-600">[*]</span> НОВИНИ
        </NuxtLink>
        <NuxtLink @click="isMenuOpen = false" to="/education-process" class="block font-black uppercase text-xl py-3 flex items-center gap-3 hover:text-blue-400 transition-colors">
          <span class="font-pixel text-2xl text-gray-600">[*]</span> ОСВІТНІЙ ПРОЦЕС
        </NuxtLink>
        <NuxtLink @click="isMenuOpen = false" to="/science-edu-process" class="block font-black uppercase text-xl py-3 flex items-center gap-3 hover:text-blue-400 transition-colors">
          <span class="font-pixel text-2xl text-gray-600">[*]</span> НАУКОВА ДІЯЛЬНІСТЬ
        </NuxtLink>
        <NuxtLink @click="isMenuOpen = false" to="/gallery" class="block font-black uppercase text-xl py-3 flex items-center gap-3 hover:text-blue-400 transition-colors">
          <span class="font-pixel text-2xl text-gray-600">[*]</span> ГАЛЕРЕЯ
        </NuxtLink>

      </nav>
    </div>

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

        <!-- 2. Локація -->
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
              <a href="https://www.instagram.com/mit_fit_knu" class="flex items-center gap-2 hover:text-blue-600 transition-colors group">
                <span class="opacity-0 group-hover:opacity-100 font-pixel text-blue-600 transition-opacity">></span>
                Instagram
              </a>
              <a href="https://www.facebook.com" class="flex items-center gap-2 hover:text-blue-600 transition-colors group">
                <span class="opacity-0 group-hover:opacity-100 font-pixel text-blue-600 transition-opacity">></span>
                Facebook
              </a>
              <a href="https://www.tiktok.com/@mit_fit_knu" class="flex items-center gap-2 hover:text-blue-600 transition-colors group">
                <span class="opacity-0 group-hover:opacity-100 font-pixel text-blue-600 transition-opacity">></span>
                TikTok
              </a>
            </div>
          </div>
        </div>

      </div>

      <!-- Копірайт -->
      <div class="border-t-2 border-black px-6 py-3 flex justify-between items-center font-pixel text-sm uppercase bg-black text-[#F4F4F0]">
        <span>© 2026 MIT_DEPT. Всі права захищено.</span>
        <span class="animate-pulse">SYS_HALTED _</span>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const isMenuOpen = ref(false)
const activeSection = ref(null)

const toggleSection = (section) => {
  activeSection.value = activeSection.value === section ? null : section
}

watch(isMenuOpen, (isOpen) => {
  if (import.meta.client) {
    if (isOpen) {
      document.body.style.overflow = 'hidden'
    } else {
      document.body.style.overflow = ''
    }
  }
})
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;700;900&family=VT323&display=swap');

body { 
  font-family: 'Space Grotesk', sans-serif; 
}
.font-pixel { 
  font-family: 'VT323', monospace; 
}
@keyframes marquee {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-50%); }
}
.animate-marquee {
  display: inline-block;
  animation: marquee 15s linear infinite;
  min-width: 200%;
}
</style>