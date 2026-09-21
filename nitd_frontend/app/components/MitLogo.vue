<!-- components/MitLogo.vue -->
<template>
  <NuxtLink to="/" class="group flex items-center font-pixel text-3xl uppercase tracking-widest transition-all">
    <!-- Ліва дужка -->
    <span class="text-blue-600 group-hover:text-black transition-colors">[</span>
    
    <!-- Основний текст (інвертується при наведенні) -->
    <span class="text-black group-hover:bg-black group-hover:text-[#F4F4F0] px-1 transition-colors">
      MIT_DEPT
    </span>
    
    <!-- Права дужка -->
    <span class="text-blue-600 group-hover:text-black transition-colors">]</span>
    
    <!-- Блимаючий курсор -->
    <span class="w-3 h-7 ml-2 bg-blue-600 animate-pulse group-hover:bg-black"></span>
  </NuxtLink>
</template>