<template>
  <div>
    <!-- HERO СЕКЦІЯ -->
    <div class="relative min-h-[85vh] flex flex-col lg:flex-row items-center justify-center border-b-2 border-black overflow-hidden px-4 lg:px-12 py-20">
      
      <!-- Фонова технічна сітка -->
      <div class="absolute inset-0 opacity-10 bg-[linear-gradient(#000_1px,transparent_1px),linear-gradient(90deg,#000_1px,transparent_1px)] bg-[size:40px_40px]"></div>

      <!-- Ліва частина: Текст -->
      <div class="relative z-10 text-left max-w-3xl flex flex-col items-start lg:w-1/2 mt-10 lg:mt-0">
        <div class="inline-block border-2 border-black px-4 py-1 mb-6 font-pixel text-xl uppercase bg-[#c7d2fe] shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
          Status: Online // 2026
        </div>

        <h1 class="text-5xl md:text-7xl lg:text-8xl font-black uppercase leading-[0.9] tracking-tighter mb-6">
          Мережеві та <br/>
          <span class="font-pixel text-6xl md:text-[110px] lg:text-[130px] text-blue-600 block my-2">Інтернет</span>
          Технології
        </h1>

        <p class="text-xl md:text-2xl font-bold max-w-xl border-l-4 border-black pl-6">
          Ми не просто вивчаємо мережі. Ми їх проєктуємо. Сучасна IT-освіта з акцентом на реальну інфраструктуру, CI/CD конвеєри та хардкорну практику.
        </p>
      </div>

      <!-- Права частина: ASCII Пончик (Термінал) -->
      <div class="relative z-10 hidden lg:flex lg:w-1/2 justify-center items-center mt-12 lg:mt-0">
        <div class="bg-black border-2 border-black p-6 shadow-[12px_12px_0px_0px_rgba(199,210,254,1)] w-full max-w-[550px]">
          <div class="flex gap-2 mb-4 border-b border-gray-700 pb-3">
            <div class="w-3.5 h-3.5 bg-red-500 rounded-full"></div>
            <div class="w-3.5 h-3.5 bg-yellow-500 rounded-full"></div>
            <div class="w-3.5 h-3.5 bg-green-500 rounded-full"></div>
            <span class="font-pixel text-sm text-gray-400 ml-3">root@mit-server:~ ./donut.sh</span>
          </div>
          <pre class="font-pixel text-[14px] leading-[14px] text-blue-500 whitespace-pre overflow-hidden flex justify-center">{{ donutFrame }}</pre>
        </div>
      </div>
      
      <!-- Декоративна біжуча стрічка -->
      <div class="absolute bottom-0 left-0 w-full border-t-2 border-black bg-black text-[#F4F4F0] overflow-hidden py-2 z-20">
        <div class="whitespace-nowrap font-pixel text-xl animate-marquee uppercase tracking-widest">
          * DevOps * Cybersecurity * Cloud Infrastructure * Node.js * Python * Docker * Kubernetes * 
          DevOps * Cybersecurity * Cloud Infrastructure * Node.js * Python * Docker * Kubernetes *
        </div>
      </div>
    </div>

    <!-- СЕКЦІЯ: ЧОМУ НАС ОБИРАЮТЬ -->
    <div class="py-24 px-6 max-w-[1400px] mx-auto">
      <div class="text-center mb-16">
        <h2 class="font-pixel text-2xl uppercase tracking-widest text-blue-600 mb-4">[ SYS_INFO ]</h2>
        <h3 class="text-4xl md:text-6xl font-black uppercase tracking-tighter">Чому обирають нас</h3>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
        <!-- Картки згенеровані зі списку whyUs (див. script) -->
        <div
          v-for="(item, i) in whyUs"
          :key="item.title"
          class="group border-2 border-black p-6 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:translate-x-[2px] hover:translate-y-[2px] hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] transition-all cursor-crosshair"
          :class="item.accent
            ? 'bg-[#c7d2fe] hover:bg-blue-700 hover:text-[#F4F4F0]'
            : 'bg-[#F4F4F0] hover:bg-black hover:text-[#F4F4F0]'"
        >
          <div class="font-pixel text-3xl mb-4" :class="item.accent ? 'text-black group-hover:text-black' : 'group-hover:text-blue-500'">[0{{ i + 1 }}]</div>
          <h4 class="text-2xl font-bold uppercase mb-3" :class="item.accent ? 'text-black group-hover:text-[#F4F4F0]' : ''">{{ item.title }}</h4>
          <p class="font-medium text-sm leading-relaxed" :class="item.accent ? 'text-black group-hover:text-[#F4F4F0]' : ''">
            {{ item.text }}
          </p>
        </div>
      </div> 
    </div> 

    <!-- РОЗДІЛЮВАЧ: Рядок коду -->
    <div class="w-full border-y-2 border-black bg-blue-600 text-[#F4F4F0] py-2 px-6 font-pixel text-sm uppercase flex justify-between">
      <span>fetch('/api/v1/about_us?limit=3&sort=pinned')</span>
      <span class="animate-pulse">Loading... [OK]</span>
    </div>

    <!-- СЕКЦІЯ: ПРО НАС ТА ІНТЕРАКТИВНИЙ ТЕРМІНАЛ -->
    <div class="py-24 px-6 max-w-[1400px] mx-auto border-t-2 border-black border-dashed my-12 bg-white">
      <div class="grid grid-cols-1 lg:grid-cols-12 gap-12 items-center mb-20">
        
        <!-- Текст (7 колонок) -->
        <div class="lg:col-span-7 flex flex-col gap-6">
          <div class="font-pixel text-xl text-blue-600 uppercase tracking-widest">[ ABOUT_ROOT // MIT_DEPT ]</div>
          <h2 class="text-5xl md:text-7xl font-black uppercase tracking-tighter leading-[0.9]">
            База для <br> твого ІТ-шляху
          </h2>
          <div class="border-l-4 border-black pl-6 flex flex-col gap-5 text-lg font-medium mt-4">
            <p>
              Забудь про нудні методички 90-х. Кафедра МІТ — це інженерний хаб, де з 2016 року ми випускаємо реальних фахівців, а не просто людей з корочками. 
            </p>
            <p>
              Наш roadmap зібраний за жорсткими світовими стандартами ITU. Ніякої води: піднімаємо хмари, налаштовуємо кібербезпеку, деплоїмо власні проєкти, працюємо з IoT та ШІ. Після нас твій GitHub буде заряджений на оффери.
            </p>
            
            <!-- Статистика набору -->
            <div class="bg-[#c7d2fe] border-2 border-black p-5 mt-2 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] hover:bg-blue-600 hover:text-white transition-colors group">
              <span class="font-pixel font-bold block mb-2 group-hover:text-black transition-colors">// STATS_2026:</span>
              <ul class="list-disc pl-5 font-bold space-y-1">
                <li>Бакалаврат: 35 місць <span class="text-sm font-normal">(29 бюджетних)</span></li>
                <li>Магістратура: 15 місць <span class="text-sm font-normal">(10 бюджетних)</span></li>
              </ul>
            </div>
          </div>
        </div>

        <!-- ІНТЕРАКТИВНИЙ ТЕРМІНАЛ (5 колонок) -->
        <div class="lg:col-span-5 bg-black border-2 border-black p-6 shadow-[12px_12px_0px_0px_rgba(199,210,254,1)] flex flex-col justify-between h-[480px]">
          
          <div class="flex flex-col sm:flex-row items-start sm:items-center justify-between border-b border-gray-800 pb-4 gap-3">
            <div class="flex items-center gap-2">
              <div class="w-3.5 h-3.5 bg-red-500 rounded-full"></div>
              <div class="w-3.5 h-3.5 bg-yellow-500 rounded-full"></div>
              <div class="w-3.5 h-3.5 bg-green-500 rounded-full"></div>
              <span class="font-pixel text-xs text-gray-400 ml-2">mit_core@sys:~</span>
            </div>
            <div class="flex gap-1 bg-gray-900 p-1 border border-gray-800">
              <button 
                @click="terminalTab = 'ascii'" 
                class="font-pixel text-[10px] px-2 py-1 uppercase transition-colors cursor-pointer"
                :class="terminalTab === 'ascii' ? 'bg-blue-600 text-white' : 'text-gray-400 hover:text-white'"
              >
                LOGO
              </button>
              <button 
                @click="terminalTab = 'specs'" 
                class="font-pixel text-[10px] px-2 py-1 uppercase transition-colors cursor-pointer"
                :class="terminalTab === 'specs' ? 'bg-blue-600 text-white' : 'text-gray-400 hover:text-white'"
              >
                SPECS
              </button>
              <button 
                @click="terminalTab = 'logs'" 
                class="font-pixel text-[10px] px-2 py-1 uppercase transition-colors cursor-pointer"
                :class="terminalTab === 'logs' ? 'bg-blue-600 text-white' : 'text-gray-400 hover:text-white'"
              >
                LOGS
              </button>
            </div>
          </div>
          
          <div class="flex-grow flex items-center justify-center py-4 overflow-hidden text-left w-full">
            <div v-if="terminalTab === 'ascii'" class="w-full flex flex-col items-center justify-center">
              <pre class="font-pixel text-[11px] sm:text-[13px] leading-[1.1] text-green-500 whitespace-pre select-none drop-shadow-[0_0_8px_rgba(34,197,94,0.4)]">
███╗   ███╗ ██╗ ████████╗
████╗ ████║ ██║ ╚══██╔══╝
██╔████╔██║ ██║    ██║   
██║╚██╔╝██║ ██║    ██║   
██║ ╚═╝ ██║ ██║    ██║   
╚═╝     ╚═╝ ╚═╝    ╚═╝   
              </pre>
              <div class="font-mono text-xs text-gray-400 mt-4 text-center">
                > SYSTEM: <span class="text-green-400">ONLINE</span><br>
                > PROTOCOLS: <span class="text-blue-400">IPv6, BGP, OSPF, K8s</span>
              </div>
            </div>

            <div v-else-if="terminalTab === 'specs'" class="w-full font-mono text-xs text-gray-300 space-y-2">
              <div class="text-blue-400 font-pixel mb-1">// HARDWARE & LABS:</div>
              <p>> CISCO RACK: <span class="text-green-400">Active (Catalyst 3750)</span></p>
              <p>> CLOUD NODES: <span class="text-green-400">Kubernetes Cluster (AWS/Local)</span></p>
              <p>> SECURITY LAB: <span class="text-green-400">Isolated Sandbox</span></p>
              <p>> IoT BENCH: <span class="text-green-400">ESP32 / Raspberry Pi / MQTT</span></p>
              <p class="text-gray-500 mt-4">> STATUS: Fully optimized for hands-on practice.</p>
            </div>

            <div v-else-if="terminalTab === 'logs'" class="w-full font-mono text-[11px] text-green-400 space-y-1 overflow-y-auto max-h-[220px]">
              <p class="text-gray-500">[15:04:01] Initializing kernel modules...</p>
              <p class="text-gray-400">[15:04:02] Loading ITU standard pathways...</p>
              <p class="text-green-400">[15:04:03] DevOps pipeline: SUCCESS</p>
              <p class="text-green-400">[15:04:04] Security firewall: SECURED</p>
              <p class="text-blue-400">[15:04:05] Student GitHub repositories: SYNCED</p>
              <p class="text-yellow-400 animate-pulse">[15:04:06] Ready for incoming connections...</p>
            </div>
          </div>

          <div class="border-t border-gray-800 pt-3 flex justify-between items-center font-pixel text-[10px] text-gray-500">
            <span>MODE: INTERACTIVE</span>
            <span class="text-green-400 animate-pulse">● LIVE_FEED</span>
          </div>

        </div>

      </div>

      <!-- Кар'єрний шлях (Career Tree) -->
      <div class="border-t-2 border-black pt-16">
        <div class="mb-10">
          <h3 class="font-pixel text-2xl uppercase tracking-widest text-blue-600 mb-2">[ CAREER_TREE ]</h3>
          <h4 class="text-3xl md:text-5xl font-black uppercase tracking-tighter">Ким ти станеш після випуску</h4>
          <p class="font-mono text-gray-600 mt-2">Клікни на стек, щоб проінспектувати майбутню професію</p>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-start">
          <div class="lg:col-span-4 flex flex-col gap-4">
            <button 
              v-for="(career, index) in careers" 
              :key="index"
              @click="activeCareer = index"
              class="text-left border-2 border-black p-5 font-bold uppercase transition-all shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] flex justify-between items-center group cursor-pointer"
              :class="activeCareer === index ? 'bg-black text-[#F4F4F0] translate-x-1 translate-y-1 shadow-none' : 'bg-[#F4F4F0] hover:bg-blue-600 hover:text-white'"
            >
              <div>
                <span class="font-pixel text-xs block mb-1 text-blue-400 group-hover:text-yellow-300">[0{{ index + 1 }} // ROLE]</span>
                <span class="text-xl font-black tracking-tight">{{ career.title }}</span>
              </div>
              <span class="font-pixel text-xl">→</span>
            </button>
          </div>

          <div class="lg:col-span-8 bg-black border-2 border-black p-8 shadow-[12px_12px_0px_0px_rgba(199,210,254,1)] text-[#F4F4F0] min-h-[420px] flex flex-col justify-between">
            <div>
              <div class="flex items-center justify-between border-b border-gray-800 pb-4 mb-6">
                <div class="flex gap-2">
                  <div class="w-3.5 h-3.5 bg-red-500 rounded-full"></div>
                  <div class="w-3.5 h-3.5 bg-yellow-500 rounded-full"></div>
                  <div class="w-3.5 h-3.5 bg-green-500 rounded-full"></div>
                  <span class="font-pixel text-xs text-gray-400 ml-2">role_inspector.sh --target={{ careers[activeCareer].id }}</span>
                </div>
                <span class="font-pixel text-xs bg-blue-600 text-white px-2 py-1 uppercase">Level: {{ careers[activeCareer].level }}</span>
              </div>

              <h5 class="text-3xl md:text-4xl font-black uppercase text-blue-400 mb-4 font-pixel tracking-wider">
                {{ careers[activeCareer].title }}
              </h5>
              
              <p class="font-mono text-gray-300 text-base md:text-lg mb-8 leading-relaxed">
                {{ careers[activeCareer].description }}
              </p>

              <div class="mb-6">
                <div class="font-pixel text-xs text-gray-400 mb-3">// TECH_STACK & TOOLS:</div>
                <div class="flex flex-wrap gap-2">
                  <span 
                    v-for="(tech, tIndex) in careers[activeCareer].stack" 
                    :key="tIndex"
                    class="border border-gray-700 bg-gray-900 font-mono text-xs px-3 py-1.5 text-blue-300 uppercase tracking-wider"
                  >
                    {{ tech }}
                  </span>
                </div>
              </div>
            </div>

            <div class="border-t border-gray-800 pt-4 flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 font-mono text-sm">
              <span class="text-gray-400">Середній старт в Україні:</span>
              <span class="font-pixel text-lg text-green-400 bg-gray-900 border border-gray-800 px-3 py-1">
                {{ careers[activeCareer].salary }}
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- СТАТИСТИКА ПРАЦЕВЛАШТУВАННЯ ТА ПАРТНЕРИ -->
    <div class="w-full bg-black text-[#F4F4F0] border-y-2 border-black py-20 px-6 my-16">
      <div class="max-w-[1400px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-5 border-2 border-white/20 p-8 bg-zinc-900 shadow-[8px_8px_0px_0px_rgba(199,210,254,1)]">
          <div class="font-pixel text-blue-400 mb-2">[ CAREER_STATS ]</div>
          <div class="text-6xl md:text-7xl font-black font-pixel text-white mb-4">76%</div>
          <p class="font-mono text-lg text-gray-300 uppercase tracking-wider">
            Студентів обіймають посади <span class="text-blue-400 font-bold">Middle / Senior / Lead</span> інженерів під час або одразу після випуску.
          </p>
        </div>

        <div class="lg:col-span-7">
          <div class="font-pixel text-xs text-gray-400 mb-4">// TOP_EMPLOYERS & PARTNERS:</div>
          <div class="grid grid-cols-2 sm:grid-cols-3 gap-4">
            <div
              v-for="p in partners"
              :key="p"
              class="border-2 border-white/20 bg-zinc-900 p-6 flex items-center justify-center font-pixel text-xl tracking-widest text-gray-300 hover:border-blue-500 hover:text-white transition-colors"
            >
              {{ p }}
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- ЕКСПЕРТНИЙ СКЛАД (ВИКЛАДАЧІ З ПІКСЕЛЬНОЮ КОРОНОЮ ДЛЯ ЗАВКАФЕДРИ) -->
    <div class="py-24 px-6 max-w-[1400px] mx-auto">
      <div class="text-center mb-16">
        <h2 class="font-pixel text-2xl uppercase tracking-widest text-blue-600 mb-4">[ CORE_TEAM ]</h2>
        <h3 class="text-4xl md:text-6xl font-black uppercase tracking-tighter">Наші викладачі — практики</h3>
        <p class="font-mono text-gray-600 mt-2">Зіркові лектори та інженери, які розробляють реальні системи (клікніть на картку для деталей)</p>
      </div>

      <div v-if="teachersPending" class="w-full border-2 border-dashed border-gray-400 py-16 flex flex-col items-center justify-center text-gray-500">
        <div class="font-pixel text-xl animate-pulse">[ FETCHING_TEACHERS... ]</div>
      </div>

      <div v-else-if="teachersError" class="w-full border-2 border-dashed border-red-500 py-16 flex flex-col items-center justify-center text-red-500 bg-red-50">
        <div class="font-pixel text-xl">[ TEACHERS_API_ERROR ]</div>
      </div>

      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
        <div v-if="!teachers || teachers.length === 0" class="col-span-full border-2 border-dashed border-black p-12 text-center bg-white">
          <div class="font-pixel text-xl mb-2">[ NO_TEACHERS_IN_DB ]</div>
          <p class="font-mono text-sm text-gray-600">Додай викладачів через панель адміністратора (http://127.0.0.1:8000/admin), і вони автоматично з'являться тут!</p>
        </div>

        <!-- Картка викладача -->
        <div 
          v-for="teacher in teachers" 
          :key="teacher.id" 
          @click="openTeacherModal(teacher)"
          class="border-2 border-black bg-white flex flex-col justify-between shadow-[6px_6px_0px_0px_rgba(0,0,0,1)] hover:translate-x-1 hover:translate-y-1 hover:shadow-none transition-all cursor-pointer group"
        >
          <div>
            <div class="w-full h-72 border-b-2 border-black bg-gray-200 relative overflow-hidden">
              <img 
                v-if="teacher.photo" 
                :src="teacher.photo.startsWith('http') ? teacher.photo : `http://127.0.0.1:8000${teacher.photo}`" 
                :alt="`${teacher.last_name} ${teacher.first_name}`" 
                class="w-full h-full object-cover object-top group-hover:scale-105 transition-transform duration-500"
              />
              <div v-else class="w-full h-full flex items-center justify-center bg-black text-green-400 font-pixel text-xs">
                [ NO_PHOTO ]
              </div>

              <!-- Золота піксельна корона для зав. кафедри -->
              <div v-if="teacher.position && teacher.position.toLowerCase().includes('завідувач')" class="absolute top-2 left-2 bg-yellow-400 border-2 border-black px-2.5 py-1 font-pixel text-xs shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] flex items-center gap-1.5 z-10">
                <span>👑</span> <span class="font-bold text-black uppercase">HEAD</span>
              </div>

              <div class="absolute top-2 right-2 bg-black text-white font-pixel text-[10px] px-2 py-1 uppercase border border-white">
                {{ teacher.degree || 'Expert' }}
              </div>
            </div>

            <div class="p-6">
              <div class="font-pixel text-xs text-blue-600 mb-1 uppercase">{{ teacher.position }}</div>
              <h4 class="text-2xl font-black uppercase mb-3 tracking-tight group-hover:text-blue-600 transition-colors">
                {{ teacher.last_name }} <br>{{ teacher.first_name }}
              </h4>
              <p class="font-mono text-xs text-gray-700 leading-relaxed line-clamp-3">
                {{ teacher.bio || 'Провідний спеціаліст та викладач кафедри Мережевих та інтернет технологій.' }}
              </p>
            </div>
          </div>

          <div class="p-6 pt-0 flex justify-between items-center font-pixel text-xs text-blue-600 underline">
            <span>[ ДЕТАЛЬНІШЕ ]</span>
            <span>→</span>
          </div>
        </div>

      </div>
    </div>

    <!-- РОЗДІЛЮВАЧ: Рядок коду -->
    <div class="w-full border-y-2 border-black bg-blue-600 text-[#F4F4F0] py-2 px-6 font-pixel text-sm uppercase flex justify-between">
      <span>fetch('/api/v1/news?limit=3&sort=pinned')</span>
      <span class="animate-pulse">Loading... [OK]</span>
    </div>

    <!-- СЕКЦІЯ: НОВИНИ (LATEST_LOGS) — максимум 3 -->
    <div class="py-24 px-6 max-w-[1400px] mx-auto bg-[#F4F4F0]">
      <div class="flex justify-between items-end mb-12 border-b-4 border-black pb-4">
        <div>
          <h2 class="font-pixel text-2xl uppercase tracking-widest text-blue-600 mb-2">[ LATEST_LOGS ]</h2>
          <h3 class="text-4xl md:text-5xl font-black uppercase tracking-tighter">Оновлення Кафедри</h3>
        </div>
        <NuxtLink to="/news" class="hidden md:inline-block border-2 border-black px-6 py-2 uppercase font-bold text-sm bg-black text-[#F4F4F0] hover:bg-blue-600 transition-colors shadow-[4px_4px_0px_0px_rgba(199,210,254,1)]">
          View_All_Logs()
        </NuxtLink>
      </div>

      <div class="flex flex-col gap-10">
        <div v-if="pending" class="w-full border-2 border-dashed border-gray-400 py-20 flex flex-col items-center justify-center text-gray-500">
          <div class="font-pixel text-2xl mb-2 animate-pulse">[ FETCHING_DATA_FROM_SERVER... ]</div>
        </div>

        <div v-else-if="error" class="w-full border-2 border-dashed border-red-500 py-20 flex flex-col items-center justify-center text-red-500 bg-red-50">
          <div class="font-pixel text-2xl mb-2">[ ERROR_CONNECTION_REFUSED ]</div>
          <div class="font-pixel text-sm">Бекенд не відповідає. Перевір, чи запущений Django (порт 8000).</div>
        </div>

        <div v-else-if="latestNews.length === 0" class="border-2 border-dashed border-black p-12 text-center bg-white">
          <div class="font-pixel text-xl">[ NO_LOGS_YET ]</div>
        </div>

        <template v-else>
          <article
            v-for="(item, i) in latestNews"
            :key="item.id"
            class="group relative grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8 border-2 border-black p-5 md:p-6 bg-[#F4F4F0] shadow-[8px_8px_0px_0px_rgba(0,0,0,1)] transition-transform hover:-translate-y-1"
          >
            <div v-if="item.is_pinned" class="absolute -top-4 -right-4 border-2 border-black bg-red-500 text-[#F4F4F0] font-pixel px-3 py-1 uppercase shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] rotate-3 z-10">
              [x] Pinned
            </div>

            <!-- Текст: обрізаний, повний варіант на /news -->
            <div class="lg:col-span-7 flex flex-col justify-center relative z-0">
              <div class="font-pixel text-gray-500 mb-3 text-sm">
                LOG_0{{ i + 1 }} // {{ item.date_posted }}
              </div>
              <h4 class="text-2xl lg:text-4xl font-black uppercase tracking-tighter mb-4 group-hover:text-blue-600 transition-colors line-clamp-3">
                {{ item.title }}
              </h4>
              <p class="font-mono text-sm md:text-base leading-relaxed border-l-4 border-blue-600 pl-4 mb-6 text-gray-800 line-clamp-4">
                {{ item.content }}
              </p>
              <NuxtLink to="/news" class="self-start font-pixel text-lg text-blue-600 hover:text-black hover:underline uppercase mt-auto">
                > Read_More
              </NuxtLink>
            </div>

            <!-- Фото: як було раніше (одне — у повний розмір, кілька — сітка). Показуємо максимум 2 -->
            <div
              class="lg:col-span-5 relative z-0 grid gap-4 border-2 border-black p-4 bg-white h-fit"
              :class="item.images && item.images.length > 1 ? 'grid-cols-1 sm:grid-cols-2' : 'grid-cols-1'"
            >
              <template v-if="item.images && item.images.length">
                <div v-for="(img, k) in item.images.slice(0, 2)" :key="img.id" class="relative">
                  <button type="button" class="block w-full cursor-zoom-in" :aria-label="`Збільшити фото: ${item.title}`" @click="openModal(imgUrl(img.image))">
                    <img
                      :src="imgUrl(img.image)"
                      :alt="item.title"
                      loading="lazy"
                      class="w-full border-2 border-black shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] group-hover:shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] transition-all"
                      :class="item.images.length === 1 ? 'h-auto max-h-[400px] object-cover object-center' : 'h-48 md:h-64 object-cover object-top'"
                    />
                  </button>
                  <span v-if="k === 1 && item.images.length > 2" class="absolute bottom-3 right-3 bg-black text-white font-pixel text-xs px-2 py-1 border-2 border-white pointer-events-none">
                    +{{ item.images.length - 2 }} фото
                  </span>
                </div>
              </template>
              <div v-else class="flex items-center justify-center min-h-[250px] bg-[#F4F4F0]">
                <span class="font-pixel text-gray-400">[ NO_IMAGE_ATTACHED ]</span>
              </div>
            </div>
          </article>

          <!-- Архів: з'являється, коли новин більше ніж 3 -->
          <NuxtLink
            v-if="hiddenCount > 0"
            to="/news"
            class="flex items-center justify-between gap-4 border-4 border-dashed border-black bg-white px-6 py-5 font-pixel text-lg uppercase hover:bg-black hover:text-[#F4F4F0] hover:border-solid transition-colors group/a"
          >
            <span>Ще {{ hiddenCount }} {{ hiddenCount === 1 ? 'запис' : 'записів' }} в архіві</span>
            <span class="text-2xl group-hover/a:translate-x-2 transition-transform">→</span>
          </NuxtLink>
        </template>
      </div>
      
      <NuxtLink to="/news" class="mt-8 md:hidden block text-center border-2 border-black px-6 py-4 uppercase font-bold text-sm bg-black text-[#F4F4F0] shadow-[4px_4px_0px_0px_rgba(199,210,254,1)]">
          View_All_Logs()
      </NuxtLink>
    </div>

    <!-- МОДАЛЬНЕ ВІКНО ДЛЯ ФОТО -->
    <div v-if="selectedImage" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/90 p-4 md:p-8 cursor-pointer backdrop-blur-sm" @click="closeModal">
      <div class="relative max-w-6xl max-h-[90vh] bg-[#F4F4F0] border-4 border-black p-2 shadow-[12px_12px_0px_0px_rgba(199,210,254,1)] cursor-default" @click.stop>
        <button @click="closeModal" class="absolute -top-6 -right-6 md:-top-8 md:-right-8 bg-red-500 border-2 border-black text-[#F4F4F0] font-pixel px-4 py-2 text-lg md:text-2xl hover:bg-black transition-colors shadow-[4px_4px_0px_0px_rgba(0,0,0,1)] z-10 cursor-pointer">
          [ X ]
        </button>
        <img :src="selectedImage" class="max-w-full max-h-[85vh] object-contain border-2 border-black bg-white" />
      </div>
    </div>

    <!-- МОДАЛЬНЕ ВІКНО ДЛЯ ПОВНОЇ ІНФОРМАЦІЇ ПРО ВИКЛАДАЧА -->
    <div v-if="selectedTeacher" class="fixed inset-0 z-[100] flex items-center justify-center bg-black/90 p-4 md:p-8 cursor-pointer backdrop-blur-sm" @click="closeTeacherModal">
      <div class="relative max-w-3xl w-full bg-[#F4F4F0] border-4 border-black p-6 md:p-10 shadow-[12px_12px_0px_0px_rgba(199,210,254,1)] cursor-default max-h-[90vh] overflow-y-auto" @click.stop>
        
        <button @click="closeTeacherModal" class="absolute top-4 right-4 bg-red-500 border-2 border-black text-[#F4F4F0] font-pixel px-3 py-1 text-base hover:bg-black transition-colors shadow-[2px_2px_0px_0px_rgba(0,0,0,1)] z-20 cursor-pointer">
          [ X ]
        </button>

        <div class="grid grid-cols-1 md:grid-cols-12 gap-8 items-start pt-2">
          <div class="md:col-span-5 border-2 border-black bg-white p-2 shadow-[4px_4px_0px_0px_rgba(0,0,0,1)]">
            <img 
              v-if="selectedTeacher.photo" 
              :src="selectedTeacher.photo.startsWith('http') ? selectedTeacher.photo : `http://127.0.0.1:8000${selectedTeacher.photo}`" 
              class="w-full h-72 md:h-80 object-cover object-top border-2 border-black" 
            />
            <div v-else class="w-full h-72 md:h-80 bg-black text-green-400 font-pixel flex items-center justify-center text-xs">
              [ NO_PHOTO ]
            </div>
          </div>

          <div class="md:col-span-7 flex flex-col justify-between">
            <div>
              <div class="flex flex-wrap items-center gap-2 mb-3 pr-8">
                <span class="font-pixel text-xs bg-blue-600 text-white px-2 py-1 uppercase">{{ selectedTeacher.degree || 'Expert' }}</span>
                <span class="font-pixel text-xs text-gray-700 uppercase">// {{ selectedTeacher.position }}</span>
              </div>
              
              <h3 class="text-2xl md:text-4xl font-black uppercase mb-6 tracking-tight leading-tight break-words">
                {{ selectedTeacher.last_name }} <br>{{ selectedTeacher.first_name }}
              </h3>

              <div class="font-mono text-sm md:text-base text-gray-800 leading-relaxed whitespace-pre-line border-l-4 border-blue-600 pl-4 mb-8 break-words">
                {{ selectedTeacher.bio }}
              </div>
            </div>

            <div class="flex flex-wrap gap-4 font-pixel text-xs pt-4 border-t-2 border-black">
              <a v-if="selectedTeacher.github" :href="selectedTeacher.github" target="_blank" class="border-2 border-black px-4 py-2 bg-white hover:bg-black hover:text-white transition-colors shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
                GITHUB PROFILE ↗
              </a>
              <a v-if="selectedTeacher.linkedin" :href="selectedTeacher.linkedin" target="_blank" class="border-2 border-black px-4 py-2 bg-[#c7d2fe] hover:bg-blue-600 hover:text-white transition-colors shadow-[2px_2px_0px_0px_rgba(0,0,0,1)]">
                LINKEDIN ↗
              </a>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue';

const { data: newsItems, pending, error } = await useFetch('http://127.0.0.1:8000/api/v1/news/');
const { data: teachers, pending: teachersPending, error: teachersError } = await useFetch('http://127.0.0.1:8000/api/v1/teachers/');

const selectedImage = ref(null);
const selectedTeacher = ref(null);
const terminalTab = ref('ascii');
const activeCareer = ref(0);

// ===== НОВИНИ: максимум 3 на головній =====
const MAX_NEWS = 3;

// Працює і з масивом, і з пагінацією Django ({ results: [...] })
const allNews = computed(() =>
  Array.isArray(newsItems.value) ? newsItems.value : (newsItems.value?.results ?? [])
);

// Закріплені зверху, далі від нових до старіших, обрізаємо до 3
const latestNews = computed(() =>
  [...allNews.value]
    .sort((a, b) =>
      (Number(!!b.is_pinned) - Number(!!a.is_pinned)) ||
      (new Date(b.date_posted || 0) - new Date(a.date_posted || 0)))
    .slice(0, MAX_NEWS)
);

const hiddenCount = computed(() => Math.max(0, allNews.value.length - MAX_NEWS));
const imgUrl = (p) => (p.startsWith('http') ? p : `http://127.0.0.1:8000${p}`);

// ===== "ЧОМУ ОБИРАЮТЬ НАС": дані карток (accent — синя картка) =====
const whyUs = [
  { title: 'Самореалізація', text: 'Освіта на кафедрі дозволить реалізувати себе в науці, промисловості та бізнесі. Прямий шлях від студента до Senior інженера.' },
  { title: 'Hardcore Дисципліни', text: 'Телекомунікації, розгортання мереж, бази даних, Штучний Інтелект та IoT. Працюємо з сучасними стеками замість застарілих методичок.' },
  { title: 'Практична підготовка', accent: true, text: 'Перспективні технологічні рішення на основі апаратного та програмного забезпечення. Пишемо код, піднімаємо контейнери, налаштовуємо сервери.' },
  { title: 'Експертний склад', text: 'Заняття проводять професори, доценти та провідні розробники сучасних інформаційних систем, які знають продакшен зсередини.' },
  { title: 'Стандарти ITU', text: 'Навчальний план повністю розроблено за жорсткими стандартами International Telecommunications Union.' },
  { title: 'Світова інтеграція', text: 'Співпраця з іноземними компаніями та закордонними навчальними закладами. Відкритий шлях до глобального IT-ринку.' }
];

const partners = ['CILIUM', 'IBM', 'INTEL', 'ДІЯ', 'MICROSOFT', 'N-IX'];

const careers = [
  {
    id: 'devops',
    title: 'DevOps / Cloud Engineer',
    level: 'Middle / Senior',
    description: 'Побудова міцних CI/CD конвеєрів, управління інфраструктурою як кодом (IaC), автоматизація деплою та моніторинг серверів у реальному часі.',
    stack: ['Docker', 'Kubernetes', 'Terraform', 'GitHub Actions', 'AWS / Linux', 'Nginx'],
    salary: '$2,000 - $4,500'
  },
  {
    id: 'llmops',
    title: 'LLMOps / AI Infrastructure',
    level: 'Specialized / R&D',
    description: 'Новітній напрямок. Розгортання, оптимізація та масштабування великих мовних моделей (LLM), побудова пайплайнів для обробки даних та інтеграція ШІ в інфраструктуру.',
    stack: ['Python', 'Docker', 'Vector Databases', 'PyTorch', 'FastAPI', 'Kubernetes'],
    salary: '$2,500 - $5,000'
  },
  {
    id: 'network',
    title: 'Network & System Engineer',
    level: 'Core Engineering',
    description: 'Проєктування захищених корпоративних мереж, налаштування маршрутизації, комутації, віртуальних приватних мереж та забезпечення безперебійної роботи систем.',
    stack: ['Cisco', 'OSPF/BGP', 'Linux OS', 'Wireshark', 'Cybersecurity', 'Firewalls'],
    salary: '$1,500 - $3,500'
  },
  {
    id: 'sec',
    title: 'Cybersecurity Specialist',
    level: 'Defense & Pentest',
    description: 'Аудит безпеки інфраструктури, пошук вразливостей, захист від DDoS-атак, робота з криптографією та моніторинг інцидентів безпеки (SIEM).',
    stack: ['Penetration Testing', 'Wireshark', 'Bash/Python', 'SIEM', 'Firewalls', 'Network Security'],
    salary: '$1,800 - $4,000'
  }
];

const openModal = (url) => {
  selectedImage.value = url;
  if (import.meta.client) { document.body.style.overflow = 'hidden'; }
};

const closeModal = () => {
  selectedImage.value = null;
  if (import.meta.client) { document.body.style.overflow = ''; }
};

const openTeacherModal = (teacher) => {
  selectedTeacher.value = teacher;
  if (import.meta.client) { document.body.style.overflow = 'hidden'; }
};

const closeTeacherModal = () => {
  selectedTeacher.value = null;
  if (import.meta.client) { document.body.style.overflow = ''; }
};

const handleKeydown = (e) => {
  if (e.key === 'Escape') {
    if (selectedImage.value) closeModal();
    if (selectedTeacher.value) closeTeacherModal();
  }
};

const donutFrame = ref('');
let animationId;

const renderDonut = () => {
  let A = 1, B = 1;
  const update = () => {
    let b = [];
    let z = [];
    
    A += 0.035; 
    B += 0.015; 
    
    let cA = Math.cos(A), sA = Math.sin(A), cB = Math.cos(B), sB = Math.sin(B);
    
    for(let k = 0; k < 1760; k++) { 
      b[k] = k % 80 === 79 ? '\n' : ' '; 
      z[k] = 0; 
    }
    
    for(let j = 0; j < 6.28; j += 0.07) {
      let ct = Math.cos(j), st = Math.sin(j);
      for(let i = 0; i < 6.28; i += 0.02) {
        let sp = Math.sin(i), cp = Math.cos(i),
            h = ct + 2, D = 1 / (sp * h * sA + st * cA + 5), t = sp * h * cA - st * sA;
            
        let x = Math.floor(40 + 30 * D * (cp * h * cB - t * sB)),
            y = Math.floor(12 + 15 * D * (cp * h * sB + t * cB)),
            o = x + 80 * y,
            N = Math.floor(8 * ((st * sA - sp * ct * cA) * cB - sp * ct * sA - st * cA - cp * ct * sB));
            
        if(y < 22 && y >= 0 && x >= 0 && x < 79 && D > z[o]) {
          z[o] = D;
          b[o] = ".,-~:;=!*#$@"[N > 0 ? N : 0];
        }
      }
    }
    donutFrame.value = b.join('');
    animationId = requestAnimationFrame(update);
  };
  update();
};

onMounted(() => {
  renderDonut();
  if (import.meta.client) {
    window.addEventListener('keydown', handleKeydown);
  }
});

onUnmounted(() => {
  cancelAnimationFrame(animationId);
  if (import.meta.client) {
    window.removeEventListener('keydown', handleKeydown);
  }
});
</script>

<style scoped>
@keyframes marquee {
  0% { transform: translateX(0%); }
  100% { transform: translateX(-50%); }
}
.animate-marquee {
  display: inline-block;
  animation: marquee 20s linear infinite;
  min-width: 200%;
}
</style>