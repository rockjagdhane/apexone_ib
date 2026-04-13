import streamlit as st
import streamlit.components.v1 as components

# Set up the Streamlit page configuration
st.set_page_config(
    page_title="Apex One | Performance on Autopilot",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Injecting the HTML, CSS, and JS from the Canvas document
# I have added the Gemini API logic to ensure the "Smart Lab" features work 
# directly within your Streamlit application.

html_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apex One | Performance on Autopilot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Poppins:wght@700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    
    <style>
        :root {
            --apex-blue: #007AFF;
            --apex-energy: #FF9500;
            --apex-focus: #AF52DE;
            --apex-recovery: #34C759;
            --apex-hydrate: #5AC8FA;
            --apex-dark: #0a0a0a;
            --apex-glass: rgba(255, 255, 255, 0.03);
        }

        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--apex-dark);
            color: #ffffff;
            margin: 0;
            padding: 0;
            overflow-x: hidden;
        }

        .hero-gradient {
            background: radial-gradient(circle at 50% 50%, #1a1a1a 0%, #0a0a0a 100%);
        }

        /* The Tesla-Style Logo Battery Animation */
        .logo-text span {
            display: inline-block;
            opacity: 0.3;
            transition: opacity 0.4s ease;
        }

        .logo-text.charging span {
            animation: batteryFill 2s infinite;
        }

        @keyframes batteryFill {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 1; text-shadow: 0 0 15px #007AFF; }
        }

        /* Glassmorphism Cards */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            transition: transform 0.3s ease, border-color 0.3s ease;
        }

        .glass-card:hover {
            transform: translateY(-5px);
            border-color: var(--apex-blue);
        }

        .reveal {
            opacity: 0;
            transform: translateY(30px);
            transition: all 0.8s ease-out;
        }

        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }

        /* Mode Glowing Borders */
        .mode-card-energy:hover { border-color: var(--apex-energy); }
        .mode-card-focus:hover { border-color: var(--apex-focus); }
        .mode-card-recovery:hover { border-color: var(--apex-recovery); }
        .mode-card-hydrate:hover { border-color: var(--apex-hydrate); }

        /* Custom Scrollbar */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #0a0a0a; }
        ::-webkit-scrollbar-thumb { background: #333; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--apex-blue); }

        .loader {
            border: 2px solid rgba(255,255,255,0.1);
            border-top: 2px solid var(--apex-blue);
            border-radius: 50%;
            width: 16px;
            height: 16px;
            animation: spin 1s linear infinite;
        }
        @keyframes spin { to { transform: rotate(360deg); } }
    </style>
</head>
<body>

    <nav class="fixed w-full z-50 bg-black/50 backdrop-blur-lg border-b border-white/5">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <div id="mainLogo" class="logo-text text-xl font-bold tracking-[0.2em] cursor-pointer">
                <span>A</span><span>P</span><span>E</span><span>X</span><span>O</span><span>N</span><span>E</span>
            </div>
            <div class="hidden md:flex space-x-8 text-sm font-medium tracking-widest text-white/60">
                <a href="#modes" class="hover:text-white transition">MODES</a>
                <a href="#lab" class="hover:text-white transition">✨ LAB</a>
                <a href="#features" class="hover:text-white transition">HARDWARE</a>
                <a href="#os" class="hover:text-white transition">APEX OS</a>
            </div>
            <button class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2 rounded-full text-xs font-bold transition">ORDER NOW</button>
        </div>
    </nav>

    <section class="h-screen flex items-center justify-center hero-gradient relative px-6">
        <div class="text-center z-10 reveal" id="heroText">
            <p class="text-blue-500 font-bold tracking-[0.4em] text-xs mb-4">AUTOPILOT PERFORMANCE</p>
            <h1 class="text-6xl md:text-8xl font-bold mb-6 tracking-tight">Fuel Your <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-blue-600">Potential.</span></h1>
            <p class="text-white/40 max-w-xl mx-auto text-lg mb-10">The world's first predictive nutrient system. Apex One learns your daily rhythm and automates your essential intake.</p>
            <div class="flex flex-col md:flex-row justify-center gap-4">
                <a href="#modes" class="bg-white text-black px-10 py-4 rounded-full font-bold transition hover:bg-blue-500 hover:text-white">Explore Modes</a>
                <a href="#lab" class="bg-blue-600/20 text-blue-400 border border-blue-600/30 px-10 py-4 rounded-full font-bold transition hover:bg-blue-600/40">Try Smart Lab</a>
            </div>
        </div>
        <div class="absolute bottom-0 w-full h-1/2 bg-gradient-to-t from-blue-900/10 to-transparent"></div>
    </section>

    <!-- Balanced Modes Section -->
    <section id="modes" class="py-32 px-6 bg-black">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-16 reveal">
                <h2 class="text-4xl font-bold mb-4">Four Pillars of Performance</h2>
                <p class="text-white/40">The Master Cell dispenses specific essential stacks for every part of your day.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-4 gap-6">
                <div class="glass-card mode-card-energy p-8 rounded-3xl reveal">
                    <i class="fas fa-bolt text-orange-500 text-2xl mb-4"></i>
                    <h3 class="font-bold text-orange-500 mb-2">ENERGY</h3>
                    <p class="text-white/40 text-sm">Caffeine anhydrous + B-Complex for instant metabolic arousal.</p>
                </div>
                <div class="glass-card mode-card-focus p-8 rounded-3xl reveal" style="transition-delay: 0.1s;">
                    <i class="fas fa-brain text-purple-500 text-2xl mb-4"></i>
                    <h3 class="font-bold text-purple-500 mb-2">FOCUS</h3>
                    <p class="text-white/40 text-sm">L-Theanine + Magnesium for calm, jitter-free cognitive endurance.</p>
                </div>
                <div class="glass-card mode-card-hydrate p-8 rounded-3xl reveal" style="transition-delay: 0.2s;">
                    <i class="fas fa-tint text-sky-400 text-2xl mb-4"></i>
                    <h3 class="font-bold text-sky-400 mb-2">HYDRATE</h3>
                    <p class="text-white/40 text-sm">Rapid-rehydration electrolytes and pH-balancing trace salts.</p>
                </div>
                <div class="glass-card mode-card-recovery p-8 rounded-3xl reveal" style="transition-delay: 0.3s;">
                    <i class="fas fa-heartbeat text-green-500 text-2xl mb-4"></i>
                    <h3 class="font-bold text-green-500 mb-2">RECOVERY</h3>
                    <p class="text-white/40 text-sm">Zinc + Vitamin C shield to support post-exertion repair.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ✨ SMART PERFORMANCE LAB (GEMINI API) -->
    <section id="lab" class="py-32 px-6 bg-white/5">
        <div class="max-w-4xl mx-auto">
            <div class="text-center mb-16 reveal">
                <p class="text-blue-500 font-bold tracking-[0.2em] text-xs mb-2">POWERED BY GEMINI AI</p>
                <h2 class="text-5xl font-bold mb-6">Smart Lab.</h2>
                <p class="text-white/40 text-lg">Describe your routine and let Apex OS automate your protocol.</p>
            </div>
            
            <div class="glass-card p-10 rounded-[3rem] reveal">
                <textarea id="labPrompt" class="w-full bg-transparent text-white border-b border-white/10 pb-4 mb-8 focus:outline-none text-xl resize-none" placeholder="e.g., I'm running a marathon at 6am and then have a high-stakes meeting at 2pm..."></textarea>
                <div class="flex justify-between items-center">
                    <button id="genLabBtn" onclick="generateProtocol()" class="bg-blue-600 text-white px-10 py-4 rounded-2xl font-bold text-sm tracking-widest hover:bg-blue-500 transition">GENERATE PROTOCOL</button>
                    <div id="labLoading" class="hidden"><div class="loader"></div></div>
                </div>

                <div id="labResponse" class="hidden pt-10 space-y-6">
                    <div class="p-6 bg-white/5 rounded-3xl border border-white/5">
                        <p id="responseText" class="text-sm text-white/60 leading-relaxed italic"></p>
                    </div>
                    <div class="grid grid-cols-4 gap-4">
                        <div class="p-4 bg-white/5 rounded-2xl text-center"><p class="text-[10px] opacity-30">ENERGY</p><p id="st-e" class="text-xs font-bold text-orange-500">--</p></div>
                        <div class="p-4 bg-white/5 rounded-2xl text-center"><p class="text-[10px] opacity-30">FOCUS</p><p id="st-f" class="text-xs font-bold text-purple-500">--</p></div>
                        <div class="p-4 bg-white/5 rounded-2xl text-center"><p class="text-[10px] opacity-30">VITAMINS</p><p id="st-v" class="text-xs font-bold text-green-500">--</p></div>
                        <div class="p-4 bg-white/5 rounded-2xl text-center"><p class="text-[10px] opacity-30">HYDRATE</p><p id="st-h" class="text-xs font-bold text-sky-400">--</p></div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="features" class="py-32 px-6 max-w-7xl mx-auto">
        <div class="grid md:grid-cols-2 gap-20 items-center">
            <div class="reveal">
                <h2 class="text-4xl font-bold mb-6">The Smart <br>Master Cell.</h2>
                <p class="text-white/50 text-lg mb-8">A single, secure-threaded cartridge containing all seven essentials. Using NFC authentication, Apex One identifies your nutrient levels and dispenses exactly what you need through precision micro-valves.</p>
                <div class="space-y-6">
                    <div class="flex items-start space-x-4">
                        <div class="p-3 bg-blue-600/10 rounded-lg text-blue-500"><i class="fas fa-microchip"></i></div>
                        <div>
                            <h4 class="font-bold">NFC Tracking</h4>
                            <p class="text-white/40 text-sm">Automatic depletion sensing with zero manual logging.</p>
                        </div>
                    </div>
                    <div class="flex items-start space-x-4">
                        <div class="p-3 bg-blue-600/10 rounded-lg text-blue-500"><i class="fas fa-screwdriver"></i></div>
                        <div>
                            <h4 class="font-bold">Threaded Security</h4>
                            <p class="text-white/40 text-sm">Screw-in base ensures a 100% pressure-sealed connection.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="glass-card p-12 rounded-[40px] border-white/10 text-center reveal">
                <div class="w-24 h-64 bg-black border border-white/20 rounded-full mx-auto relative overflow-hidden">
                    <div class="absolute bottom-0 w-full bg-blue-500/40" id="fluidLevel" style="height: 60%; transition: height 2s ease;"></div>
                    <div class="absolute top-1/4 w-full h-1 bg-white/10"></div>
                    <div class="absolute top-2/4 w-full h-1 bg-white/10"></div>
                    <div class="absolute top-3/4 w-full h-1 bg-white/10"></div>
                </div>
                <p class="mt-8 text-xs font-bold tracking-widest text-white/30 uppercase">Multi-Nutrient Cell Active</p>
            </div>
        </div>
    </section>

    <section id="os" class="py-32 bg-white/5">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-20 reveal">
                <h2 class="text-5xl font-bold mb-6">Your Life, Simulated.</h2>
                <p class="text-white/40 text-xl max-w-2xl mx-auto">Apex OS doesn't just react; it anticipates. It builds a nutrition timeline tailored to your unique routine.</p>
            </div>
            
            <div class="grid md:grid-cols-3 gap-8">
                <div class="glass-card p-8 rounded-3xl reveal">
                    <h3 class="text-blue-500 font-bold mb-4">01. PREDICTIVE ROUTINE</h3>
                    <p class="text-white/60">The bottle learns you. It primes **Energy** for your 8AM start and switches to **Focus** for your 2PM deep work session—all automatically.</p>
                </div>
                <div class="glass-card p-8 rounded-3xl reveal" style="transition-delay: 0.2s;">
                    <h3 class="text-blue-500 font-bold mb-4">02. OPTIONAL HEALTH SYNC</h3>
                    <p class="text-white/60">Privacy-first link to activity data. If you finish a high-intensity workout, Apex One prepares **Recovery** before you even take a sip.</p>
                </div>
                <div class="glass-card p-8 rounded-3xl reveal" style="transition-delay: 0.4s;">
                    <h3 class="text-blue-500 font-bold mb-4">03. AUTO-REPLENISH</h3>
                    <p class="text-white/60">NFC-triggered logistics. The system tracks internal consumption across all modes and ships a new Cell before you hit empty.</p>
                </div>
            </div>
        </div>
    </section>

    <footer class="py-20 border-t border-white/5 text-center">
        <div class="logo-text text-2xl font-bold tracking-[0.4em] mb-6">APEXONE</div>
        <p class="text-white/20 text-xs tracking-widest uppercase">Precision Hydration. Autopilot Performance.</p>
    </footer>

    <script>
        const apiKey = ""; // Execution environment provides key

        /**
         * ✨ Gemini API Integration - Smart Performance Lab
         */
        async function generateProtocol() {
            const prompt = document.getElementById('labPrompt').value;
            if(!prompt) return;

            const loader = document.getElementById('labLoading');
            const responseDiv = document.getElementById('labResponse');
            const textEl = document.getElementById('responseText');
            const btn = document.getElementById('genLabBtn');

            loader.classList.remove('hidden');
            responseDiv.classList.add('hidden');
            btn.disabled = true;

            try {
                const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-09-2025:generateContent?key=${apiKey}`, {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({
                        contents: [{ parts: [{ text: `User Routine: ${prompt}. Explain the Apex One nutrient protocol. End with JSON: {"e":"80%","f":"30%","v":"High","h":"800ml/hr"}` }] }],
                        systemInstruction: { parts: [{ text: "You are Apex OS Nutrition Intelligence. Provide a scientific, high-performance hydration protocol." }] }
                    })
                });

                const data = await response.json();
                const raw = data.candidates[0].content.parts[0].text;
                
                const jsonMatch = raw.match(/\{.*\}/);
                if(jsonMatch) {
                    const stats = JSON.parse(jsonMatch[0]);
                    document.getElementById('st-e').innerText = stats.e;
                    document.getElementById('st-f').innerText = stats.f;
                    document.getElementById('st-v').innerText = stats.v;
                    document.getElementById('st-h').innerText = stats.h;
                }
                textEl.innerText = raw.replace(/\{.*\}/, '').trim();
                responseDiv.classList.remove('hidden');
            } catch (e) {
                console.error(e);
            } finally {
                loader.classList.add('hidden');
                btn.disabled = false;
            }
        }

        // 1. Logo Animation
        const logo = document.getElementById('mainLogo');
        function triggerCharge() {
            logo.classList.add('charging');
            setTimeout(() => logo.classList.remove('charging'), 3000);
        }
        logo.addEventListener('mouseenter', triggerCharge);
        window.addEventListener('load', triggerCharge);

        // 2. Reveal Animations
        const reveals = document.querySelectorAll('.reveal');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('active'); });
        }, { threshold: 0.1 });
        reveals.forEach(el => observer.observe(el));

        // 3. Fluid Level Simulation
        setInterval(() => {
            const level = document.getElementById('fluidLevel');
            if (level) {
                const newHeight = Math.floor(Math.random() * 40) + 40; 
                level.style.height = `${newHeight}%`;
            }
        }, 5000);

        // 4. Smooth Anchor Scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const targetId = this.getAttribute('href');
                if (targetId === "#") return;
                e.preventDefault();
                const target = document.querySelector(targetId);
                if (target) target.scrollIntoView({ behavior: 'smooth' });
            });
        });

        window.onload = () => {
            document.querySelector('.reveal').classList.add('active');
            triggerCharge();
        }
    </script>
</body>
</html>
"""

# Render the application
# We use a large height to ensure the landing page is fully scrollable within the component
components.html(html_code, height=4500, scrolling=False)
