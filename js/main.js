// --- 1. SISTEMA DE NAVEGACIÓN PRINCIPAL ---
function showSection(id) {
    // Ocultar todos los contenidos y quitar clase activa de los botones
    document.querySelectorAll('.content-section').forEach(s => s.classList.add('hidden'));
    document.querySelectorAll('.nav-link').forEach(l => l.classList.remove('active'));

    // Mostrar la sección elegida y activar su botón
    document.getElementById(`section-${id}`).classList.remove('hidden');
    document.getElementById(`nav-${id}`).classList.add('active');

    // Hacer scroll suave hacia arriba si no estamos en dashboard
    if (id !== 'dashboard') window.scrollTo({ top: 0, behavior: 'smooth' });
}

// --- 2. TRANSICIÓN DE ESTADO (HARDENING LOCKDOWN) ---
function triggerLockdown() {
    const overlay = document.getElementById('lockdown-overlay');
    const progress = document.getElementById('progress-fill');
    overlay.classList.add('active');
    progress.style.width = '100%';

    // Simular carga y aplicar la clase state-sec al body
    setTimeout(() => {
        document.body.classList.add('state-sec');
        document.body.classList.remove('state-vuln');
        overlay.classList.remove('active');
        progress.style.width = '0%';
        updateSOCMonitor(true); // Cambiar texto de terminal del Breach Lab
    }, 2000);
}

function revertState() {
    document.body.classList.add('state-vuln');
    document.body.classList.remove('state-sec');
    updateSOCMonitor(false);
}

// --- 3. TERMINAL TIPO MÁQUINA DE ESCRIBIR EN CLOUD BREACH LAB ---
let typeInterval;
function updateSOCMonitor(isHardened) {
    const container = document.getElementById('term-content');
    if (!container) return;
    clearInterval(typeInterval);
    container.innerHTML = "";

    const linesVuln = [
        "[CRITICAL] Multi-Cloud Defender Detectó Múltiples Anomalías.",
        "Vector 1: Tokens SAS y ACLs Expuestos. Vector 2: Cuenta Snowflake sin MFA.",
        "Permisos Globales: <span class='bg-red-600/30 px-1 text-white'>Full Control / 0.0.0.0/0</span>",
        "<span class='text-red-400 font-bold'>ALERTA GLOBAL: Infraestructura vulnerable a exfiltración masiva.</span>"
    ];
    const linesSec = [
        "[INFO] Aplicando Playbook de Remediación Automática y Políticas Deny-All...",
        "[SUCCESS] Tokens Revocados. MFA Forzado. S3 Block Public Access Habilitado.",
        "Control de Acceso: <span class='bg-emerald-600/30 px-1 text-white'>IAM Roles + Network Allow-listing</span>",
        "<span class='text-emerald-400 font-bold'>ESTADO GLOBAL: Brechas cerradas. Postura de seguridad asegurada.</span>"
    ];

    const lines = isHardened ? linesSec : linesVuln;
    container.className = `font-mono text-xs md:text-sm cursor leading-relaxed min-h-[60px] md:min-h-[80px] ${isHardened ? 'text-emerald-400' : 'text-red-500'}`;

    let lineIdx = 0; let charIdx = 0; let currentStr = "";

    typeInterval = setInterval(() => {
        if (lineIdx >= lines.length) { clearInterval(typeInterval); return; }
        let line = lines[lineIdx];

        // Leer tags HTML completos para no renderizar código roto
        if (line[charIdx] === '<') {
            let endIdx = line.indexOf('>', charIdx);
            currentStr += line.substring(charIdx, endIdx + 1);
            charIdx = endIdx + 1;
        } else {
            currentStr += line.charAt(charIdx); charIdx++;
        }

        container.innerHTML = currentStr;
        if (charIdx >= line.length) { currentStr += "<br>"; lineIdx++; charIdx = 0; }
    }, 30);
}

// --- 4. CERRAR PANTALLA INTRODUCCIÓN ---
function playClickSound() {
    try {
        const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioCtx.createOscillator();
        const gainNode = audioCtx.createGain();
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(800, audioCtx.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(100, audioCtx.currentTime + 0.1);
        gainNode.gain.setValueAtTime(0.05, audioCtx.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + 0.1);
        oscillator.connect(gainNode);
        gainNode.connect(audioCtx.destination);
        oscillator.start();
        oscillator.stop(audioCtx.currentTime + 0.1);
    } catch (e) {
        // Ignorar de forma pasiva si no hay soporte o permisos
    }
}

// Global functions for SOC Controls
function enterDashboard() {
    document.getElementById('intro-screen').classList.add('dismissed');
    // Iniciar el monitor SOC al entrar
    setTimeout(() => { updateSOCMonitor(false); }, 500);
}

// --- 5. TABS INTERACTIVOS (CLI COMMANDS - SECCIÓN 2) ---
function switchTab(cloud, ev) {
    document.querySelectorAll('.tab-content').forEach(c => c.classList.add('hidden'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active', 'opacity-100'));
    document.getElementById(`code-${cloud}`).classList.remove('hidden');
    ev.target.classList.add('active', 'opacity-100');
}



// --- 7. EFECTO 3D TILT (TARJETAS DE RIESGO) ---
document.querySelectorAll('.tilt-card').forEach(card => {
    const content = card.querySelector('.tilt-content');
    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        content.style.transform = `rotateY(${x * 15}deg) rotateX(${y * -15}deg) translateZ(30px)`;
    });
    card.addEventListener('mouseleave', () => {
        content.style.transform = `rotateY(0deg) rotateX(0deg) translateZ(0px)`;
    });
});

// --- CLOUD BREACH LAB SOC LOGIC (FINAL UPDATED) ---
const incidentData = {
    microsoft: {
        title: "Microsoft AI Research (Azure SAS Token)",
        desc: "Exposición accidental de 38 TB al publicar modelos de entrenamiento en GitHub usando tokens SAS mal configurados.",
        impact: "38 TB de datos expuestos: backups, contraseñas y mensajes de Teams de empleados",
        vulnCode: "az storage container generate-sas --permissions rwl --expiry 2051-10-06",
        hardCode: "Azure RBAC + Entra ID (Delegation SAS)",
        analysis: "Fallo: El token otorgaba 'Full Control' sobre toda la cuenta en lugar de solo lectura sobre un archivo. \nSolución: Deshabilitar acceso por llave de cuenta y usar RBAC.",
        riskStatus: "Exfiltración de Datos Masivos y Ataque a la Cadena de Suministro."
    },
    att: {
        title: "AT&T / Snowflake (Identidad & MFA)",
        desc: "Exfiltración de registros debido a credenciales robadas y falta de autenticación multifactor (MFA).",
        impact: "100 millones de registros de clientes expuestos. Los atacantes entraron desde IPs no autorizadas.",
        vulnCode: "ALTER USER 'admin_data' SET MIN_MFA_DAYS = 0;\nCREATE NETWORK POLICY 'open_access' ALLOWED_IP_LIST = ('0.0.0.0/0');",
        hardCode: "MFA Obligatorio + Network Allow-listing",
        analysis: "Fallo: El MFA era opcional y la red estaba abierta a todo internet. \nSolución: Forzar MFA global y restringir acceso solo a VPCs autorizadas.",
        riskStatus: "Acceso No Autorizado por Robo de Credenciales."
    },
    latimes: {
        title: "Los Angeles Times (AWS S3)",
        desc: "Atacantes obtuvieron acceso de escritura a un bucket S3 de assets y plantaron un minero de criptomonedas.",
        impact: "Los lectores del sitio web minaron Monero para los atacantes sin saberlo mediante un script inyectado.",
        vulnCode: "aws s3api put-bucket-acl --bucket latimes-assets \n--grant-write uri=http://acs.amazonaws.com/groups/global/AllUsers",
        hardCode: "S3 Block Public Access + Content Integrity (SRI)",
        analysis: "Fallo: Permiso de 'Escritura' para 'Todo el Mundo'. \nSolución: Activar S3 Block Public Access y validar scripts con hashes SRI.",
        riskStatus: "Cryptojacking e Inyección de Código Malicioso."
    }
};

let isLabHardened = false;
let currentLab = 'microsoft';

function renderDynamicLab() {
    const data = incidentData[currentLab];
    const container = document.getElementById('dynamic-lab-container');
    const vulnClasses = isLabHardened ? "opacity-0 scale-105 pointer-events-none" : "opacity-100 scale-100 pointer-events-auto";
    const secClasses = isLabHardened ? "opacity-100 scale-100 pointer-events-auto" : "opacity-0 scale-95 pointer-events-none";

    container.innerHTML = `
        <div class="absolute inset-0 transition-opacity duration-300">
            <div id="view-vuln" class="absolute inset-0 transition-all duration-700 border border-red-500/50 bg-[#0a0202] rounded-xl p-8 flex flex-col z-20 ${vulnClasses}">
                <h4 class="text-red-500 font-bold mb-4 flex items-center gap-2 drop-shadow-[0_0_8px_rgba(239,68,68,0.8)]">⚠️ ESTADO: VULNERABLE</h4>
                <div class="overflow-y-auto mb-4 pr-2 custom-scroll">
                    <p class="leading-relaxed mb-2 text-[#cbd5e1]">
                        <strong class="text-red-400">Falla:</strong> ${data.desc}<br>
                        <strong class="text-red-400">Impacto:</strong> ${data.impact}
                    </p>
                </div>
                <div class="bg-[#050505] flex-1 p-6 rounded-xl font-mono font-bold text-red-500 border border-red-900/50 relative overflow-y-auto shadow-inner">
                    <pre class="whitespace-pre-wrap leading-loose drop-shadow-[0_0_3px_rgba(239,68,68,0.5)]">${data.vulnCode}</pre>
                </div>
            </div>

            <div id="view-sec" class="absolute inset-0 transition-all duration-700 ease-in-out rounded-xl p-8 flex flex-col z-10 ${secClasses} laser-transition shadow-[0_0_40px_rgba(16,185,129,0.3)] bg-gradient-to-br from-[#064e3b] to-[#010a13] border-2 border-emerald-500">
                <h4 class="text-emerald-400 font-bold mb-4 flex items-center gap-2 drop-shadow-[0_0_8px_rgba(16,185,129,0.8)]">🛡️ ESTADO: FORTIFICADO (HARDENING)</h4>
                <div class="overflow-y-auto mb-4 pr-2 custom-scroll">
                    <p class="leading-relaxed font-medium mb-2 text-slate-100">
                        <strong class="text-emerald-400">Riesgo Mitigado:</strong> ${data.riskStatus}<br>
                        <strong class="text-emerald-400">Análisis:</strong> ${data.analysis}
                    </p>
                </div>
                <div class="bg-[#020617] flex-1 p-6 rounded-xl font-mono font-bold text-emerald-400 border border-emerald-800/80 relative overflow-y-auto shadow-inner">
                    <pre class="whitespace-pre-wrap leading-loose drop-shadow-[0_0_3px_rgba(16,185,129,0.5)]">${data.hardCode}</pre>
                </div>
            </div>
        </div>
    `;
}

function updateLabUI() {
    // Restaurar botones a estado inactivo general
    document.querySelectorAll('.lab-btn').forEach(btn => {
        btn.classList.remove('active-vuln', 'active-sec', 'border-red-500', 'bg-red-950/40', 'border-emerald-500', 'bg-emerald-950/40', 'text-red-200', 'text-emerald-200');
        btn.classList.add('border-transparent', 'text-slate-500', 'opacity-70');
        const dot = btn.querySelector('div');
        if (dot) {
            dot.className = 'w-2 h-2 rounded-full bg-slate-600';
        }
    });

    const activeMap = { 'microsoft': 'msft', 'att': 'att', 'latimes': 'lat' };
    const shortId = activeMap[currentLab];
    const activeBtn = document.getElementById(`btn-lab-${shortId}`);

    if (activeBtn) {
        activeBtn.classList.remove('border-transparent', 'text-slate-500', 'opacity-70');
        const dot = activeBtn.querySelector('div');
        if (!isLabHardened) {
            activeBtn.classList.add('active-vuln', 'border-red-500', 'bg-red-950/40', 'text-red-200');
            if (dot) dot.className = 'w-2 h-2 rounded-full bg-red-500 animate-pulse shadow-[0_0_8px_rgba(239,68,68,0.8)]';
        } else {
            activeBtn.classList.add('active-sec', 'border-emerald-500', 'bg-emerald-950/40', 'text-emerald-200');
            if (dot) dot.className = 'w-2 h-2 rounded-full bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,0.8)]';
        }
    }
}

function switchLab(shortId) {
    const reverseMap = { 'msft': 'microsoft', 'att': 'att', 'lat': 'latimes' };
    currentLab = reverseMap[shortId] || shortId;
    isLabHardened = false; // Reset estado

    // Toggle central a estado Vulnerable
    const toggleBtn = document.getElementById('lab-remediation-btn');
    toggleBtn.innerHTML = "APLICAR HARDENING";
    toggleBtn.className = "font-display font-bold uppercase tracking-wider text-xs px-6 py-2 rounded border border-red-500 bg-red-900/40 text-red-100 hover:bg-red-700 hover:text-white transition-all shadow-[0_0_15px_rgba(239,68,68,0.5)] pointer-events-auto";

    // Reset Risk Gauge
    const needle = document.getElementById('lab-risk-needle');
    if (needle) {
        needle.style.transition = 'transform 1000ms cubic-bezier(0.34, 1.56, 0.64, 1)';
        needle.style.transform = "rotate(70deg)";
    }
    const shield = document.getElementById('shield-icon');
    if (shield) { shield.classList.add('opacity-0', 'scale-50'); shield.classList.remove('opacity-100', 'scale-100'); }

    const riskTypes = {
        'microsoft': 'RIESGO: EXCESO DE PRIVILEGIOS SAS',
        'att': 'RIESGO: IDENTIDAD SIN MFA Y RED ABIERTA',
        'latimes': 'RIESGO: ACL GLOBAL EN S3'
    };

    const statusText = document.getElementById('lab-risk-status-text');
    statusText.textContent = riskTypes[currentLab] || "CRITICAL";
    statusText.className = "text-red-500 font-bold mt-4 text-xs tracking-widest text-center transition-colors duration-500 animate-pulse z-10";

    const breachLabMain = document.getElementById('breach-lab');
    if (breachLabMain) {
        breachLabMain.className = 'glass-panel md:col-span-12 mt-4 p-0 flex flex-col relative overflow-hidden ring-1 ring-red-500/20 lab-container-vuln transition-all duration-1000 bg-[#050505]';
    }

    const scrollBar = document.getElementById('scroll-progress-bar');
    if (scrollBar) {
        scrollBar.classList.remove('bg-emerald-500');
        scrollBar.classList.add('bg-red-500');
    }

    const labContainer = document.getElementById('breach-lab-content');
    labContainer.className = 'p-6 bg-[#030303] grid grid-cols-1 md:grid-cols-10 gap-6 relative z-10 scanlines-bg transition-all duration-1000 rounded-xl border-t border-red-900/40';

    updateLabUI();
    renderDynamicLab();
}

function toggleLabRemediation() {
    if (isLabHardened) {
        // Revertir a estado vulnerable reutilizando switchLab
        switchLab(currentLab);
        return;
    }

    isLabHardened = true;
    const toggleBtn = document.getElementById('lab-remediation-btn');
    const labContainer = document.getElementById('breach-lab-content');
    const needle = document.getElementById('lab-risk-needle');
    const statusText = document.getElementById('lab-risk-status-text');

    toggleBtn.innerHTML = "REVERTIR A ESTADO VULNERABLE";
    toggleBtn.className = "font-display font-bold uppercase tracking-wider text-xs px-6 py-2 rounded border border-emerald-500 bg-emerald-900/40 text-emerald-100 hover:bg-emerald-700 transition-all shadow-[0_0_15px_rgba(16,185,129,0.5)] cursor-pointer pointer-events-auto";

    const breachLabMain = document.getElementById('breach-lab');
    if (breachLabMain) {
        breachLabMain.className = 'glass-panel md:col-span-12 mt-4 p-0 flex flex-col relative overflow-hidden transition-all duration-1000 bg-gradient-to-br from-[#064e3b] via-[#010a13] to-[#010a13] ring-2 ring-emerald-500 shadow-[0_0_30px_rgba(16,185,129,0.4)] border-2 border-emerald-500 lab-container-sec';
    }

    const scrollBar = document.getElementById('scroll-progress-bar');
    if (scrollBar) {
        scrollBar.classList.remove('bg-red-500');
        scrollBar.classList.add('bg-emerald-500');
    }

    labContainer.style.background = "";
    labContainer.className = 'p-6 grid grid-cols-1 md:grid-cols-10 gap-6 relative z-10 rounded-xl transition-all duration-1000 bg-transparent';

    needle.style.transition = 'transform 1000ms cubic-bezier(0.34, 1.56, 0.64, 1)';
    needle.style.transform = "rotate(-70deg)";
    needle.classList.add('pulse-success');
    setTimeout(() => needle.classList.remove('pulse-success'), 1500);

    const shield = document.getElementById('shield-icon');
    if (shield) { shield.classList.remove('opacity-0', 'scale-50'); shield.classList.add('opacity-100', 'scale-100'); }

    statusText.textContent = "SISTEMA FORTIFICADO (CIS/NIST)";
    statusText.className = "text-emerald-400 text-center font-bold mt-4 text-xs tracking-widest transition-colors duration-500 z-10 font-display drop-shadow-[0_0_8px_rgba(16,185,129,0.8)]";
    
    updateLabUI();
    renderDynamicLab();
}

// Iniciar lab
window.addEventListener('DOMContentLoaded', () => {
    switchLab('microsoft');

    // Configurar scroll progress bar
    window.addEventListener('scroll', () => {
        const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
        const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (winScroll / height) * 100;
        const scrollBar = document.getElementById('scroll-progress-bar');
        if (scrollBar) {
            scrollBar.style.width = scrolled + '%';
        }
    });

    // Inyectar clase glitch-alert a las alertas de riesgo del DOM cada cierto tiempo
    setInterval(() => {
        if (!isLabHardened) {
            const statusText = document.getElementById('lab-risk-status-text');
            if (statusText) {
                statusText.classList.remove('glitch-alert');
                void statusText.offsetWidth; // trigger reflow
                statusText.classList.add('glitch-alert');
            }
        }
    }, 4000);
});
