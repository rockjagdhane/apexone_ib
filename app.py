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
            scroll-behavior: smooth;
            margin: 0;
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
    </style>
</head>
<body>

    <!-- Navigation -->
    <nav class="fixed w-full z-50 bg-black/70 backdrop-blur-lg border-b border-white/5">
        <div class="max-w-7xl mx-auto px-6 py-4 flex justify-between items-center">
            <div id="mainLogo" class="logo-text text-xl font-bold tracking-[0.2em] cursor-pointer">
                <span>A</span><span>P</span><span>E</span><span>X</span><span>O</span><span>N</span><span>E</span>
            </div>
            <div class="hidden md:flex space-x-8 text-sm font-medium tracking-widest text-white/60">
                <a href="#modes" class="hover:text-white transition">MODES</a>
                <a href="#features" class="hover:text-white transition">HARDWARE</a>
                <a href="#os" class="hover:text-white transition">APEX OS</a>
                <a href="#subscription" class="hover:text-white transition">SUBSCRIPTION</a>
            </div>
            <button class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2 rounded-full text-xs font-bold transition">ORDER NOW</button>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="min-h-screen flex items-center justify-center hero-gradient relative px-6 pt-20">
        <div class="text-center z-10 reveal w-full max-w-4xl mx-auto" id="heroText">
            <p class="text-blue-500 font-bold tracking-[0.4em] text-xs mb-4">AUTOPILOT PERFORMANCE</p>
            <h1 class="text-5xl md:text-8xl font-bold mb-6 tracking-tight leading-tight">Fuel Your <br><span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-blue-600">Potential.</span></h1>
            <p class="text-white/40 max-w-xl mx-auto text-lg md:text-xl mb-10">The world's first predictive nutrient system. Apex One learns your daily rhythm and automates your essential intake.</p>
            <div class="flex flex-col md:flex-row justify-center items-center gap-4">
                <a href="#modes" class="bg-white text-black px-10 py-4 rounded-full font-bold transition hover:bg-blue-500 hover:text-white w-full md:w-auto">Explore Modes</a>
                <a href="#features" class="bg-transparent border border-white/20 text-white px-10 py-4 rounded-full font-bold transition hover:bg-white hover:text-black w-full md:w-auto">View Hardware</a>
            </div>
        </div>
        <div class="absolute bottom-10 left-1/2 -translate-x-1/2 animate-bounce opacity-20">
            <i class="fas fa-chevron-down text-2xl"></i>
        </div>
        <div class="absolute bottom-0 w-full h-1/2 bg-gradient-to-t from-blue-900/10 to-transparent pointer-events-none"></div>
    </section>

    <!-- Balanced Modes Section -->
    <section id="modes" class="py-32 px-6 bg-black">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-16 reveal">
                <h2 class="text-4xl font-bold mb-4">Four Pillars of Performance</h2>
                <p class="text-white/40">The Master Cell dispenses specific essential stacks for every part of your day.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <div class="glass-card mode-card-energy p-10 rounded-3xl reveal">
                    <i class="fas fa-bolt text-orange-500 text-3xl mb-6"></i>
                    <h3 class="font-bold text-orange-500 text-xl mb-3">ENERGY</h3>
                    <p class="text-white/40 text-sm leading-relaxed">Caffeine anhydrous + B-Complex for instant metabolic arousal and sharp focus.</p>
                </div>
                <div class="glass-card mode-card-focus p-10 rounded-3xl reveal" style="transition-delay: 0.1s;">
                    <i class="fas fa-brain text-purple-500 text-3xl mb-6"></i>
                    <h3 class="font-bold text-purple-500 text-xl mb-3">FOCUS</h3>
                    <p class="text-white/40 text-sm leading-relaxed">L-Theanine + Magnesium for calm, jitter-free cognitive endurance during deep work.</p>
                </div>
                <div class="glass-card mode-card-hydrate p-10 rounded-3xl reveal" style="transition-delay: 0.2s;">
                    <i class="fas fa-tint text-sky-400 text-3xl mb-6"></i>
                    <h3 class="font-bold text-sky-400 text-xl mb-3">HYDRATE</h3>
                    <p class="text-white/40 text-sm leading-relaxed">Rapid-rehydration electrolytes and pH-balancing trace salts for all-day baseline health.</p>
                </div>
                <div class="glass-card mode-card-recovery p-10 rounded-3xl reveal" style="transition-delay: 0.3s;">
                    <i class="fas fa-heartbeat text-green-500 text-3xl mb-6"></i>
                    <h3 class="font-bold text-green-500 text-xl mb-3">RECOVERY</h3>
                    <p class="text-white/40 text-sm leading-relaxed">Zinc + Vitamin C shield to support post-exertion repair and immune system stability.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Hardware Section -->
    <section id="features" class="py-32 px-6 max-w-7xl mx-auto">
        <div class="grid md:grid-cols-2 gap-20 items-center">
            <div class="reveal">
                <h2 class="text-4xl md:text-5xl font-bold mb-6">The Smart <br>Master Cell.</h2>
                <p class="text-white/50 text-lg mb-8 leading-relaxed">A single, secure-threaded cartridge containing all seven essentials. Using NFC authentication, Apex One identifies your nutrient levels and dispenses exactly what you need through precision micro-valves.</p>
                <div class="space-y-8">
                    <div class="flex items-start space-x-6">
                        <div class="p-4 bg-blue-600/10 rounded-2xl text-blue-500"><i class="fas fa-microchip text-xl"></i></div>
                        <div>
                            <h4 class="font-bold text-xl mb-1">NFC Tracking</h4>
                            <p class="text-white/40 text-sm">Automatic depletion sensing with zero manual logging. The app knows before you do.</p>
                        </div>
                    </div>
                    <div class="flex items-start space-x-6">
                        <div class="p-4 bg-blue-600/10 rounded-2xl text-blue-500"><i class="fas fa-screwdriver text-xl"></i></div>
                        <div>
                            <h4 class="font-bold text-xl mb-1">Threaded Security</h4>
                            <p class="text-white/40 text-sm">Screw-in base ensures a 100% pressure-sealed connection for consistent micro-dosing.</p>
                        </div>
                    </div>
                </div>
            </div>
            <div class="glass-card p-12 rounded-[40px] border-white/10 text-center reveal flex flex-col items-center">
                <div class="w-32 h-80 bg-black border border-white/20 rounded-full relative overflow-hidden shadow-2xl">
                    <div class="absolute bottom-0 w-full bg-blue-500/40" id="fluidLevel" style="height: 60%; transition: height 2s ease;"></div>
                    <div class="absolute top-1/4 w-full h-1 bg-white/5"></div>
                    <div class="absolute top-2/4 w-full h-1 bg-white/5"></div>
                    <div class="absolute top-3/4 w-full h-1 bg-white/5"></div>
                    <div class="absolute inset-0 flex flex-col justify-center items-center opacity-20 text-[8px] font-bold tracking-widest text-white">
                        <p class="mb-2">VITAMINS</p>
                        <p class="mb-2">ENERGY</p>
                        <p class="mb-2">ELECTROLYTES</p>
                        <p>IMMUNE</p>
                    </div>
                </div>
                <p class="mt-8 text-xs font-bold tracking-widest text-blue-500 uppercase">NFC MASTER CELL AUTHENTICATED</p>
            </div>
        </div>
    </section>

    <!-- OS Section -->
    <section id="os" class="py-32 bg-white/5">
        <div class="max-w-7xl mx-auto px-6">
            <div class="text-center mb-20 reveal">
                <h2 class="text-5xl font-bold mb-6">Your Life, Simulated.</h2>
                <p class="text-white/40 text-xl max-w-2xl mx-auto">Apex OS doesn't just react; it anticipates. It builds a nutrition timeline tailored to your unique daily routine.</p>
            </div>
            
            <div class="grid md:grid-cols-3 gap-8">
                <div class="glass-card p-10 rounded-3xl reveal">
                    <div class="text-blue-500 text-3xl font-bold mb-6">01</div>
                    <h3 class="text-white font-bold text-xl mb-4">PREDICTIVE ROUTINE</h3>
                    <p class="text-white/40 leading-relaxed">The bottle learns you. It primes **Energy** for your 8AM start and switches to **Focus** for your 2PM deep work session—all automatically.</p>
                </div>
                <div class="glass-card p-10 rounded-3xl reveal" style="transition-delay: 0.2s;">
                    <div class="text-blue-500 text-3xl font-bold mb-6">02</div>
                    <h3 class="text-white font-bold text-xl mb-4">OPTIONAL HEALTH SYNC</h3>
                    <p class="text-white/40 leading-relaxed">Privacy-first link to activity data. If you finish a high-intensity workout, Apex One prepares **Recovery** before you even take a sip.</p>
                </div>
                <div class="glass-card p-10 rounded-3xl reveal" style="transition-delay: 0.4s;">
                    <div class="text-blue-500 text-3xl font-bold mb-6">03</div>
                    <h3 class="text-white font-bold text-xl mb-4">AUTO-REPLENISH</h3>
                    <p class="text-white/40 leading-relaxed">NFC-triggered logistics. The system tracks internal consumption across all modes and ships a new Cell before you hit empty.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Subscription Section -->
    <section id="subscription" class="py-32 px-6">
        <div class="max-w-4xl mx-auto text-center reveal">
            <h2 class="text-4xl md:text-5xl font-bold mb-10">Choose Your Performance.</h2>
            <div class="grid md:grid-cols-2 gap-8">
                <div class="glass-card p-10 rounded-[40px] border-white/5 flex flex-col text-left">
                    <h3 class="text-2xl font-bold mb-2">Apex Standard</h3>
                    <p class="text-white/30 mb-8 italic">Core Performance Tier</p>
                    <ul class="space-y-4 mb-12 text-white/60 text-sm flex-grow">
                        <li class="flex items-center"><i class="fas fa-check text-blue-500 mr-3"></i> Manual Dial Mode Control</li>
                        <li class="flex items-center"><i class="fas fa-check text-blue-500 mr-3"></i> Basic Hydration Tracking</li>
                        <li class="flex items-center"><i class="fas fa-check text-blue-500 mr-3"></i> Static White Logo LED</li>
                        <li class="flex items-center opacity-40"><i class="fas fa-times mr-3"></i> No Health Sync</li>
                    </ul>
                    <button class="w-full py-4 border border-white/20 rounded-2xl font-bold hover:bg-white hover:text-black transition">Current Tier</button>
                </div>
                <div class="glass-card p-10 rounded-[40px] border-blue-500 bg-blue-500/5 relative flex flex-col text-left">
                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-blue-600 text-white px-6 py-1 rounded-full text-[10px] font-bold tracking-widest uppercase">MOST ADVANCED</div>
                    <h3 class="text-2xl font-bold mb-2 text-blue-400">Apex Elite</h3>
                    <p class="text-blue-400/50 mb-8 font-bold">$9.99 / Month</p>
                    <ul class="space-y-4 mb-12 text-white/80 text-sm flex-grow">
                        <li class="flex items-center font-bold"><i class="fas fa-star text-blue-500 mr-3"></i> Autonomous Routine Simulation</li>
                        <li class="flex items-center"><i class="fas fa-star text-blue-500 mr-3"></i> Full Health App Predictive Mix</li>
                        <li class="flex items-center"><i class="fas fa-star text-blue-500 mr-3"></i> Autonomous Auto-Ship</li>
                        <li class="flex items-center"><i class="fas fa-star text-blue-500 mr-3"></i> 20% Off All Master Cells</li>
                    </ul>
                    <button class="w-full py-4 bg-blue-600 rounded-2xl font-bold hover:bg-blue-500 transition shadow-lg shadow-blue-500/20">Upgrade Now</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="py-24 border-t border-white/5 text-center bg-black">
        <div class="logo-text text-3xl font-bold tracking-[0.4em] mb-8">APEXONE</div>
        <p class="text-white/20 text-xs tracking-widest uppercase mb-12">Precision Hydration. Autopilot Performance.</p>
        <div class="flex justify-center space-x-10 text-white/40 text-sm mb-12">
            <a href="#" class="hover:text-white">Instagram</a>
            <a href="#" class="hover:text-white">Twitter</a>
            <a href="#" class="hover:text-white">Support</a>
        </div>
        <p class="text-white/10 text-[10px]">© 2026 APEX Performance Technology. All rights reserved.</p>
    </footer>

    <script>
        // 1. Tesla-Style Logo Battery Animation on Hover/Load
        const logo = document.getElementById('mainLogo');
        function triggerCharge() {
            const logoEl = document.getElementById('mainLogo');
            if (logoEl) {
                logoEl.classList.add('charging');
                setTimeout(() => {
                    if (logoEl) logoEl.classList.remove('charging');
                }, 3000);
            }
        }
        
        if (logo) {
            logo.addEventListener('mouseenter', triggerCharge);
        }
        window.addEventListener('load', triggerCharge);

        // 2. Reveal Animations on Scroll
        const reveals = document.querySelectorAll('.reveal');
        const observerOptions = { threshold: 0.1 };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('active');
                }
            });
        }, observerOptions);

        reveals.forEach(el => observer.observe(el));

        // 3. Fluid Level Simulation (Hardware Section)
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
                if (target) {
                    const headerOffset = 80;
                    const elementPosition = target.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });
                }
            });
        });

        // Trigger initial reveal for hero
        window.addEventListener('load', () => {
            const hero = document.getElementById('heroText');
            if (hero) {
                hero.classList.add('active');
            }
            triggerCharge();
        });
    </script>
</body>
</html>
"""

# Render the application
# We use a large height to ensure the landing page is fully scrollable within the component
components.html(html_code, height=4500, scrolling=False)
