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



// --- EFECTO 3D TILT CON BRILLO DINÁMICO ---
document.querySelectorAll('.tilt-card').forEach(card => {
    const content = card.querySelector('.tilt-content');

    // Crear el elemento de brillo (glare)
    const glare = document.createElement('div');
    glare.className = 'glare-effect absolute inset-0 pointer-events-none rounded-xl opacity-0 transition-opacity duration-300';
    glare.style.background = 'radial-gradient(circle at 50% 50%, rgba(255,255,255,0.1) 0%, transparent 60%)';
    content.appendChild(glare);

    card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left; // Posición X del ratón en la tarjeta
        const y = e.clientY - rect.top;  // Posición Y del ratón en la tarjeta

        // Rotación
        const rotX = ((x / rect.width) - 0.5) * 20; // Max 20 grados
        const rotY = ((y / rect.height) - 0.5) * -20;

        content.style.transform = `rotateY(${rotX}deg) rotateX(${rotY}deg) translateZ(30px)`;

        // Mover el brillo
        glare.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(255,255,255,0.15) 0%, transparent 60%)`;
        glare.style.opacity = '1';
    });

    card.addEventListener('mouseleave', () => {
        content.style.transform = `rotateY(0deg) rotateX(0deg) translateZ(0px)`;
        glare.style.opacity = '0';
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



function updateLabUI() {
    // Resetear botones
    document.querySelectorAll('.lab-btn').forEach(btn => {
        btn.classList.remove('active-vuln', 'active-sec', 'border-red-500', 'bg-red-950/40', 'border-emerald-500', 'bg-emerald-950/40', 'text-red-200', 'text-emerald-200');
        btn.classList.add('border-transparent', 'text-slate-500', 'opacity-70');
        const dotContainer = btn.querySelector('.flex.items-center.gap-2');
        if (dotContainer) dotContainer.innerHTML = '<div class="w-1.5 h-1.5 rounded-full bg-slate-600"></div>';
    });

    const activeMap = { 'microsoft': 'msft', 'att': 'att', 'latimes': 'lat', 'msft': 'msft', 'lat': 'lat' };
    const shortId = activeMap[currentLab] || currentLab;
    const activeBtn = document.getElementById(`btn-lab-${shortId}`);

    // Iluminar botón activo
    if (activeBtn) {
        activeBtn.classList.remove('border-transparent', 'text-slate-500', 'opacity-70');
        const dotContainer = activeBtn.querySelector('.flex.items-center.gap-2');
        if (!isLabHardened) {
            activeBtn.classList.add('active-vuln', 'border-red-500', 'bg-red-950/40', 'text-red-200');
            if (dotContainer) dotContainer.innerHTML = '<span class="text-[10px] text-red-400 opacity-80 uppercase tracking-widest hidden xl:inline-block">Activo</span><div class="w-2.5 h-2.5 rounded-full bg-red-500 animate-pulse shadow-[0_0_8px_rgba(239,68,68,1)]"></div>';
        } else {
            activeBtn.classList.add('active-sec', 'border-emerald-500', 'bg-emerald-950/40', 'text-emerald-200');
            if (dotContainer) dotContainer.innerHTML = '<span class="text-[10px] text-emerald-400 opacity-80 uppercase tracking-widest hidden xl:inline-block">Seguro</span><div class="w-2.5 h-2.5 rounded-full bg-emerald-500 shadow-[0_0_8px_rgba(16,185,129,1)]"></div>';
        }
    }

    // CONTROL DE VISIBILIDAD DE LOS CASOS
    document.querySelectorAll('.lab-content-pane').forEach(pane => {
        pane.classList.add('opacity-0', 'pointer-events-none');
        pane.classList.remove('opacity-100', 'pointer-events-auto');
    });

    const activePane = document.getElementById(`lab-content-${shortId}`);
    if (activePane) {
        activePane.classList.remove('opacity-0', 'pointer-events-none');
        activePane.classList.add('opacity-100', 'pointer-events-auto');

        // Manejar sub-vistas (Vulnerable vs Seguro) dentro del panel
        const viewVuln = activePane.querySelector('.lab-view-vuln');
        const viewSec = activePane.querySelector('.lab-view-sec');

        if (isLabHardened) {
            viewVuln.classList.add('opacity-0', 'pointer-events-none', 'scale-105');
            viewVuln.classList.remove('opacity-100', 'pointer-events-auto', 'scale-100');
            viewSec.classList.add('opacity-100', 'pointer-events-auto', 'scale-100');
            viewSec.classList.remove('opacity-0', 'pointer-events-none', 'scale-95');
        } else {
            viewVuln.classList.add('opacity-100', 'pointer-events-auto', 'scale-100');
            viewVuln.classList.remove('opacity-0', 'pointer-events-none', 'scale-105');
            viewSec.classList.add('opacity-0', 'pointer-events-none', 'scale-95');
            viewSec.classList.remove('opacity-100', 'pointer-events-auto', 'scale-100');
        }
    }
}
function switchLab(shortId) {
    const reverseMap = { 'msft': 'microsoft', 'att': 'att', 'lat': 'latimes' };
    currentLab = reverseMap[shortId] || shortId;
    isLabHardened = false;

    // Reset de estilos del botón de remediación
    const toggleBtn = document.getElementById('lab-remediation-btn');
    toggleBtn.innerHTML = "APLICAR HARDENING";
    toggleBtn.className = "font-display font-bold uppercase px-8 py-3 rounded border border-red-500 bg-red-950/60 text-red-100 hover:bg-red-600 hover:text-white transition-all shadow-[0_0_15px_rgba(239,68,68,0.4)] pointer-events-auto flex items-center gap-2 group text-[0.95rem]";

    // Reset del medidor de riesgo
    document.getElementById('lab-risk-needle').style.transform = "rotate(65deg)";
    document.getElementById('lab-risk-status-text').textContent = "CRITICAL RISK";
    document.getElementById('lab-risk-status-text').className = "text-red-500 font-bold font-mono mt-6 tracking-widest transition-colors duration-500 animate-pulse z-10 text-center text-xl";

    updateLabUI(); // Solo actualizamos visibilidad
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

    if (isLabHardened) {
        toggleBtn.innerHTML = "SISTEMA SEGURO / FORTIFICADO";
        toggleBtn.className = "font-display font-bold uppercase tracking-wider text-xs px-6 py-2 rounded border border-emerald-500 bg-emerald-900/40 text-emerald-100 shadow-[0_0_15px_rgba(16,185,129,0.5)] cursor-not-allowed pointer-events-none";

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
    }
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

// --- ANIMACIONES DE REVELACIÓN AL SCROLL ---
document.addEventListener("DOMContentLoaded", () => {
    const observerOptions = {
        root: null,
        rootMargin: '0px',
        threshold: 0.15 // El elemento aparece cuando el 15% es visible
    };

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('is-visible');
                // Opcional: dejar de observar una vez que aparece
                // observer.unobserve(entry.target); 
            }
        });
    }, observerOptions);

    // Seleccionamos qué elementos queremos animar
    const elementsToAnimate = document.querySelectorAll('.glass-panel, .tilt-card, section h2');

    elementsToAnimate.forEach(el => {
        el.classList.add('fade-in-section');
        observer.observe(el);
    });
});

// --- ANIMACIÓN DE CONTADORES NUMÉRICOS EN TEXTO ---
function initTextCounters() {
    const counters = document.querySelectorAll('.counter');
    const speed = 60; // Ajusta este valor para hacer la cuenta más lenta o rápida

    // Darle tiempo a la animación reveal-text de CSS para que termine antes de empezar a contar
    setTimeout(() => {
        counters.forEach(counter => {
            const updateCount = () => {
                const target = +counter.getAttribute('data-target');
                const count = +counter.innerText;

                // Calculamos el incremento
                const inc = target / speed;

                if (count < target) {
                    // Sumamos y redondeamos para no mostrar decimales
                    counter.innerText = Math.ceil(count + inc);
                    setTimeout(updateCount, 30); // 30ms por frame
                } else {
                    counter.innerText = target; // Asegurarnos de terminar en el número exacto
                }
            };

            updateCount();
        });
    }, 1200); // 1.2 segundos de retraso esperando que el panel inicial se muestre
}

// Ejecutar cuando se cargue el DOM
document.addEventListener('DOMContentLoaded', () => {
    initTextCounters();
});

// --- FUNCIONALIDAD DE COPIAR CÓDIGO ---
function copyTerminalCode() {
    // Buscar qué pestaña está visible actualmente
    const activeTab = document.querySelector('.tab-content:not(.hidden)');
    if (!activeTab) return;

    // Extraer solo el texto (sin las etiquetas span de HTML)
    const codeText = activeTab.innerText;

    // Copiar al portapapeles
    navigator.clipboard.writeText(codeText).then(() => {
        // Feedback visual
        const copyBtn = document.getElementById('copyBtn');
        const copyText = document.getElementById('copyText');

        copyText.innerText = "¡Copiado!";
        copyBtn.classList.add('text-emerald-400', 'border-emerald-400/50');

        // Volver a la normalidad después de 2 segundos
        setTimeout(() => {
            copyText.innerText = "Copiar";
            copyBtn.classList.remove('text-emerald-400', 'border-emerald-400/50');
        }, 2000);
    }).catch(err => {
        console.error('Error al copiar: ', err);
    });
}