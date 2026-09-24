<template>
  <main class="page">
    <div class="dots" aria-hidden="true"></div>

    <!-- Біжучий рядок -->
    <div class="ticker" aria-hidden="true">
      <div class="ticker__track">
        <span v-for="n in 2" :key="n">
          CISCO ✦ HUAWEI ✦ MIKROTIK ✦ DOCKER ✦ KUBERNETES ✦ AWS ✦ КІБЕРБЕЗПЕКА ✦ G5 ✦
        </span>
      </div>
    </div>

    <div class="wrap">
      <!-- HEADER -->
      <header class="head reveal">
        <div>
          <p class="tag">[ НАБІР 2026 ]</p>
          <h1 class="title">
            Стань<br />
            <span class="title__mark">частиною мережі</span>
          </h1>
        </div>
        <NuxtLink to="/" class="btn btn--light">← На головну</NuxtLink>
      </header>

      <!-- ІНФО -->
      <section class="info">
        <article class="card reveal">
          <p class="label">Про факультет</p>
          <p class="lead">
            Шановні абітурієнти та батьки, запрошуємо Вас на навчання до Київського національного
            університету імені Тараса Шевченка.
          </p>
          <p class="lead"><mark>Факультет інформаційних технологій за рейтингом є на першому місці серед ІТ факультетів країни.</mark></p>
        </article>

        <article class="card card--dark reveal">
          <p class="label label--lime">Програма</p>
          <p class="body">
            Кафедра мережевих та інтернет технологій запрошує на навчання за освітніми програмами
            <strong>«Мережеві та інтернет технології»</strong> (спеціальність G5 «Електроніка, електронні
            комунікації, приладобудування та радіотехніка»).
          </p>
          <div class="seats">
            <div v-for="s in seats" :key="s.name" class="seat">
              <p class="seat__name">Бюджетні місця · {{ s.name }}</p>
              <p class="seat__num">{{ s.free }}<small>/{{ s.total }}</small></p>
              <div class="bar" role="img" :aria-label="`${s.free} з ${s.total} місць`">
                <span :style="{ width: (s.free / s.total) * 100 + '%' }"></span>
              </div>
            </div>
          </div>
        </article>

        <article class="card card--dark reveal perk">
          <p class="label label--lime">Бакалавр</p>
          <p class="body">
            Подаючи заявку з пріоритетом 1 або 2, вступник отримує <b class="hl">додаткові 2%</b> до конкурсного балу.
          </p>
        </article>
        <article class="card card--dark reveal perk">
          <p class="label label--lime">Магістр</p>
          <p class="body">
            Це <b class="hl">єдина магістерська програма на ФІТ</b>, для вступу на яку складається фахове вступне
            випробування замість ЄФВВ.
          </p>
        </article>
      </section>

      <!-- ГРА -->
      <section class="net reveal" aria-labelledby="net-title">
        <h2 id="net-title" class="h2 h2--center">Запусти мережу</h2>
        <p class="net__hint">
          Увімкни всі 4 вузли, щоб відкрити подачу заявки.
          <span class="net__count" aria-live="polite">{{ connectedCount }}/4</span>
        </p>

        <div class="progress" role="progressbar" aria-valuemin="0" aria-valuemax="4" :aria-valuenow="connectedCount">
          <span :style="{ width: connectedCount * 25 + '%' }"></span>
        </div>

        <div class="topo">
          <svg class="topo__lines" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">
            <line
              v-for="(n, i) in nodes" :key="n.id"
              :x1="n.x" :y1="n.y" x2="50" y2="50"
              :class="['line', { 'line--on': on[i] }]"
            />
          </svg>

          <div :class="['server', { 'server--on': allConnected }]">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="square" aria-hidden="true">
              <rect x="3" y="4" width="18" height="6" /><rect x="3" y="14" width="18" height="6" />
              <path d="M7 7h.01M7 17h.01" />
            </svg>
            <span>{{ allConnected ? 'ONLINE' : 'OFFLINE' }}</span>
          </div>

          <button
            v-for="(n, i) in nodes" :key="n.id"
            type="button"
            :class="['node', { 'node--on': on[i] }]"
            :style="{ left: n.x + '%', top: n.y + '%' }"
            :aria-pressed="on[i]"
            @click="toggle(i)"
          >
            <i class="node__led"></i>
            <span>{{ n.label }}</span>
          </button>
        </div>

        <!-- Термінал -->
        <div class="term" role="log" aria-live="polite">
          <p v-for="(l, i) in log" :key="l.k" :class="{ 'term__last': i === log.length - 1 }">
            <span>$</span> {{ l.t }}
          </p>
        </div>

        <div class="actions">
          <button type="button" class="btn btn--light" @click="setAll(true)" :disabled="allConnected">Увімкнути все</button>
          <button type="button" class="btn btn--light" @click="setAll(false)" :disabled="connectedCount === 0">Скинути</button>
        </div>

        <div class="cta">
          <Transition name="pop" mode="out-in">
            <a v-if="allConnected" key="go" href="https://vstup.edbo.gov.ua/" target="_blank" rel="noopener" class="btn btn--go">
              Подати заявку в ЄДБО ↗
            </a>
            <button v-else key="lock" type="button" class="btn btn--lock" aria-disabled="true">
              🔒 Ще {{ 4 - connectedCount }} {{ 4 - connectedCount === 1 ? 'вузол' : 'вузли' }} до доступу
            </button>
          </Transition>
        </div>
      </section>

      <!-- BENTO -->
      <section class="bento-sec">
        <h2 class="h2 h2--tag reveal">Що ти отримаєш</h2>

        <div class="bento">
          <article class="b b--wide b--white reveal">
            <span class="chip">Hard skills</span>
            <div>
              <h3>Реальне<br />залізо</h3>
              <p>Практика на обладнанні Cisco, Huawei, Mikrotik. Ніяких конспектів під диктовку.</p>
            </div>
          </article>

          <article class="b b--black reveal">
            <span class="emoji" aria-hidden="true">🔥</span>
            <div><h3>Кібер&shy;безпека</h3><p>Захист, атаки, реагування на інциденти.</p></div>
          </article>

          <article class="b b--white reveal b--career">
            <span class="chip chip--dark">Кар'єра</span>
            <div><h3>Офер ще до диплома</h3><p>Стажування й перші ролі вже під час навчання.</p></div>
            <span class="bg-sign" aria-hidden="true">$</span>
          </article>

          <article class="b b--wide b--code reveal">
            <pre class="code"><span>student@fit:~$</span> ./deploy_future.sh
<em>&gt; installing devops tools…</em></pre>
            <div>
              <h3>DevOps &amp; Cloud</h3>
              <p>Docker, Kubernetes, AWS. Вчимо будувати інфраструктуру, яка не падає.</p>
            </div>
          </article>

          <article class="b b--wide b--yellow reveal">
            <div class="inner">
              <h3>Ком'юніті</h3>
              <p>Олімпіади, хакатони, кіберспорт та нетворкінг. Наші студенти — це сім'я.</p>
            </div>
          </article>
        </div>
      </section>
    </div>
  </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';

const seats = [
  { name: 'Бакалавр', free: 29, total: 35 },
  { name: 'Магістр', free: 10, total: 15 },
];

const nodes = [
  { id: 'r', label: 'ROUTER_01', x: 20, y: 20, msg: 'ROUTER_01 підключено — маршрути знайдено' },
  { id: 's', label: 'SWITCH_A', x: 80, y: 20, msg: 'SWITCH_A підключено — VLAN піднято' },
  { id: 'g', label: 'GATEWAY', x: 20, y: 80, msg: 'GATEWAY підключено — вихід в інтернет є' },
  { id: 'f', label: 'FIREWALL', x: 80, y: 80, msg: 'FIREWALL підключено — правила активні' },
];

const on = ref([false, false, false, false]);
let key = 0;
const log = ref([{ k: key++, t: 'очікуємо підключення вузлів…' }]);

const push = (t) => {
  log.value = [...log.value, { k: key++, t }].slice(-4);
};

const connectedCount = computed(() => on.value.filter(Boolean).length);
const allConnected = computed(() => connectedCount.value === 4);

const toggle = (i) => {
  on.value[i] = !on.value[i];
  push(on.value[i] ? nodes[i].msg : `${nodes[i].label} відключено`);
  if (allConnected.value) push('мережа працює — заявку відкрито ✔');
};

const setAll = (v) => {
  on.value = on.value.map(() => v);
  push(v ? 'усі вузли підключено — мережа працює ✔' : 'мережу скинуто');
};

onMounted(() => {
  const els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) {
    els.forEach((e) => e.classList.add('is-in'));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { threshold: 0.12 });
  els.forEach((e) => io.observe(e));
});
</script>

<style scoped>
.page {
  --ink: #000; --paper: #f4f4f0; --lime: #a3e635; --pink: #c026d3; --yellow: #facc15; --mute: #52525b;
  position: relative; overflow: hidden; min-height: 100vh;
  padding: clamp(7rem, 12vw, 10rem) 0 8rem;
  background: var(--paper); color: var(--ink);
  font-family: ui-monospace, 'JetBrains Mono', 'Courier New', monospace;
  line-height: 1.5;
}
.page *, .page *::before, .page *::after { box-sizing: border-box; }
.page ::selection { background: var(--pink); color: #fff; }
.dots { position: absolute; inset: 0; opacity: .18; pointer-events: none;
  background: radial-gradient(#000 1px, transparent 1px) 0 0 / 24px 24px; }
.wrap { position: relative; z-index: 1; max-width: 1400px; margin: 0 auto; padding: 0 clamp(1rem, 4vw, 2rem); }

/* Ticker */
.ticker { position: absolute; top: clamp(4.5rem, 8vw, 6rem); left: 0; right: 0; z-index: 1; overflow: hidden;
  background: var(--ink); color: var(--lime); border-block: 3px solid var(--ink); padding: .35rem 0; font-size: .75rem; }
.ticker__track { display: flex; width: max-content; animation: scroll 40s linear infinite; }
.ticker__track span { white-space: pre; padding-right: 2rem; }
@keyframes scroll { to { transform: translateX(-50%); } }

/* Head */
.head { display: flex; flex-wrap: wrap; align-items: flex-end; justify-content: space-between; gap: 1.5rem;
  border-bottom: 8px solid var(--ink); padding: 2rem 0; margin-bottom: 3rem; }
.tag { display: inline-block; background: var(--ink); color: #fff; padding: .25rem .6rem; margin: 0 0 .75rem;
  box-shadow: 4px 4px 0 var(--pink); font-size: .9rem; letter-spacing: .1em; }
.title { margin: 0; font-size: clamp(2.6rem, 8vw, 6.5rem); font-weight: 900; line-height: .95; letter-spacing: -.04em; text-transform: uppercase; }
.title__mark { display: inline-block; margin-top: .5rem; padding: 0 .3em; background: var(--ink); color: #fff; box-shadow: 8px 8px 0 var(--lime); }

/* Buttons */
.btn { display: inline-flex; align-items: center; justify-content: center; gap: .5rem; padding: .85rem 1.4rem;
  border: 4px solid var(--ink); background: #fff; color: var(--ink); font: inherit; font-weight: 800; font-size: .85rem;
  text-transform: uppercase; text-decoration: none; cursor: pointer; box-shadow: 4px 4px 0 var(--ink);
  transition: transform .12s, box-shadow .12s, background .12s; }
.btn:hover:not(:disabled) { background: var(--lime); transform: translate(-2px, -2px); box-shadow: 6px 6px 0 var(--ink); }
.btn:active:not(:disabled) { transform: translate(4px, 4px); box-shadow: 0 0 0 var(--ink); }
.btn:disabled { opacity: .45; cursor: not-allowed; }
.btn--go { background: var(--ink); color: var(--lime); border-color: var(--lime); box-shadow: 8px 8px 0 var(--lime);
  font-size: clamp(1rem, 2.4vw, 1.4rem); padding: 1.2rem 2rem; }
.btn--go:hover { background: var(--ink) !important; color: #fff; }
.btn--lock { background: #e4e4e7; color: var(--mute); border-style: dashed; box-shadow: none; cursor: not-allowed; }
:where(.btn, .node):focus-visible { outline: 4px solid var(--pink); outline-offset: 3px; }

/* Info */
.info { display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; margin-bottom: 5rem; }
.card { background: #fff; border: 4px solid var(--ink); padding: 2rem; box-shadow: 8px 8px 0 var(--ink); }
.card--dark { background: var(--ink); color: #fff; }
.label { margin: 0 0 1rem; padding-bottom: .5rem; border-bottom: 2px dashed #d4d4d8; font-size: .75rem; color: var(--mute); }
.label--lime { color: var(--lime); border-color: #3f3f46; }
.lead { margin: 0 0 1rem; font-size: clamp(1.05rem, 1.6vw, 1.3rem); font-weight: 700; max-width: 60ch; }
.lead mark { background: var(--lime); padding: .1em .3em; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
.body { margin: 0 0 1.5rem; color: #d4d4d8; font-size: 1.05rem; max-width: 62ch; }
.body strong, .hl { color: #fff; }
.hl { text-decoration: underline; text-decoration-color: var(--lime); text-decoration-thickness: 4px; text-underline-offset: 4px; }
.seats { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; border-top: 2px dashed #3f3f46; padding-top: 1.5rem; }
.seat__name { margin: 0; font-size: .75rem; color: #a1a1aa; }
.seat__num { margin: .25rem 0 .5rem; font-size: 3.2rem; font-weight: 900; line-height: 1; }
.seat__num small { font-size: 1.5rem; color: #a1a1aa; }
.bar { height: 10px; background: #27272a; border: 2px solid #52525b; }
.bar span { display: block; height: 100%; background: var(--lime); }
.perk { grid-column: auto; }

/* Network */
.net { margin-bottom: 6rem; padding: clamp(1.5rem, 4vw, 3rem); background: #fff; border: 8px solid var(--ink); box-shadow: 16px 16px 0 var(--ink); }
.h2 { margin: 0 0 1rem; font-size: clamp(1.8rem, 4.5vw, 3.5rem); font-weight: 900; letter-spacing: -.03em; text-transform: uppercase; }
.h2--center { text-align: center; }
.h2--tag { display: inline-block; background: var(--ink); color: #fff; padding: .6rem 1.2rem; margin-bottom: 2rem; }
.net__hint { text-align: center; margin: 0 0 1rem; font-weight: 700; color: var(--mute); }
.net__count { display: inline-block; margin-left: .5rem; background: var(--ink); color: var(--lime); padding: 0 .5rem; }
.progress { max-width: 480px; height: 14px; margin: 0 auto 2rem; border: 3px solid var(--ink); background: #fff; }
.progress span { display: block; height: 100%; background: var(--lime); transition: width .35s; }

.topo { position: relative; width: 100%; max-width: 760px; margin: 0 auto; aspect-ratio: 16 / 10; min-height: 340px; }
.topo__lines { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }
.line { stroke: #d4d4d8; stroke-width: 6; stroke-dasharray: 12 12; vector-effect: non-scaling-stroke; transition: stroke .3s; }
.line--on { stroke: #65a30d; animation: dash 1s linear infinite; }
@keyframes dash { to { stroke-dashoffset: -24; } }

.server { position: absolute; left: 50%; top: 50%; translate: -50% -50%; z-index: 2; width: clamp(96px, 18vw, 150px); aspect-ratio: 1;
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: .4rem;
  background: #fff; border: 8px solid var(--ink); font-weight: 800; font-size: .7rem; color: var(--mute); transition: all .4s; }
.server svg { width: 45%; color: var(--ink); }
.server--on { border-color: var(--lime); color: var(--ink); scale: 1.1; box-shadow: 0 0 0 6px var(--ink), 0 0 60px rgba(132, 204, 22, .6); }

.node { position: absolute; z-index: 3; translate: -50% -50%; width: clamp(84px, 16vw, 116px); aspect-ratio: 1;
  display: flex; flex-direction: column; align-items: center; justify-content: center; gap: .5rem;
  background: #fff; color: var(--mute); border: 4px solid var(--ink); font: inherit; font-weight: 800; font-size: clamp(.6rem, 1.4vw, .75rem);
  cursor: pointer; box-shadow: 4px 4px 0 var(--ink); transition: scale .15s, background .15s, box-shadow .15s; }
.node:hover { scale: 1.08; }
.node:active { scale: .95; }
.node__led { width: 16px; height: 16px; border-radius: 50%; border: 2px solid var(--ink); background: #d4d4d8; }
.node--on { background: var(--lime); color: var(--ink); box-shadow: 0 0 0 var(--ink); }
.node--on .node__led { background: var(--ink); animation: blink 1.4s steps(2) infinite; }
@keyframes blink { 50% { opacity: .3; } }

.term { max-width: 560px; margin: 2rem auto 1.25rem; padding: 1rem 1.2rem; min-height: 7.5rem; background: #18181b; border: 4px solid var(--ink); color: #a1a1aa; font-size: .85rem; }
.term p { margin: 0 0 .2rem; }
.term span { color: var(--lime); }
.term__last { color: #fff; }
.actions { display: flex; flex-wrap: wrap; justify-content: center; gap: 1rem; margin-bottom: 2rem; }
.cta { display: flex; justify-content: center; min-height: 90px; }

/* Bento */
.bento { display: grid; grid-template-columns: repeat(4, 1fr); gap: 2rem; }
.b { position: relative; overflow: hidden; display: flex; flex-direction: column; justify-content: space-between; gap: 1.5rem;
  min-height: 300px; padding: 2rem; border: 4px solid var(--ink); box-shadow: 8px 8px 0 var(--ink); transition: transform .15s, box-shadow .15s; }
.b:hover { transform: translate(-3px, -3px); box-shadow: 11px 11px 0 var(--ink); }
.b--wide { grid-column: span 2; }
.b h3 { margin: 0 0 .75rem; font-size: clamp(1.8rem, 3.4vw, 3rem); font-weight: 900; line-height: 1; text-transform: uppercase; hyphens: manual; }
.b p { margin: 0; font-weight: 700; font-size: 1.05rem; max-width: 46ch; }
.b--white { background: #fff; color: var(--ink); }
.b--black { background: var(--ink); color: #fff; }
.b--black p { color: #d4d4d8; }
.b--code { background: #18181b; color: #fff; }
.b--code p { color: #d4d4d8; }
.b--yellow { background: var(--yellow); padding: 1.5rem; }
.inner { flex: 1; display: flex; flex-direction: column; justify-content: center; padding: 2rem; background: #fff; border: 4px solid var(--ink); color: var(--ink); }
.chip { align-self: flex-start; padding: .35rem .8rem; border: 2px solid var(--ink); background: #fff; color: var(--ink); font-size: .75rem; font-weight: 800; box-shadow: 2px 2px 0 var(--ink); }
.chip--dark { background: var(--ink); color: #fff; }
.emoji { font-size: 4.5rem; line-height: 1; transition: scale .2s; transform-origin: left; }
.b:hover .emoji { scale: 1.2; }
.code { margin: 0; padding-bottom: 1rem; border-bottom: 2px solid #3f3f46; color: #a1a1aa; font: inherit; font-size: .85rem; white-space: pre-wrap; }
.code span { color: var(--lime); }
.code em { color: #71717a; font-style: normal; }
.bg-sign { position: absolute; right: -.5rem; bottom: -2rem; font-size: 11rem; font-weight: 900; opacity: .08; pointer-events: none; }
.b--career > div { position: relative; z-index: 1; }

/* Reveal */
.reveal { opacity: 0; translate: 0 24px; transition: opacity .5s, translate .5s; }
.reveal.is-in { opacity: 1; translate: 0 0; }

/* Transition */
.pop-enter-active { animation: pop .5s cubic-bezier(.175, .885, .32, 1.275); }
.pop-leave-active { transition: opacity .15s; }
.pop-leave-to { opacity: 0; }
@keyframes pop { from { transform: scale(.6); opacity: 0; } to { transform: scale(1); opacity: 1; } }

@media (max-width: 1000px) {
  .bento { grid-template-columns: 1fr 1fr; }
  .info { grid-template-columns: 1fr; }
}
@media (max-width: 640px) {
  .bento { grid-template-columns: 1fr; }
  .b--wide { grid-column: auto; }
  .seats { grid-template-columns: 1fr; }
  .card { box-shadow: 5px 5px 0 var(--ink); }
  .topo { min-height: 320px; }
}
@media (prefers-reduced-motion: reduce) {
  .ticker__track, .line--on, .node--on .node__led { animation: none; }
  .reveal { opacity: 1; translate: 0 0; transition: none; }
  * { scroll-behavior: auto !important; }
}
</style>