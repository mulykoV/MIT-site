<template>
  <div class="bg-[#F4F4F0] min-h-screen text-black font-mono selection:bg-blue-600 selection:text-white pb-32 pt-32 lg:pt-40 relative overflow-hidden">
    
    <!-- Декоративний фон (Сітка) -->
    <div class="absolute inset-0 opacity-10 bg-[linear-gradient(#000_1px,transparent_1px),linear-gradient(90deg,#000_1px,transparent_1px)] bg-[size:40px_40px] pointer-events-none"></div>

    <div class="max-w-[1400px] mx-auto px-6 relative z-10">
      
      <!-- HEADER -->
      <div class="border-b-8 border-black pb-8 mb-12 flex flex-col md:flex-row justify-between items-end gap-6">
        <div>
          <div class="font-pixel text-blue-600 text-xl mb-3 uppercase tracking-widest bg-black text-white px-2 py-1 w-fit shadow-[4px_4px_0px_0px_rgba(37,99,235,1)]">[ ACADEMIC_HUB ]</div>
          <h1 class="text-5xl md:text-7xl font-black uppercase tracking-tighter">
            ОСВІТНІЙ <br><span class="text-white bg-black px-3 mt-2 inline-block shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">ПРОЦЕС</span>
          </h1>
        </div>
      </div>

      <!-- ГОЛОВНІ СТОРІНКИ (блоки) -->
      <section class="feat" aria-labelledby="feat-title">
        <div class="feat__head">
          <p class="feat__kicker font-pixel">// MAIN_PAGES</p>
          <h2 id="feat-title" class="feat__title">Головне</h2>
          <p class="feat__sub">Основні сторінки освітнього процесу: обери потрібну.</p>
        </div>

        <div class="feat__grid">
          <NuxtLink
            v-for="(f, i) in featured"
            :key="f.to"
            :to="f.to"
            class="fc"
            :style="{ '--c': f.color, '--on': f.on }"
          >
            <span class="fc__n font-pixel" aria-hidden="true">0{{ i + 1 }}</span>
            <span class="fc__icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square" stroke-linejoin="miter"><path :d="f.icon" /></svg>
            </span>
            <span class="fc__tag font-pixel">[ {{ f.tag }} ]</span>
            <h3 class="fc__t">{{ f.title }}</h3>
            <p class="fc__p">{{ f.text }}</p>
            <span class="fc__go font-pixel">Відкрити <i aria-hidden="true">→</i></span>
          </NuxtLink>
        </div>
      </section>

      <!-- Розділювач -->
      <div class="sep" role="separator">
        <span class="sep__line"></span>
        <span class="sep__txt font-pixel">// ДОКУМЕНТИ ТА ПОСИЛАННЯ</span>
        <span class="sep__line"></span>
      </div>

      <!-- СТАТУС ЗАВАНТАЖЕННЯ -->
      <div v-if="pending" class="w-full border-4 border-dashed border-gray-400 py-32 flex flex-col items-center justify-center text-gray-500 bg-white mb-12">
        <div class="font-pixel text-3xl mb-4 animate-pulse text-blue-600">[ MOUNTING_FILE_SYSTEM... ]</div>
      </div>

      <div v-else-if="error" class="w-full border-4 border-black py-32 flex flex-col items-center justify-center text-red-500 bg-red-100 shadow-[12px_12px_0px_0px_rgba(0,0,0,1)] mb-12">
        <div class="font-pixel text-3xl mb-4">[ CONNECTION_FAILED ]</div>
        <p class="font-bold text-xl text-black">Не вдалося завантажити академічну базу даних.</p>
      </div>

      <div v-else-if="!sections || sections.length === 0" class="border-4 border-dashed border-gray-400 p-12 text-center bg-white">
        <span class="font-pixel text-gray-400 text-xl">[ DIRECTORY_EMPTY ]</span>
        <p class="font-mono text-gray-500 mt-2">Розділи освітнього процесу ще не створені.</p>
      </div>

      <!-- ОСНОВНИЙ КОНТЕНТ (САЙДБАР + ДАНІ) -->
      <div v-else class="flex flex-col lg:flex-row gap-10">
        
        <!-- САЙДБАР (Навігація по розділах) -->
        <div class="w-full lg:w-1/4 shrink-0 flex flex-col gap-4">
          <div class="font-pixel text-xs text-gray-500 uppercase border-b-4 border-black pb-2 mb-2">
            // DIRECTORIES
          </div>
          
          <button 
            v-for="section in sections" 
            :key="section.id"
            @click="activeSectionId = section.id"
            class="text-left font-bold uppercase p-4 border-4 border-black transition-all cursor-pointer flex justify-between items-center group"
            :class="activeSectionId === section.id ? 'bg-black text-white shadow-none translate-x-1 translate-y-1' : 'bg-white text-black shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:bg-yellow-400'"
          >
            <span class="truncate pr-4">{{ section.title }}</span>
            <span v-if="activeSectionId === section.id" class="font-pixel text-yellow-400 text-sm animate-pulse">●</span>
            <span v-else class="font-pixel text-gray-400 text-sm group-hover:text-black">></span>
          </button>
        </div>

        <!-- ПРАВА ПАНЕЛЬ (Вміст вибраного розділу) -->
        <div class="w-full lg:w-3/4">
          <Transition name="fade-slide" mode="out-in">
            <div :key="activeSectionId" v-if="activeSection" class="flex flex-col gap-10">
              
              <!-- Заголовок та Інтро розділу -->
              <div class="bg-white border-4 border-black p-8 shadow-[8px_8px_0px_0px_rgba(37,99,235,1)] relative">
                <div class="absolute -top-4 -right-4 bg-yellow-400 text-black font-pixel text-[10px] px-3 py-1 border-2 border-black shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] z-10">
                  ID: {{ activeSection.slug }}
                </div>
                <h2 class="text-3xl md:text-5xl font-black uppercase tracking-tighter mb-4 text-black border-b-4 border-dashed border-gray-300 pb-4">
                  {{ activeSection.title }}
                </h2>
                <div v-if="activeSection.intro" class="prose prose-lg max-w-none font-mono font-medium text-gray-700 leading-relaxed whitespace-pre-line">
                  {{ activeSection.intro }}
                </div>
              </div>

              <!-- ГРУПИ ПОСИЛАНЬ -->
              <div v-if="activeSection.groups && activeSection.groups.length > 0" class="flex flex-col gap-12">
                <div v-for="group in activeSection.groups" :key="group.id" class="border-t-8 border-black pt-8">
                  
                  <h3 v-if="group.title" class="text-2xl font-black uppercase mb-6 flex items-center gap-4">
                    <span class="text-blue-600 font-pixel">#</span>
                    {{ group.title }}
                  </h3>
                  
                  <!-- СІТКА ПОСИЛАНЬ -->
                  <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <component
                      :is="link.href ? 'a' : 'div'"
                      v-for="link in group.links"
                      :key="link.id"
                      v-bind="link.href ? { href: link.href, target: '_blank', rel: 'noopener' } : { title: 'Посилання ще не додано' }"
                      class="flex flex-col bg-white border-4 border-black p-5 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:-translate-y-1 hover:translate-x-1 hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] transition-all group"
                      :class="{ 'opacity-60': !link.href }"
                    >
                      <div class="flex justify-between items-start mb-3 gap-4">
                        <div class="font-pixel text-[10px] text-white bg-black px-2 py-1 uppercase border border-black group-hover:bg-blue-600 transition-colors">
                          FILE_LINK
                        </div>
                        <div v-if="link.note" class="font-pixel text-[8px] text-black bg-yellow-300 px-2 py-1 border border-black uppercase text-right">
                          {{ link.note }}
                        </div>
                      </div>
                      
                      <h4 class="text-lg font-bold uppercase leading-tight group-hover:text-blue-600 transition-colors">
                        {{ link.title }}
                      </h4>
                      
                      <div class="mt-auto pt-4 flex justify-end">
                        <svg class="w-6 h-6 text-black group-hover:text-blue-600 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="square" stroke-linejoin="miter" stroke-width="3" d="M14 5l7 7m0 0l-7 7m7-7H3"></path></svg>
                      </div>
                    </component>
                  </div>
                  
                </div>
              </div>

              <!-- ГАЛЕРЕЯ / СЕРТИФІКАТИ -->
              <div v-if="activeSection.images && activeSection.images.length > 0" class="border-t-8 border-black pt-8">
                <h3 class="text-2xl font-black uppercase mb-6 flex items-center gap-4">
                  <span class="text-yellow-500 font-pixel">@</span>
                  ДОКУМЕНТИ ТА СЕРТИФІКАТИ
                </h3>
                <div class="gal">
                  <button
                    v-for="(img, i) in activeSection.images"
                    :key="img.id"
                    type="button"
                    class="gal__item"
                    :aria-label="`Відкрити: ${img.caption || 'документ'}`"
                    @click="openImageModal(i)"
                  >
                    <span class="gal__frame">
                      <img :src="imgUrl(img.image)" :alt="img.caption || 'Документ'" loading="lazy" />
                      <span class="gal__no font-pixel">DOC_0{{ i + 1 }}</span>
                      <span class="gal__zoom" aria-hidden="true"><b class="font-pixel">Дивитись ⤢</b></span>
                    </span>
                    <span class="gal__cap font-pixel">{{ img.caption || 'Документ' }}</span>
                  </button>
                </div>
              </div>

            </div>
          </Transition>
        </div>

      </div>
    </div>

    <!-- ПЕРЕГЛЯД ДОКУМЕНТІВ (lightbox) -->
    <Teleport to="body">
      <Transition name="lb">
        <div v-if="currentImage" class="lb" role="dialog" aria-modal="true" aria-label="Перегляд документа" @click.self="closeImageModal">
          <div class="lb__box">
            <header class="lb__bar">
              <span class="lb__cnt font-pixel">DOC {{ imageIndex + 1 }} / {{ images.length }}</span>
              <div class="lb__actions">
                <a :href="imgUrl(currentImage.image)" target="_blank" rel="noopener" class="lb__btn lb__btn--open font-pixel">Оригінал ↗</a>
                <button type="button" class="lb__btn lb__btn--x font-pixel" aria-label="Закрити" @click="closeImageModal">X</button>
              </div>
            </header>

            <div class="lb__stage">
              <button v-if="images.length > 1" type="button" class="lb__nav lb__nav--l font-pixel" aria-label="Попередній документ" @click="stepImage(-1)">←</button>
              <img :src="imgUrl(currentImage.image)" :alt="currentImage.caption || 'Документ'" class="lb__img" />
              <button v-if="images.length > 1" type="button" class="lb__nav lb__nav--r font-pixel" aria-label="Наступний документ" @click="stepImage(1)">→</button>
            </div>

            <footer v-if="currentImage.caption" class="lb__cap">{{ currentImage.caption }}</footer>
          </div>
        </div>
      </Transition>
    </Teleport>

  </div>
</template>

<script setup>
import { ref, computed, watch, onMounted, onBeforeUnmount } from 'vue';

// Ендпоїнт із бекенду (див. urls.py: path('education/', ...))
const { data: sections, pending, error } = await useFetch('https://mit-site-3t9h.vercel.app/api/v1/education/');

// ===== Головні сторінки (блоки зверху) =====
// Якщо файли лежать не в корені pages/, змін значення `to`.
const featured = [
  {
    to: '/program-description',
    tag: 'БАКАЛАВРАТ',
    title: 'Освітня програма (бакалавр)',
    text: 'Освітньо-професійна програма першого (бакалаврського) рівня.',
    color: '#2563eb', on: '#ffffff',
    icon: 'M3 9l9-5 9 5-9 5-9-5zM7 11.5V16c0 1 2.2 2.5 5 2.5s5-1.5 5-2.5v-4.5',
  },
  {
    to: '/master-program',
    tag: 'МАГІСТРАТУРА',
    title: 'Освітня програма (магістр)',
    text: 'Освітньо-професійна програма другого (магістерського) рівня.',
    color: '#dc2626', on: '#ffffff',
    icon: 'M12 3l9 5-9 5-9-5 9-5zM3 13l9 5 9-5',
  },
  {
    to: '/bachelor-program',
    tag: 'ОПИС ПРОГРАМИ',
    title: 'Опис освітньої програми',
    text: 'Опис програм, навчальні плани та структура підготовки.',
    color: '#facc15', on: '#000000',
    icon: 'M6 3h9l4 4v14H6V3zM14 3v5h5M9 13h7M9 17h7',
  },
  {
    to: '/syllabi',
    tag: 'АРХІВ ДОКУМЕНТІВ',
    title: 'Силабуси та РПНД',
    text: 'Робочі програми дисциплін, курсове проєктування та практика.',
    color: '#000000', on: '#ffffff',
    icon: 'M9 6h11M9 12h11M9 18h11M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2',
  },
];

// Стан активного розділу
const activeSectionId = ref(null);

// Коли дані завантажилися, робимо перший розділ активним за замовчуванням
watch(sections, (newSections) => {
  if (newSections && newSections.length > 0 && !activeSectionId.value) {
    activeSectionId.value = newSections[0].id;
  }
}, { immediate: true });

// Обчислюємо активний розділ
const activeSection = computed(() => {
  if (!sections.value) return null;
  return sections.value.find(s => s.id === activeSectionId.value) || null;
});

// Перегляд документів (сертифікатів) з навігацією
const imgUrl = (p) => (p.startsWith('http') ? p : `https://mit-site-3t9h.vercel.app${p}`);
const images = computed(() => activeSection.value?.images ?? []);
const imageIndex = ref(null);
const currentImage = computed(() => (imageIndex.value === null ? null : images.value[imageIndex.value] ?? null));

const openImageModal = (i) => {
  imageIndex.value = i;
  if (import.meta.client) document.body.style.overflow = 'hidden';
};

const closeImageModal = () => {
  imageIndex.value = null;
  if (import.meta.client) document.body.style.overflow = '';
};

const stepImage = (d) => {
  const n = images.value.length;
  if (n) imageIndex.value = (imageIndex.value + d + n) % n;
};

// Клавіатура: Esc — закрити, ← → — гортати
const onKey = (e) => {
  if (imageIndex.value === null) return;
  if (e.key === 'Escape') closeImageModal();
  if (e.key === 'ArrowRight') stepImage(1);
  if (e.key === 'ArrowLeft') stepImage(-1);
};
onMounted(() => window.addEventListener('keydown', onKey));
onBeforeUnmount(() => {
  window.removeEventListener('keydown', onKey);
  if (import.meta.client) document.body.style.overflow = '';
});
</script>

<style scoped>
/* ===== Блоки головних сторінок ===== */
.feat { margin-bottom: 3.5rem; }
.feat__head { margin-bottom: 2rem; }
.feat__kicker { margin: 0 0 .4rem; font-size: .75rem; color: #52525b; text-transform: uppercase; letter-spacing: .1em; }
.feat__title { margin: 0; font-size: clamp(2rem, 5vw, 3.4rem); font-weight: 900; line-height: 1; text-transform: uppercase; letter-spacing: -.03em; }
.feat__sub { margin: .6rem 0 0; color: #52525b; font-weight: 600; }

.feat__grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.75rem; }

.fc { position: relative; display: flex; flex-direction: column; gap: .8rem; min-height: 320px; padding: 1.5rem; overflow: hidden;
  background: #fff; color: #000; border: 4px solid #000; box-shadow: 8px 8px 0 var(--c); text-decoration: none;
  transition: transform .18s, box-shadow .18s, background .18s, color .18s; }
.fc:hover, .fc:focus-visible { transform: translate(-4px, -4px); box-shadow: 12px 12px 0 #000; background: var(--c); color: var(--on); }
.fc:focus-visible { outline: 4px solid #facc15; outline-offset: 3px; }
.fc:active { transform: translate(4px, 4px); box-shadow: 0 0 0 #000; }

.fc__n { position: absolute; top: .4rem; right: 1rem; font-size: 4.5rem; line-height: 1; opacity: .08; pointer-events: none; transition: opacity .18s; }
.fc:hover .fc__n { opacity: .25; }

.fc__icon { display: inline-flex; align-items: center; justify-content: center; width: 3.6rem; height: 3.6rem; margin-bottom: .4rem;
  background: var(--c); color: var(--on); border: 4px solid #000; box-shadow: 4px 4px 0 #000; transition: background .18s, color .18s; }
.fc__icon svg { width: 60%; height: 60%; }
.fc:hover .fc__icon { background: #fff; color: #000; }

.fc__tag { font-size: .7rem; text-transform: uppercase; letter-spacing: .08em; opacity: .7; }
.fc__t { margin: 0; font-size: clamp(1.3rem, 2vw, 1.7rem); font-weight: 900; line-height: 1.05; text-transform: uppercase; letter-spacing: -.02em; }
.fc__p { margin: 0; font-size: .9rem; font-weight: 500; line-height: 1.5; opacity: .85; }
.fc__go { margin-top: auto; display: inline-flex; align-items: center; gap: .6rem; padding-top: 1rem; border-top: 3px dashed currentColor; font-size: .8rem; text-transform: uppercase; }
.fc__go i { font-style: normal; transition: transform .18s; }
.fc:hover .fc__go i { transform: translateX(8px); }

/* Розділювач */
.sep { display: flex; align-items: center; gap: 1rem; margin: 0 0 3rem; }
.sep__line { flex: 1; height: 8px; background: #000; }
.sep__txt { flex-shrink: 0; padding: .4rem .9rem; background: #000; color: #fff; font-size: .75rem; letter-spacing: .1em; }

@media (max-width: 1200px) { .feat__grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 640px) {
  .feat__grid { grid-template-columns: 1fr; gap: 1.5rem; }
  .fc { min-height: 0; box-shadow: 6px 6px 0 var(--c); }
  .sep__txt { font-size: .65rem; }
}
@media (prefers-reduced-motion: reduce) { .fc, .fc * { transition-duration: .01ms !important; } }

/* ===== Галерея документів ===== */
.gal { display: grid; grid-template-columns: repeat(auto-fill, minmax(min(100%, 300px), 1fr)); gap: 1.75rem; }
.gal__item { display: flex; flex-direction: column; padding: 0; font: inherit; color: inherit; text-align: left; cursor: zoom-in; background: #fff;
  border: 4px solid #000; box-shadow: 6px 6px 0 #000; transition: transform .18s, box-shadow .18s; }
.gal__item:hover, .gal__item:focus-visible { transform: translate(-3px, -3px); box-shadow: 10px 10px 0 #2563eb; }
.gal__item:focus-visible { outline: 4px solid #facc15; outline-offset: 3px; }
.gal__frame { position: relative; display: block; aspect-ratio: 4 / 3; overflow: hidden; border-bottom: 4px solid #000;
  background: repeating-linear-gradient(45deg, #f4f4f0 0 10px, #ebebe4 10px 20px); }
.gal__frame img { display: block; width: 100%; height: 100%; padding: .75rem; object-fit: contain; transition: transform .3s; }
.gal__item:hover .gal__frame img { transform: scale(1.04); }
.gal__no { position: absolute; top: .6rem; left: .6rem; padding: .2rem .5rem; background: #000; color: #fff; font-size: .65rem; letter-spacing: .08em; }
.gal__zoom { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; background: rgba(0, 0, 0, .55); opacity: 0; transition: opacity .18s; }
.gal__zoom b { padding: .5rem .9rem; background: #facc15; color: #000; border: 3px solid #000; font-size: .75rem; text-transform: uppercase; }
.gal__item:hover .gal__zoom, .gal__item:focus-visible .gal__zoom { opacity: 1; }
.gal__cap { display: block; padding: .8rem 1rem; background: #000; color: #fff; font-size: .75rem; letter-spacing: .04em; text-transform: uppercase; }

/* ===== Перегляд документа (lightbox) ===== */
.lb { position: fixed; inset: 0; z-index: 9999; display: flex; align-items: center; justify-content: center; padding: clamp(.5rem, 2.5vw, 1.5rem);
  background: rgba(0, 0, 0, .92); backdrop-filter: blur(6px); }
.lb__box { display: flex; flex-direction: column; width: min(1100px, 100%); max-height: 100%; overflow: hidden; background: #f4f4f0; border: 4px solid #000; box-shadow: 12px 12px 0 #facc15; }
.lb__bar { display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-shrink: 0; padding: .7rem .9rem; background: #000; color: #facc15; }
.lb__cnt { font-size: .75rem; letter-spacing: .1em; }
.lb__actions { display: flex; gap: .6rem; }
.lb__btn { display: inline-flex; align-items: center; justify-content: center; min-width: 2.4rem; min-height: 2.4rem; padding: .3rem .8rem; background: #fff; color: #000; border: 3px solid #fff;
  font-size: .7rem; text-transform: uppercase; text-decoration: none; cursor: pointer; transition: background .12s, color .12s, border-color .12s; }
.lb__btn:hover { background: #facc15; border-color: #facc15; }
.lb__btn--x { background: #dc2626; color: #fff; border-color: #dc2626; font-size: 1rem; }
.lb__btn--x:hover { background: #fff; color: #dc2626; border-color: #fff; }
.lb__btn:focus-visible, .lb__nav:focus-visible { outline: 4px solid #facc15; outline-offset: 2px; }
.lb__stage { position: relative; display: flex; align-items: center; justify-content: center; flex: 1; min-height: 0; padding: clamp(.5rem, 2vw, 1.25rem);
  background: repeating-linear-gradient(45deg, #e4e4e7 0 12px, #dcdce0 12px 24px); }
.lb__img { display: block; max-width: 100%; max-height: calc(100vh - 12rem); object-fit: contain; background: #fff; border: 3px solid #000; box-shadow: 6px 6px 0 #000; }
.lb__nav { position: absolute; top: 50%; translate: 0 -50%; z-index: 2; width: 3rem; height: 3rem; background: #fff; border: 4px solid #000; box-shadow: 3px 3px 0 #000; font-size: 1.3rem; cursor: pointer; transition: background .12s; }
.lb__nav:hover { background: #facc15; }
.lb__nav--l { left: .75rem; }
.lb__nav--r { right: .75rem; }
.lb__cap { flex-shrink: 0; padding: .8rem 1rem; background: #000; color: #fff; text-align: center; font-weight: 800; text-transform: uppercase; font-size: clamp(.8rem, 1.6vw, 1rem); }

.lb-enter-active, .lb-leave-active { transition: opacity .2s; }
.lb-enter-active .lb__box, .lb-leave-active .lb__box { transition: transform .25s cubic-bezier(.175, .885, .32, 1.275); }
.lb-enter-from, .lb-leave-to { opacity: 0; }
.lb-enter-from .lb__box, .lb-leave-to .lb__box { transform: scale(.95) translateY(16px); }

@media (max-width: 640px) {
  .lb__btn--open { display: none; }
  .lb__nav { width: 2.4rem; height: 2.4rem; font-size: 1rem; }
}
@media (prefers-reduced-motion: reduce) { .gal__item, .gal__item *, .lb *, .lb { transition-duration: .01ms !important; } }

/* Анімація перемикання вкладок */
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 0.3s ease;
}
.fade-slide-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(-20px);
}

</style>
