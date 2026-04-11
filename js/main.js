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
    } catch(e) {
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

// --- CLOUD BREACH LAB SOC LOGIC ---
const incidentData = {
    microsoft: {
        title: "Microsoft AI Research (Sept 2023)",
        service: "Azure Blob Storage & SAS Tokens",
        desc: "Investigadores publicaron accidentalmente un token SAS con alcance a nivel de cuenta y permisos de control total, exponiendo datos internos en lugar de solo los modelos de IA previstos.",
        impact: "Exposición de 38 TB de datos privados, incluyendo backups de workstations y mensajes de Teams.",
        vulnCode: "# PROBLEMA (ROJO): Token SAS con permisos excesivos y larga duración\naz storage container generate-sas --permissions rwl --expiry 2033-01-01",
        hardCode: "# SOLUCIÓN (VERDE): Implementar RBAC y Azure Managed Identity\naz role assignment create --role 'Storage Blob Data Reader' --scope /subscriptions/<sub-id>/...",
        analysis: "Falla en el Mínimo Privilegio. La remediación exige eliminar el uso de tokens compartidos en favor de identidades administradas.",
        doc: "Microsoft MSRC & Wiz Research Analysis"
    },
    att: {
        title: "AT&T / Snowflake (Julio 2024)",
        service: "Snowflake Data Warehouse & IAM",
        desc: "Atacantes utilizaron credenciales robadas para acceder a entornos que no tenían la autenticación multifactor (MFA) impuesta, ni restricciones de red (Network Policies) habilitadas.",
        impact: "Exfiltración de registros de llamadas y mensajes de más de 100 millones de clientes.",
        vulnCode: "-- PROBLEMA (ROJO): MFA Opcional y acceso de red abierto a Internet\nALTER USER 'admin' SET MIN_MFA_DAYS = 0;\nCREATE NETWORK POLICY 'open' ALLOWED_IP_LIST = ('0.0.0.0/0');",
        hardCode: "-- SOLUCIÓN (VERDE): Forzar MFA obligatorio y restringir acceso a la VPC\nALTER USER 'admin' SET MIN_MFA_DAYS = 1;\nCREATE NETWORK POLICY 'att_only' ALLOWED_IP_LIST = ('10.2.0.0/16');",
        analysis: "Falla de Identidad. El endurecimiento de la configuración de acceso es responsabilidad del cliente según el Modelo de Responsabilidad Compartida.",
        doc: "Mandiant (UNC5537) & Snowflake IR Report"
    },
    latimes: {
        title: "Los Angeles Times (2018)",
        service: "Amazon S3 & ACLs",
        desc: "Un bucket de S3 que alojaba archivos JavaScript críticos fue configurado con una ACL que otorgaba permisos de escritura al grupo global 'AllUsers', permitiendo inyecciones de código malicioso.",
        impact: "Cryptojacking masivo: los navegadores de los lectores fueron secuestrados para minar criptomonedas (Monero).",
        vulnCode: "# PROBLEMA (ROJO): Permisos de escritura otorgados al mundo (AllUsers)\naws s3api put-bucket-acl --bucket assets --grant-write uri=http://acs.amazonaws.com/groups/global/AllUsers",
        hardCode: "# SOLUCIÓN (VERDE): Activar S3 Block Public Access a nivel de cuenta\naws s3control put-public-access-block --public-access-block-configuration 'BlockPublicAcls=true,BlockPublicPolicy=true'",
        analysis: "Falla de Superficie de Ataque. Las ACLs públicas son un método heredado; el hardening moderno requiere el bloqueo centralizado de acceso público.",
        doc: "AWS Security Blog: 'Amazon S3 Block Public Access'"
    }
};

let isLabHardened = false;
let currentLab = 'microsoft';

function renderDynamicLab() {
    const data = incidentData[currentLab];
    const container = document.getElementById('dynamic-lab-container');
    
    const vulnClasses = isLabHardened ? "opacity-0 pointer-events-none scale-105" : "opacity-100 pointer-events-auto scale-100";
    const secClasses = isLabHardened ? "opacity-100 pointer-events-auto scale-100" : "opacity-0 pointer-events-none scale-95";

    container.innerHTML = `
        <div class="absolute inset-0 transition-opacity duration-300">
            <div id="view-vuln" class="absolute inset-0 transition-all duration-700 border border-red-500/40 bg-red-950/20 rounded-xl p-4 md:p-6 flex flex-col z-20 ${vulnClasses}">
                <h4 class="text-red-500 font-bold mb-3 flex items-center gap-2">⚠️ ESTADO: VULNERABLE</h4>
                <div class="overflow-y-auto mb-3 pr-2 custom-scroll">
                    <p class="text-xs text-slate-300 leading-relaxed">
                        <strong class="text-red-400">Incidente:</strong> ${data.title}<br>
                        <strong class="text-red-400">Falla:</strong> ${data.desc}<br>
                        <strong class="text-red-400">Impacto:</strong> ${data.impact}
                    </p>
                </div>
                <div class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-sm text-red-300 border border-red-900/50 relative overflow-y-auto shadow-inner">
                    <pre class="whitespace-pre-wrap leading-loose">${data.vulnCode}</pre>
                </div>
            </div>

            <div id="view-sec" class="absolute inset-0 transition-all duration-700 border border-emerald-500/40 bg-emerald-950/20 rounded-xl p-4 md:p-6 flex flex-col z-10 ${secClasses}">
                <h4 class="text-emerald-500 font-bold mb-3 flex items-center gap-2">🛡️ ESTADO: FORTIFICADO (HARDENING)</h4>
                <div class="overflow-y-auto mb-3 pr-2 custom-scroll">
                    <p class="text-xs text-slate-300 leading-relaxed">
                        <strong class="text-emerald-400">Remediación:</strong> ${data.analysis}<br>
                        <strong class="text-emerald-400">Referencia:</strong> ${data.doc}
                    </p>
                </div>
                <div class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-sm text-emerald-300 border border-emerald-900/50 relative overflow-y-auto shadow-inner">
                    <pre class="whitespace-pre-wrap leading-loose">${data.hardCode}</pre>
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
        btn.querySelector('.lab-icon').innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path>';
        btn.querySelector('.lab-icon').classList.remove('text-red-500', 'text-emerald-500', 'animate-pulse');
        btn.querySelector('.lab-icon').classList.add('text-slate-600');
    });

    const activeMap = { 'microsoft': 'msft', 'att': 'att', 'latimes': 'lat' };
    const shortId = activeMap[currentLab];
    const activeBtn = document.getElementById(`btn-lab-${shortId}`);
    
    if(activeBtn) {
        activeBtn.classList.remove('border-transparent', 'text-slate-500', 'opacity-70');
        if(!isLabHardened) {
            activeBtn.classList.add('active-vuln', 'border-red-500', 'bg-red-950/40', 'text-red-200');
            activeBtn.querySelector('.lab-icon').classList.remove('text-slate-600');
            activeBtn.querySelector('.lab-icon').classList.add('text-red-500', 'animate-pulse');
        } else {
            activeBtn.classList.add('active-sec', 'border-emerald-500', 'bg-emerald-950/40', 'text-emerald-200');
            activeBtn.querySelector('.lab-icon').innerHTML = '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>';
            activeBtn.querySelector('.lab-icon').classList.remove('text-slate-600');
            activeBtn.querySelector('.lab-icon').classList.add('text-emerald-500');
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
    document.getElementById('lab-risk-needle').style.transform = "rotate(70deg)";
    
    const riskTypes = {
        'microsoft': 'RIESGO POR CONFIGURACIÓN EXCESIVA',
        'att': 'RIESGO POR FALLA DE IDENTIDAD',
        'latimes': 'RIESGO POR EXPOSICIÓN DE RED'
    };
    
    const statusText = document.getElementById('lab-risk-status-text');
    statusText.textContent = riskTypes[currentLab] || "CRITICAL";
    statusText.className = "text-red-500 font-bold mt-4 text-xs tracking-widest text-center transition-colors duration-500 animate-pulse z-10";
    
    const labContainer = document.getElementById('breach-lab');
    labContainer.classList.remove('ring-emerald-500/20', 'bg-[#022c22]');
    labContainer.classList.add('ring-red-500/20', 'bg-[#050505]');
    
    updateLabUI();
    renderDynamicLab();
}

function toggleLabRemediation() {
    isLabHardened = !isLabHardened;
    const toggleBtn = document.getElementById('lab-remediation-btn');
    const labContainer = document.getElementById('breach-lab');
    const needle = document.getElementById('lab-risk-needle');
    const statusText = document.getElementById('lab-risk-status-text');

    if(isLabHardened) {
        toggleBtn.innerHTML = "HARDENED / SECURED";
        toggleBtn.className = "font-display font-bold uppercase tracking-wider text-xs px-6 py-2 rounded border border-emerald-500 bg-emerald-900/40 text-emerald-100 hover:bg-emerald-700 hover:text-white transition-all shadow-[0_0_15px_rgba(16,185,129,0.5)] cursor-not-allowed pointer-events-none";
        
        labContainer.classList.add('ring-emerald-500/20', 'bg-[#022c22]');
        labContainer.classList.remove('ring-red-500/20', 'bg-[#050505]');
        
        needle.style.transform = "rotate(-70deg)";
        statusText.textContent = "SISTEMA SEGURO Y ENDURECIDO";
        statusText.className = "text-emerald-500 text-center font-bold mt-4 text-xs tracking-widest transition-colors duration-500 z-10";

        // Transicionar DOM
        const viewVuln = document.getElementById('view-vuln');
        const viewSec = document.getElementById('view-sec');
        if(viewVuln) {
            viewVuln.className = "absolute inset-0 transition-all duration-700 border border-red-500/40 bg-red-950/20 rounded-xl p-4 md:p-6 flex flex-col z-20 opacity-0 pointer-events-none scale-105";
        }
        if(viewSec) {
            viewSec.className = "absolute inset-0 transition-all duration-700 border border-emerald-500/40 bg-emerald-950/20 rounded-xl p-4 md:p-6 flex flex-col z-10 opacity-100 pointer-events-auto scale-100";
        }
    }
    updateLabUI();
}

// Iniciar lab
window.addEventListener('DOMContentLoaded', () => {
    switchLab('microsoft');
});

// Check touch support to prevent Tilt 3D jumping on mobiles
if ('ontouchstart' in window || navigator.maxTouchPoints > 0) {
    document.querySelectorAll('.tilt-card').forEach(card => {
        const content = card.querySelector('.tilt-content');
        if(content) content.style.transform = 'translateZ(0px)';
        const clone = card.cloneNode(true);
        card.parentNode.replaceChild(clone, card); 
    });
}
