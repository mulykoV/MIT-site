<template>
  <div class="min-h-screen bg-[#F4F4F0] text-black selection:bg-black selection:text-[#F4F4F0] overflow-x-hidden">
    
    <!-- ДЕСКТОПНИЙ ХЕДЕР -->
    <header class="border-b-4 border-black sticky top-0 bg-[#F4F4F0] z-40">
      <div class="flex justify-between items-center px-6 py-4 max-w-[1400px] mx-auto">
        
        <MitLogo />

        <!-- Навігація (Desktop) -->
        <nav class="hidden md:flex gap-4 lg:gap-8 font-bold uppercase text-xs lg:text-sm tracking-widest relative items-center">
          <!-- Твої десктопні дропдауни залишаються без змін -->
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
          <!-- Інші десктопні лінки -->
          <NuxtLink to="/news" class="py-2 hover:text-blue-600 transition-colors">Новини</NuxtLink>
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
      <div class="flex justify-between items-center p-6 border-b-2 border-gray-800 bg-gray-900 sticky top-0">
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

        <!-- Одиночні посилання (Без підменю) -->
        <NuxtLink @click="isMenuOpen = false" to="/news" class="block font-black uppercase text-xl py-3 flex items-center gap-3 hover:text-blue-400 transition-colors">
          <span class="font-pixel text-2xl text-gray-600">[*]</span> НОВИНИ
        </NuxtLink>
        <NuxtLink @click="isMenuOpen = false" to="/gallery" class="block font-black uppercase text-xl py-3 flex items-center gap-3 hover:text-blue-400 transition-colors">
          <span class="font-pixel text-2xl text-gray-600">[*]</span> ГАЛЕРЕЯ
        </NuxtLink>

      </nav>
    </div>

    <!-- Основний контент -->
    <main>
      <slot />
    </main>

    <!-- Твій Футер -->
    <footer>...</footer>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'

const isMenuOpen = ref(false)
const activeSection = ref(null) // Зберігає ID відкритої категорії

// Функція для перемикання категорій
const toggleSection = (section) => {
  // Якщо клікаємо на вже відкриту — закриваємо її, інакше відкриваємо нову
  activeSection.value = activeSection.value === section ? null : section
}

// Блокуємо скрол сторінки під меню, коли воно відкрите
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