<template>
  <main class="page">
    <div class="grid-bg" aria-hidden="true"></div>

    <div class="wrap">
      <!-- HEADER -->
      <header class="head">
        <div>
          <p class="tag font-pixel">[ ЕФІР КАФЕДРИ ]</p>
          <h1 class="title">Системні<br /><span class="title__mark">оновлення</span></h1>
        </div>
        <NuxtLink to="/" class="btn btn--light font-pixel">← На головну</NuxtLink>
      </header>

      <!-- LIVE стрічка -->
      <div v-if="all.length" class="live" aria-hidden="true">
        <span class="live__badge font-pixel"><i></i> LIVE</span>
        <div class="live__win">
          <div class="live__track">
            <span v-for="(n, i) in tickerItems" :key="i"><b>&gt;&gt;</b> {{ n.title }}</span>
          </div>
        </div>
      </div>

      <!-- ТУЛБАР -->
      <div v-if="all.length" class="toolbar">
        <label class="search">
          <span class="sr">Пошук новин</span>
          <input v-model.trim="query" type="search" placeholder="Пошук за назвою чи текстом…" />
        </label>
        <div class="seg" role="group" aria-label="Сортування">
          <button type="button" :class="{ on: sort === 'new' }" :aria-pressed="sort === 'new'" @click="sort = 'new'">Спочатку нові</button>
          <button type="button" :class="{ on: sort === 'old' }" :aria-pressed="sort === 'old'" @click="sort = 'old'">Спочатку старі</button>
        </div>
        <p class="count font-pixel" aria-live="polite">{{ list.length }} з {{ all.length }}</p>
      </div>

      <!-- СТАНИ -->
      <div v-if="pending" class="grid">
        <div v-for="n in 3" :key="n" class="skeleton"></div>
      </div>

      <div v-else-if="error" class="state state--err">
        <p class="font-pixel state__t">[ SIGNAL_LOST ]</p>
        <p>Не вдалося з'єднатися з сервером новин. Перевір, чи запущено Django на порту 8000.</p>
        <button type="button" class="btn btn--dark font-pixel" @click="refresh()">Спробувати ще раз</button>
      </div>

      <div v-else-if="!all.length" class="state">
        <p class="font-pixel state__t">[ NO_TRANSMISSIONS ]</p>
        <p>Новин поки немає. Додай першу в панелі адміністратора.</p>
      </div>

      <div v-else-if="!list.length" class="state">
        <p class="font-pixel state__t">[ 0 РЕЗУЛЬТАТІВ ]</p>
        <p>За запитом «{{ query }}» нічого не знайдено.</p>
        <button type="button" class="btn btn--dark font-pixel" @click="query = ''">Скинути пошук</button>
      </div>

      <template v-else>
        <!-- ГОЛОВНА -->
        <article v-if="featured" class="hero" tabindex="0" role="button" :aria-label="`Відкрити: ${featured.title}`" @click="open(featured)" @keydown.enter="open(featured)">
          <span class="badge font-pixel">{{ featured.is_pinned ? '★ Закріплено' : '#Головна' }}</span>
          <div class="hero__img">
            <img v-if="photosOf(featured)[0]" :src="photosOf(featured)[0]" :alt="featured.title" />
            <div v-else class="noimg font-pixel">[ NO_PHOTO ]</div>
            <span v-if="photosOf(featured).length > 1" class="more font-pixel">+{{ photosOf(featured).length - 1 }} фото</span>
          </div>
          <div class="hero__txt">
            <p class="meta font-pixel">{{ fmt(featured) }} · {{ readTime(featured) }} хв читання</p>
            <h2>{{ featured.title }}</h2>
            <p class="excerpt">{{ featured.content }}</p>
            <span class="btn btn--dark font-pixel">Читати повністю</span>
          </div>
        </article>

        <!-- СІТКА -->
        <div v-if="rest.length" class="grid">
          <article v-for="n in rest" :key="n.id" class="card" tabindex="0" role="button" :aria-label="`Відкрити: ${n.title}`" @click="open(n)" @keydown.enter="open(n)">
            <div class="card__img">
              <img v-if="photosOf(n)[0]" :src="photosOf(n)[0]" :alt="n.title" loading="lazy" />
              <div v-else class="noimg font-pixel">[ NO_PHOTO ]</div>
              <span class="stamp font-pixel">{{ fmt(n, true) }}</span>
              <span v-if="n.is_pinned" class="pin font-pixel">★</span>
              <span v-if="photosOf(n).length > 1" class="more font-pixel">{{ photosOf(n).length }} фото</span>
            </div>
            <div class="card__body">
              <h3>{{ n.title }}</h3>
              <p>{{ n.content }}</p>
              <div class="card__foot font-pixel"><span>{{ readTime(n) }} хв читання</span><span class="arrow">→</span></div>
            </div>
          </article>
        </div>
      </template>
    </div>

    <!-- МОДАЛКА -->
    <Teleport to="body">
      <Transition name="modal">
        <div v-if="selected" class="modal" role="dialog" aria-modal="true" :aria-label="selected.title">
          <div class="modal__bg" @click="close"></div>
          <button type="button" ref="closeBtn" class="modal__x font-pixel" aria-label="Закрити" @click="close">X</button>

          <div class="modal__box">
            <div class="modal__bar font-pixel">
              <span><i></i> ПОВІДОМЛЕННЯ</span>
              <span>{{ fmt(selected) }}</span>
            </div>
            <div class="modal__scroll">
              <div v-if="gallery.length" class="gal">
                <img :src="gallery[idx]" :alt="`${selected.title} — фото ${idx + 1}`" />
                <template v-if="gallery.length > 1">
                  <button type="button" class="gal__b gal__b--l font-pixel" aria-label="Попереднє фото" @click="step(-1)">←</button>
                  <button type="button" class="gal__b gal__b--r font-pixel" aria-label="Наступне фото" @click="step(1)">→</button>
                  <span class="gal__n font-pixel">{{ idx + 1 }} / {{ gallery.length }}</span>
                </template>
              </div>
              <div v-if="gallery.length > 1" class="thumbs">
                <button v-for="(g, i) in gallery" :key="i" type="button" :class="{ on: i === idx }" :aria-label="`Фото ${i + 1}`" @click="idx = i">
                  <img :src="g" alt="" />
                </button>
              </div>
              <div class="modal__txt">
                <p v-if="selected.is_pinned" class="badge badge--in font-pixel">★ Закріплено</p>
                <h2>{{ selected.title }}</h2>
                <p class="meta font-pixel">{{ readTime(selected) }} хв читання</p>
                <div class="full">{{ selected.content }}</div>
              </div>
            </div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </main>
</template>

<script setup>
import { ref, computed, watch, nextTick, onMounted, onBeforeUnmount } from 'vue';

const API = 'http://127.0.0.1:8000';
const { data, pending, error, refresh } = await useFetch(`${API}/api/v1/news/`, { default: () => [] });

const all = computed(() => (Array.isArray(data.value) ? data.value : (data.value?.results ?? [])));
const query = ref('');
const sort = ref('new');

const abs = (p) => (!p ? '' : p.startsWith('http') ? p : `${API}${p}`);
const photosOf = (n) => {
  const arr = (n.images || []).map((i) => abs(i.image)).filter(Boolean);
  if (!arr.length && n.photo) arr.push(abs(n.photo));
  return arr;
};
const dateOf = (n) => n.date_posted || n.created_at || n.date;
const fmt = (n, short = false) => {
  const v = dateOf(n);
  const d = v ? new Date(v) : null;
  if (!d || isNaN(d)) return '—';
  return d.toLocaleDateString('uk-UA', short ? { day: '2-digit', month: '2-digit', year: '2-digit' } : { day: 'numeric', month: 'long', year: 'numeric' });
};
const readTime = (n) => Math.max(1, Math.ceil((n.content || '').split(/\s+/).length / 180));

const list = computed(() => {
  const q = query.value.toLowerCase();
  const items = all.value.filter((n) => !q || `${n.title} ${n.content}`.toLowerCase().includes(q));
  const ts = (n) => new Date(dateOf(n) || 0).getTime();
  return items.sort((a, b) => (sort.value === 'new'
    ? (Number(!!b.is_pinned) - Number(!!a.is_pinned)) || ts(b) - ts(a)
    : ts(a) - ts(b)));
});
const featured = computed(() => (!query.value && list.value.length ? list.value[0] : null));
const rest = computed(() => (featured.value ? list.value.slice(1) : list.value));

const tickerItems = computed(() => {
  const l = all.value.slice(0, 5);
  return [...l, ...l, ...l, ...l];
});

// Модалка + галерея
const selected = ref(null);
const idx = ref(0);
const closeBtn = ref(null);
const gallery = computed(() => (selected.value ? photosOf(selected.value) : []));

const open = async (n) => {
  selected.value = n;
  idx.value = 0;
  document.body.style.overflow = 'hidden';
  await nextTick();
  closeBtn.value?.focus();
};
const close = () => { selected.value = null; document.body.style.overflow = ''; };
const step = (d) => { const l = gallery.value.length; idx.value = (idx.value + d + l) % l; };

const onKey = (e) => {
  if (!selected.value) return;
  if (e.key === 'Escape') close();
  if (e.key === 'ArrowRight') step(1);
  if (e.key === 'ArrowLeft') step(-1);
};
onMounted(() => window.addEventListener('keydown', onKey));
onBeforeUnmount(() => { window.removeEventListener('keydown', onKey); document.body.style.overflow = ''; });
watch(selected, (v) => { if (!v) idx.value = 0; });
</script>

<style scoped>
.page { --ink: #000; --paper: #f4f4f0; --or: #f97316; --mute: #52525b;
  position: relative; overflow: hidden; min-height: 100vh; padding: clamp(7rem, 12vw, 10rem) 0 6rem;
  background: var(--paper); color: var(--ink); font-family: ui-monospace, 'Courier New', monospace; line-height: 1.5; }
.page *, .page *::before, .page *::after { box-sizing: border-box; }
.page ::selection { background: var(--or); color: #000; }
.grid-bg { position: absolute; inset: 0; opacity: .08; pointer-events: none;
  background: linear-gradient(#000 1px, transparent 1px) 0 0 / 50px 50px, linear-gradient(90deg, #000 1px, transparent 1px) 0 0 / 50px 50px; }
.wrap { position: relative; z-index: 1; max-width: 1400px; margin: 0 auto; padding: 0 clamp(1rem, 4vw, 2rem); }
.sr { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }

.head { display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 1.5rem; padding-bottom: 2rem; margin-bottom: 2rem; border-bottom: 8px solid var(--ink); }
.tag { display: inline-block; margin: 0 0 .75rem; padding: .25rem .6rem; background: var(--ink); color: #fff; font-size: .9rem; letter-spacing: .1em; box-shadow: 4px 4px 0 var(--or); }
.title { margin: 0; font-size: clamp(2.6rem, 7vw, 5.5rem); font-weight: 900; line-height: .95; letter-spacing: -.04em; text-transform: uppercase; }
.title__mark { display: inline-block; margin-top: .5rem; padding: 0 .3em; background: var(--ink); color: #fff; box-shadow: 8px 8px 0 var(--or); }

.btn { display: inline-flex; align-items: center; justify-content: center; padding: .85rem 1.4rem; border: 4px solid var(--ink); font-size: .85rem; text-transform: uppercase; text-decoration: none; cursor: pointer;
  box-shadow: 4px 4px 0 var(--ink); transition: transform .12s, box-shadow .12s, background .12s; }
.btn--light { background: #fff; color: var(--ink); }
.btn--dark { background: var(--ink); color: #fff; }
.btn:hover { background: var(--or); color: #000; transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--ink); }
.btn:active { transform: translate(4px, 4px); box-shadow: none; }
:where(.btn, .seg button, .search input, .hero, .card, .gal__b, .thumbs button, .modal__x):focus-visible { outline: 4px solid #c026d3; outline-offset: 3px; }

/* Live */
.live { display: flex; margin-bottom: 2rem; background: var(--ink); color: var(--or); border: 4px solid var(--ink); box-shadow: 8px 8px 0 var(--or); overflow: hidden; }
.live__badge { flex-shrink: 0; display: flex; align-items: center; gap: .5rem; padding: .7rem 1rem; background: var(--or); color: #000; border-right: 4px solid var(--ink); font-size: .75rem; }
.live__badge i, .modal__bar i { width: 8px; height: 8px; border-radius: 50%; background: currentColor; animation: pulse 1.4s ease-in-out infinite; }
.live__win { flex: 1; overflow: hidden; display: flex; align-items: center; }
.live__track { display: flex; gap: 2rem; width: max-content; padding: .5rem 1rem; white-space: nowrap; font-weight: 700; animation: tick 45s linear infinite; }
.live__track b { color: #fff; opacity: .5; margin-right: .4rem; }
.live:hover .live__track { animation-play-state: paused; }
@keyframes tick { to { transform: translateX(-50%); } }
@keyframes pulse { 50% { opacity: .25; } }

/* Toolbar */
.toolbar { display: flex; flex-wrap: wrap; align-items: center; gap: 1rem; margin-bottom: 2.5rem; }
.search { flex: 1 1 260px; }
.search input { width: 100%; padding: .85rem 1rem; border: 4px solid var(--ink); background: #fff; font: inherit; font-weight: 700; box-shadow: 4px 4px 0 var(--ink); }
.search input:focus { background: #fff7ed; }
.seg { display: flex; border: 4px solid var(--ink); background: #fff; box-shadow: 4px 4px 0 var(--ink); }
.seg button { padding: .8rem 1rem; border: 0; background: transparent; font: inherit; font-weight: 800; font-size: .8rem; cursor: pointer; }
.seg button + button { border-left: 4px solid var(--ink); }
.seg button.on { background: var(--ink); color: var(--or); }
.seg button:not(.on):hover { background: var(--or); }
.count { margin: 0 0 0 auto; font-size: .8rem; color: var(--mute); }

/* Hero */
.hero { position: relative; display: grid; grid-template-columns: 1.5fr 1fr; margin-bottom: 3rem; background: #fff; border: 8px solid var(--ink); box-shadow: 16px 16px 0 var(--ink); cursor: pointer; overflow: hidden; transition: box-shadow .25s, border-color .25s; }
.hero:hover, .hero:focus-visible { border-color: var(--or); box-shadow: 8px 8px 0 var(--or); }
.hero__img { position: relative; min-height: 420px; background: #18181b; border-right: 8px solid var(--ink); overflow: hidden; }
.hero__img img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; transition: transform .6s; }
.hero:hover .hero__img img { transform: scale(1.04); }
.hero__txt { display: flex; flex-direction: column; justify-content: center; gap: 1.2rem; padding: clamp(1.5rem, 3vw, 2.5rem); background: var(--paper); }
.hero h2 { margin: 0; font-size: clamp(1.6rem, 3vw, 2.6rem); font-weight: 900; line-height: 1.05; letter-spacing: -.02em; text-transform: uppercase; }
.excerpt { margin: 0; color: #27272a; font-weight: 500; display: -webkit-box; -webkit-line-clamp: 5; -webkit-box-orient: vertical; overflow: hidden; }
.hero__txt .btn { align-self: flex-start; }
.hero:hover .hero__txt .btn { background: var(--or); color: #000; }
.meta { margin: 0; font-size: .75rem; color: var(--mute); text-transform: uppercase; }
.badge { position: absolute; top: 1rem; left: 1rem; z-index: 3; padding: .3rem .8rem; background: var(--or); border: 2px solid var(--ink); box-shadow: 2px 2px 0 var(--ink); font-size: .75rem; }
.badge--in { position: static; display: inline-block; margin: 0 0 1rem; }

.noimg { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; color: #52525b; font-size: 1rem;
  background: repeating-linear-gradient(45deg, #18181b 0 12px, #1f1f23 12px 24px); }
.more { position: absolute; right: .8rem; bottom: .8rem; z-index: 2; padding: .25rem .6rem; background: var(--ink); color: #fff; font-size: .7rem; border: 2px solid #fff; }

/* Grid */
.grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; }
.card { display: flex; flex-direction: column; background: #fff; border: 4px solid var(--ink); box-shadow: 8px 8px 0 var(--ink); cursor: pointer; transition: transform .2s, box-shadow .2s; }
.card:hover, .card:focus-visible { transform: translateY(-6px); box-shadow: 12px 12px 0 var(--or); }
.card__img { position: relative; aspect-ratio: 16 / 9; border-bottom: 4px solid var(--ink); background: #18181b; overflow: hidden; }
.card__img img { width: 100%; height: 100%; object-fit: cover; filter: grayscale(1) contrast(1.15); transition: filter .4s, transform .5s; }
.card:hover .card__img img, .card:focus-visible .card__img img { filter: none; transform: scale(1.05); }
.stamp { position: absolute; top: .5rem; left: .5rem; z-index: 2; padding: .2rem .5rem; background: var(--ink); color: #fff; font-size: .65rem; }
.pin { position: absolute; top: .5rem; right: .5rem; z-index: 2; padding: .2rem .5rem; background: var(--or); border: 2px solid var(--ink); font-size: .75rem; }
.card__body { display: flex; flex: 1; flex-direction: column; gap: .75rem; padding: 1.4rem; }
.card h3 { margin: 0; font-size: 1.35rem; font-weight: 900; line-height: 1.1; text-transform: uppercase; letter-spacing: -.01em; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.card:hover h3 { color: #c2410c; }
.card p { margin: 0; flex: 1; font-size: .9rem; color: #3f3f46; display: -webkit-box; -webkit-line-clamp: 3; -webkit-box-orient: vertical; overflow: hidden; }
.card__foot { display: flex; justify-content: space-between; padding-top: .8rem; border-top: 2px dashed #d4d4d8; font-size: .75rem; color: #c2410c; }
.arrow { transition: transform .2s; }
.card:hover .arrow { transform: translateX(6px); }

/* States */
.state { padding: 4rem 1.5rem; text-align: center; background: #fff; border: 4px dashed #a1a1aa; }
.state > * + * { margin-top: 1rem; }
.state__t { font-size: 1.6rem; color: var(--mute); }
.state--err { border: 4px solid var(--ink); background: #fee2e2; box-shadow: 12px 12px 0 var(--ink); }
.state--err .state__t { color: #b91c1c; }
.skeleton { aspect-ratio: 4 / 4.2; border: 4px solid var(--ink); background: linear-gradient(90deg, #e4e4e7 25%, #f4f4f5 50%, #e4e4e7 75%) 0 0 / 200% 100%; animation: shimmer 1.4s linear infinite; }
@keyframes shimmer { to { background-position: -200% 0; } }

/* Modal */
.modal { position: fixed; inset: 0; z-index: 9999; display: flex; align-items: center; justify-content: center; padding: clamp(.5rem, 3vw, 1.5rem); }
.modal__bg { position: absolute; inset: 0; background: rgba(0, 0, 0, .9); backdrop-filter: blur(6px); }
.modal__x { position: absolute; top: 1rem; right: 1rem; z-index: 3; width: 3rem; height: 3rem; background: #dc2626; color: #fff; border: 4px solid #000; box-shadow: 4px 4px 0 #fff; font-size: 1.1rem; cursor: pointer; }
.modal__x:hover { transform: translate(3px, 3px); box-shadow: none; }
.modal__box { position: relative; width: 100%; max-width: 900px; max-height: 90vh; display: flex; flex-direction: column; background: #fff; border: 8px solid #000; box-shadow: 16px 16px 0 var(--or); overflow: hidden; }
.modal__bar { display: flex; justify-content: space-between; gap: 1rem; padding: .8rem 1rem; background: #000; color: var(--or); font-size: .7rem; }
.modal__bar span:first-child { display: flex; align-items: center; gap: .6rem; }
.modal__bar span:last-child { color: #a1a1aa; }
.modal__scroll { overflow-y: auto; background: var(--paper); }
.gal { position: relative; background: #000; border-bottom: 8px solid #000; }
.gal img { display: block; width: 100%; max-height: 55vh; object-fit: contain; }
.gal__b { position: absolute; top: 50%; translate: 0 -50%; width: 3rem; height: 3rem; background: #fff; border: 4px solid #000; font-size: 1.2rem; cursor: pointer; box-shadow: 3px 3px 0 #000; }
.gal__b:hover { background: var(--or); }
.gal__b--l { left: .8rem; } .gal__b--r { right: .8rem; }
.gal__n { position: absolute; bottom: .8rem; left: .8rem; padding: .2rem .6rem; background: #000; color: #fff; font-size: .7rem; }
.thumbs { display: flex; gap: .6rem; padding: .8rem; overflow-x: auto; background: #18181b; }
.thumbs button { flex: 0 0 84px; height: 56px; padding: 0; border: 3px solid #3f3f46; background: #000; cursor: pointer; opacity: .6; }
.thumbs button.on { border-color: var(--or); opacity: 1; }
.thumbs img { width: 100%; height: 100%; object-fit: cover; display: block; }
.modal__txt { position: relative; padding: clamp(1.25rem, 4vw, 3rem); }
.modal__txt h2 { margin: 0 0 .75rem; font-size: clamp(1.6rem, 4vw, 2.8rem); font-weight: 900; line-height: 1.02; letter-spacing: -.03em; text-transform: uppercase; }
.full { margin-top: 1.5rem; padding-left: 1.2rem; border-left: 6px solid var(--or); max-width: 68ch; font-size: 1.05rem; font-weight: 500; line-height: 1.7; white-space: pre-line; color: #27272a; overflow-wrap: anywhere; }

.modal-enter-active, .modal-leave-active { transition: opacity .25s; }
.modal-enter-active .modal__box, .modal-leave-active .modal__box { transition: transform .3s cubic-bezier(.175, .885, .32, 1.275); }
.modal-enter-from, .modal-leave-to { opacity: 0; }
.modal-enter-from .modal__box, .modal-leave-to .modal__box { transform: scale(.95) translateY(20px); }

@media (max-width: 1000px) { .grid { grid-template-columns: 1fr 1fr; } .hero { grid-template-columns: 1fr; } .hero__img { min-height: 280px; border-right: 0; border-bottom: 8px solid var(--ink); } }
@media (max-width: 640px) { .grid { grid-template-columns: 1fr; } .count { margin-left: 0; } .seg { width: 100%; } .seg button { flex: 1; } .hero { box-shadow: 8px 8px 0 var(--ink); } }
@media (prefers-reduced-motion: reduce) { .live__track, .live__badge i, .modal__bar i, .skeleton { animation: none; } * { transition-duration: .01ms !important; } }
</style>