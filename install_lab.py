import os
import re

# ================================
# UPDATE INDEX.HTML
# ================================
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

breach_lab_new_html = """            <!-- SECCIÓN 5: REDISEÑO CLOUD BREACH LAB SOC -->
            <section id="breach-lab" class="glass-panel md:col-span-12 mt-4 p-0 flex flex-col relative overflow-hidden ring-1 ring-red-500/20 lab-container-vuln transition-colors duration-1000 bg-[#050505]">
                <div class="p-6 border-b border-red-900/50 bg-black/40 flex justify-between items-center relative z-10 backdrop-blur-md transition-colors duration-1000 lab-header">
                    <h2 class="text-xl font-display text-red-500 flex items-center gap-2 transition-colors duration-1000 lab-title">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z">
                            </path>
                        </svg>
                        5. Cloud Breach Lab (SOC Terminal)
                    </h2>
                    
                    <!-- Botón Interruptor Global Central (Before/After) -->
                    <button onclick="toggleLabRemediation()" id="lab-remediation-btn" class="font-display font-bold uppercase tracking-wider text-xs px-6 py-2 rounded border border-red-500 bg-red-900/40 text-red-100 hover:bg-red-700 hover:text-white transition-all shadow-[0_0_15px_rgba(239,68,68,0.5)]">
                        APLICAR HARDENING
                    </button>
                </div>

                <!-- Lista de Alertas Dinámicas (TABS) -->
                <div class="flex flex-col md:flex-row gap-2 p-4 bg-black/60 border-b border-red-900/30 relative z-10 font-mono text-xs transition-colors duration-1000 lab-tabs-container">
                    <button onclick="switchLab('msft')" id="btn-lab-msft" class="lab-btn focus:outline-none flex items-center justify-between w-full md:w-auto px-4 py-3 rounded border transition-all active-vuln border-red-500 bg-red-950/40 text-red-200 shadow-[0_0_10px_rgba(239,68,68,0.3)]">
                        <span>[ ALERTA ] Microsoft AI</span>
                        <svg class="w-4 h-4 ml-3 flex-shrink-0 animate-pulse text-red-500 lab-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                    </button>
                    <button onclick="switchLab('att')" id="btn-lab-att" class="lab-btn focus:outline-none flex items-center justify-between w-full md:w-auto px-4 py-3 rounded border transition-all border-transparent text-slate-500 hover:bg-white/5 opacity-70">
                        <span>[ ALERTA ] AT&T / Snowflake</span>
                        <svg class="w-4 h-4 ml-3 flex-shrink-0 text-slate-600 lab-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                    </button>
                    <button onclick="switchLab('lat')" id="btn-lab-lat" class="lab-btn focus:outline-none flex items-center justify-between w-full md:w-auto px-4 py-3 rounded border transition-all border-transparent text-slate-500 hover:bg-white/5 opacity-70">
                        <span>[ ALERTA ] LA Times (S3)</span>
                        <svg class="w-4 h-4 ml-3 flex-shrink-0 text-slate-600 lab-icon" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                    </button>
                </div>

                <!-- Contenedor Principal: Split entre Código y Risk Gauge -->
                <div class="p-6 bg-[#030303] flex flex-col md:flex-row gap-6 relative z-10 scanlines-bg transition-colors duration-1000 flex-1">
                    
                    <!-- Area de Código de Casos -->
                    <div class="flex-1 relative code-display-area min-h-[300px]">
                        <!-- CASO 1: MICROSOFT -->
                        <div id="lab-content-msft" class="lab-content-pane absolute inset-0 opacity-100 pointer-events-auto transition-opacity duration-300">
                            <!-- Vista Vulnerable -->
                            <div class="lab-view-vuln absolute inset-0 transition-opacity duration-700 border border-red-500/40 bg-red-950/20 rounded-xl p-4 md:p-6 flex flex-col z-20">
                                <h4 class="text-red-500 font-bold mb-3 flex items-center gap-2">⚠️ Ataque Foco: Azure SAS Over-permissioned</h4>
                                <div class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-red-300 border border-red-900/50 lab-code-glitch relative overflow-x-auto shadow-inner">
                                    <span class="text-red-500/50"># Generando token de acceso total en lugar de un archivo</span><br>
                                    <span class="text-blue-400">az</span> storage container generate-sas \\<br>
                                    &nbsp;&nbsp;--account-name research_data --name models \\<br>
                                    &nbsp;&nbsp;<span class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded">
                                        --permissions rwl
                                        <span class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-56 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                        Da permiso de (R)ead, (W)rite y (L)ist a cualquier persona anónima con la URL.
                                        </span>
                                    </span>
                                    <span class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded ml-1 mt-2 lg:mt-0">
                                        --expiry 2033-01-01
                                        <span class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-56 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                        Token válido por 10 años. Muy difícil de auditar y revocar adecuadamente.
                                        </span>
                                    </span>
                                </div>
                            </div>
                            <!-- Vista Hardened -->
                            <div class="lab-view-sec absolute inset-0 opacity-0 pointer-events-none transition-opacity duration-700 border border-emerald-500/40 bg-emerald-950/20 rounded-xl p-4 md:p-6 flex flex-col z-10 scale-95">
                                <h4 class="text-emerald-500 font-bold mb-3 flex items-center gap-2">🛡️ Hardening: Role-Based Access Control</h4>
                                <div class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-emerald-300 border border-emerald-900/50 overflow-x-auto shadow-inner">
                                    <span class="text-emerald-500/50"># IAM: El acceso se otorga por Identidad (RBAC) sin exponer links</span><br>
                                    <span class="text-blue-400">az</span> role assignment create --assignee &lt;app-id&gt; \\<br>
                                    &nbsp;&nbsp;<span class="bg-emerald-600/40 text-emerald-100 font-bold px-1 rounded">--role "Storage Blob Data Reader"</span> \\<br>
                                    &nbsp;&nbsp;--scope /subscriptions/&lt;sub-id&gt;/...
                                </div>
                            </div>
                        </div>

                        <!-- CASO 2: SNOWFLAKE -->
                        <div id="lab-content-att" class="lab-content-pane absolute inset-0 opacity-0 pointer-events-none transition-opacity duration-300">
                            <div class="lab-view-vuln absolute inset-0 transition-opacity duration-700 border border-red-500/40 bg-red-950/20 rounded-xl p-4 md:p-6 flex flex-col z-20">
                                <h4 class="text-red-500 font-bold mb-3 flex items-center gap-2">⚠️ Ataque Foco: MFA Opcional y Red Abierta</h4>
                                <div class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-red-300 border border-red-900/50 lab-code-glitch relative overflow-x-auto shadow-inner">
                                    <span class="text-blue-400">ALTER USER</span> "analyst_user" 
                                    <span class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded ml-1">
                                        SET MIN_MFA_DAYS = 0
                                        <span class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-56 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                        Omitió el uso de MFA. Atacantes con contraseña robada entraron al data warehouse libremente.
                                        </span>
                                    </span>
                                    <br><br>
                                    <span class="text-blue-400">CREATE NETWORK POLICY</span> "public_access" <br>
                                    &nbsp;&nbsp;ALLOWED_IP_LIST = 
                                    <span class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded">
                                        ('0.0.0.0/0')
                                        <span class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-56 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                        Mala configuración del Firewall: Abre la interfaz de base de datos a TODO el internet.
                                        </span>
                                    </span>
                                </div>
                            </div>
                            <div class="lab-view-sec absolute inset-0 opacity-0 pointer-events-none transition-opacity duration-700 border border-emerald-500/40 bg-emerald-950/20 rounded-xl p-4 md:p-6 flex flex-col z-10 scale-95">
                                <h4 class="text-emerald-500 font-bold mb-3 flex items-center gap-2">🛡️ Hardening: MFA Mandatorio & Network Whitelisting</h4>
                                <div class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-emerald-300 border border-emerald-900/50 overflow-x-auto shadow-inner">
                                    <span class="text-emerald-500/50">-- Zero trust enforcing</span><br>
                                    <span class="text-blue-400">ALTER USER</span> "analyst_user" <span class="bg-emerald-600/40 text-emerald-100 font-bold px-1 rounded">SET MIN_MFA_DAYS = 1</span>;<br><br>
                                    <span class="text-blue-400">CREATE NETWORK POLICY</span> "att_only" <br>
                                    &nbsp;&nbsp;ALLOWED_IP_LIST = <span class="bg-emerald-600/40 text-emerald-100 font-bold px-1 rounded">('10.2.0.0/16')</span>;
                                </div>
                            </div>
                        </div>

                        <!-- CASO 3: LA TIMES -->
                        <div id="lab-content-lat" class="lab-content-pane absolute inset-0 opacity-0 pointer-events-none transition-opacity duration-300">
                            <div class="lab-view-vuln absolute inset-0 transition-opacity duration-700 border border-red-500/40 bg-red-950/20 rounded-xl p-4 md:p-6 flex flex-col z-20">
                                <h4 class="text-red-500 font-bold mb-3 flex items-center gap-2">⚠️ Ataque Foco: AWS S3 y ACL Global</h4>
                                <div class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-red-300 border border-red-900/50 lab-code-glitch relative overflow-x-auto shadow-inner">
                                    <span class="text-blue-400">aws</span> s3api put-bucket-acl --bucket latimes-web-assets \\<br>
                                    &nbsp;&nbsp;
                                    <span class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded mt-2">
                                        --grant-write uri=http://acs.amazonaws.com/groups/global/AllUsers
                                        <span class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-64 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                        Permite a todos (AllUsers) subir y editar los archivos HTML/JS del balde. Los atacantes inyectaron mineros web.
                                        </span>
                                    </span>
                                </div>
                            </div>
                            <div class="lab-view-sec absolute inset-0 opacity-0 pointer-events-none transition-opacity duration-700 border border-emerald-500/40 bg-emerald-950/20 rounded-xl p-4 md:p-6 flex flex-col z-10 scale-95">
                                <h4 class="text-emerald-500 font-bold mb-3 flex items-center gap-2">🛡️ Hardening: Block Public Access</h4>
                                <div class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-emerald-300 border border-emerald-900/50 overflow-x-auto shadow-inner">
                                    <span class="text-emerald-500/50"># Invalidando las ACLs en favor del control IAM</span><br>
                                    <span class="text-blue-400">aws</span> s3control put-public-access-block --account-id &lt;acct-id&gt; \\<br>
                                    &nbsp;&nbsp;<span class="bg-emerald-600/40 text-emerald-100 font-bold px-1 rounded">--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true"</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Risk Gauge (SVG Dinámico) -->
                    <div class="w-full md:w-56 flex flex-col items-center justify-center p-6 bg-black/60 rounded-xl border border-red-900/30 transition-colors duration-1000 lab-gauge-container relative overflow-hidden">
                        
                        <div class="text-xs uppercase tracking-widest text-slate-400 mb-6 font-mono font-bold z-10">System Risk Level</div>
                        
                        <div class="relative w-40 h-20 overflow-hidden z-10">
                            <!-- Arco base -->
                            <svg class="w-full h-full" viewBox="0 0 100 50">
                                <path d="M 5 50 A 45 45 0 0 1 95 50" fill="none" stroke="#222" stroke-width="10" stroke-linecap="round"></path>
                                <!-- Sección Verde (Safe) -->
                                <path d="M 5 50 A 45 45 0 0 1 50 5" fill="none" class="stroke-emerald-600" stroke-width="10" opacity="0.9"></path>
                                <!-- Sección Roja (Critical) -->
                                <path d="M 50 5 A 45 45 0 0 1 95 50" fill="none" class="stroke-red-600" stroke-width="10" opacity="0.9"></path>
                            </svg>
                            <!-- Pila Pivot/Aguja -->
                            <div id="lab-risk-needle" class="absolute bottom-0 left-1/2 w-[3px] h-[45px] bg-[#ddd] rounded-full origin-bottom -translate-x-1/2 transition-transform duration-1000 ease-[cubic-bezier(0.34,1.56,0.64,1)] shadow-md z-10" style="transform: rotate(70deg);"></div>
                            <div class="absolute bottom-0 left-1/2 w-4 h-4 bg-slate-200 rounded-full -translate-x-1/2 translate-y-[40%] z-20 shadow-lg border border-slate-900"></div>
                        </div>
                        
                        <div id="lab-risk-status-text" class="text-red-500 font-bold font-mono mt-4 text-base tracking-widest transition-colors duration-500 animate-pulse z-10">CRITICAL</div>

                        <!-- Scanline sutil que cruza solo por detrás del medidor -->
                        <div class="absolute inset-0 scanline-element pointer-events-none opacity-30"></div>
                    </div>

                </div>
            </section>
"""

# Usar Regex para extraer la sección breach-lab vieja y reemplazar
pattern = r'<!-- SECCIÓN 5: CLOUD BREACH LAB.*?</section>'
html = re.sub(pattern, breach_lab_new_html, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# ================================
# UPDATE CSS
# ================================
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

soc_css = """
/* SOC Breach Lab Redesign */
.scanlines-bg {
    background-image: repeating-linear-gradient(
        0deg,
        rgba(0,0,0,0.15),
        rgba(0,0,0,0.15) 1px,
        transparent 1px,
        transparent 2px
    );
    background-size: 100% 2px;
}

.scanline-element {
    background: linear-gradient(to bottom, transparent 50%, rgba(239, 68, 68, 0.1) 51%, transparent 100%);
    background-size: 100% 4px;
    animation: scanlineScroll 6s linear infinite;
}

@keyframes scanlineScroll {
    0% { transform: translateY(-100%); }
    100% { transform: translateY(100%); }
}

.lab-code-glitch span {
    animation: textFlicker 4s infinite step-end;
}

@keyframes textFlicker {
    0%, 100% { opacity: 1; }
    98% { opacity: 0.8; }
    99% { opacity: 0.5; }
}

/* Hardened State Lab Variations */
.lab-container-sec {
    background-color: #022c22 !important; /* emerald-950/30 */
    box-shadow: inset 0 0 50px rgba(16, 185, 129, 0.1);
}

.lab-view-sec {
    transform: scale(1) !important;
}

.lab-view-vuln {
    opacity: 0 !important;
    pointer-events: none;
    transform: scale(1.05);
}

.active-sec {
    border-color: #10b981 !important;
    background-color: rgba(16, 185, 129, 0.2) !important;
    color: #a7f3d0 !important;
    box-shadow: 0 0 10px rgba(16, 185, 129, 0.2) !important;
}
"""
with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(css + "\\n" + soc_css)


# ================================
# UPDATE JS
# ================================
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Quitar la seccion vieja de switchLab (porque vamos a reescribirla con logica nueva)
# Simple reemplazo
js = re.sub(r'function switchLab\(.*?\}', '', js, flags=re.DOTALL)

soc_js = """
// --- CLOUD BREACH LAB SOC LOGIC ---
let isLabHardened = false;
let currentLab = 'msft';

function updateLabUI() {
    // Buttons state
    document.querySelectorAll('.lab-btn').forEach(btn => {
        btn.classList.remove('active-vuln', 'active-sec', 'border-red-500', 'bg-red-950/40', 'border-emerald-500', 'bg-emerald-950/40', 'text-red-200', 'text-emerald-200');
        btn.classList.add('border-transparent', 'text-slate-500', 'opacity-70');
        btn.querySelector('.lab-icon').innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>'; // Warning SVG
        btn.querySelector('.lab-icon').classList.remove('text-red-500', 'text-emerald-500', 'animate-pulse');
        btn.querySelector('.lab-icon').classList.add('text-slate-600');
    });

    const activeBtn = document.getElementById(`btn-lab-${currentLab}`);
    if(activeBtn) {
        activeBtn.classList.remove('border-transparent', 'text-slate-500', 'opacity-70');
        if(!isLabHardened) {
            activeBtn.classList.add('active-vuln', 'border-red-500', 'bg-red-950/40', 'text-red-200');
            activeBtn.querySelector('.lab-icon').classList.remove('text-slate-600');
            activeBtn.querySelector('.lab-icon').classList.add('text-red-500', 'animate-pulse');
        } else {
            activeBtn.classList.add('active-sec', 'border-emerald-500', 'bg-emerald-950/40', 'text-emerald-200');
            activeBtn.querySelector('.lab-icon').innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>'; // Check SVG
            activeBtn.querySelector('.lab-icon').classList.remove('text-slate-600');
            activeBtn.querySelector('.lab-icon').classList.add('text-emerald-500');
        }
    }

    // Toggle Content Panes
    document.querySelectorAll('.lab-content-pane').forEach(pane => {
        pane.classList.remove('opacity-100', 'pointer-events-auto');
        pane.classList.add('opacity-0', 'pointer-events-none');
        pane.style.zIndex = "1";
    });
    const activePane = document.getElementById(`lab-content-${currentLab}`);
    if(activePane) {
        activePane.classList.remove('opacity-0', 'pointer-events-none');
        activePane.classList.add('opacity-100', 'pointer-events-auto');
        activePane.style.zIndex = "10";
    }
}

function switchLab(labId) {
    currentLab = labId;
    isLabHardened = false; // reset state
    
    // Reset global toggle button UI
    const toggleBtn = document.getElementById('lab-remediation-btn');
    toggleBtn.innerHTML = "APLICAR HARDENING";
    toggleBtn.className = "font-display font-bold uppercase tracking-wider text-xs px-6 py-2 rounded border border-red-500 bg-red-900/40 text-red-100 hover:bg-red-700 hover:text-white transition-all shadow-[0_0_15px_rgba(239,68,68,0.5)]";
    
    // Reset gauge & container
    document.getElementById('lab-risk-needle').style.transform = "rotate(70deg)";
    document.getElementById('lab-risk-status-text').textContent = "CRITICAL";
    document.getElementById('lab-risk-status-text').className = "text-red-500 font-bold font-mono mt-4 text-base tracking-widest transition-colors duration-500 animate-pulse z-10";
    
    const labContainer = document.getElementById('breach-lab');
    labContainer.classList.remove('ring-emerald-500/20', 'bg-[#022c22]');
    labContainer.classList.add('ring-red-500/20', 'bg-[#050505]');
    
    // Lab UI
    updateLabUI();
    
    // Toggle View (Vuln vs Sec)
    document.querySelectorAll('.lab-view-sec').forEach(v => {
        v.classList.remove('opacity-100', 'pointer-events-auto', 'scale-100');
        v.classList.add('opacity-0', 'pointer-events-none', 'scale-95');
    });
    document.querySelectorAll('.lab-view-vuln').forEach(v => {
        v.classList.remove('opacity-0', 'pointer-events-none', 'scale-105');
        v.classList.add('opacity-100', 'pointer-events-auto', 'scale-100');
    });
}

function toggleLabRemediation() {
    isLabHardened = !isLabHardened;
    const toggleBtn = document.getElementById('lab-remediation-btn');
    const labContainer = document.getElementById('breach-lab');
    const needle = document.getElementById('lab-risk-needle');
    const statusText = document.getElementById('lab-risk-status-text');

    if(isLabHardened) {
        toggleBtn.innerHTML = "HARDENED / SECURED";
        toggleBtn.className = "font-display font-bold uppercase tracking-wider text-xs px-6 py-2 rounded border border-emerald-500 bg-emerald-900/40 text-emerald-100 hover:bg-emerald-700 hover:text-white transition-all shadow-[0_0_15px_rgba(16,185,129,0.5)] pointer-events-none";
        
        labContainer.classList.add('ring-emerald-500/20', 'bg-[#022c22]');
        labContainer.classList.remove('ring-red-500/20', 'bg-[#050505]');
        
        needle.style.transform = "rotate(-70deg)";
        statusText.textContent = "SAFE";
        statusText.className = "text-emerald-500 font-bold font-mono mt-4 text-base tracking-widest transition-colors duration-500 z-10";

        // Vistas
        const activePane = document.getElementById(`lab-content-${currentLab}`);
        if(activePane){
            const viewSec = activePane.querySelector('.lab-view-sec');
            const viewVuln = activePane.querySelector('.lab-view-vuln');
            if(viewVuln) {
                viewVuln.classList.add('opacity-0', 'pointer-events-none', 'scale-105');
                viewVuln.classList.remove('opacity-100', 'pointer-events-auto', 'scale-100');
            }
            if(viewSec) {
                viewSec.classList.remove('opacity-0', 'pointer-events-none', 'scale-95');
                viewSec.classList.add('opacity-100', 'pointer-events-auto', 'scale-100');
            }
        }
    }
    updateLabUI();
}

// Check touch support to prevent Tilt 3D jumping on mobiles
if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
    document.querySelectorAll('.tilt-card').forEach(card => {
        // Remove or alter event listeners
        const content = card.querySelector('.tilt-content');
        if(content) content.style.transform = 'translateZ(0px)';
        // Reset and remove tilt behavior for touch screens completely
        const clone = card.cloneNode(true);
        card.parentNode.replaceChild(clone, card); 
    });
}
"""

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js + "\\n" + soc_js)

print("Installation Complete.")
