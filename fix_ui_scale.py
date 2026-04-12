import re

# 1. INYECTAR CSS (Escala Tipográfica Controlada)
css_payload = """
/* --- ESCALA TIPOGRÁFICA CONTROLADA (UI/UX Engineering) --- */
:root {
    --font-size-base: 16px; /* Base equilibrada */
}
html { font-size: var(--font-size-base) !important; }

/* Títulos con impacto pero sin desbordar */
h1 { font-size: 2rem !important; font-weight: 700; letter-spacing: 0.05em; } /* 32px */
h2 { font-size: 1.5rem !important; font-weight: 600; margin-bottom: 1rem; } /* 24px */
h3 { font-size: 1.15rem !important; font-weight: 600; } /* 18.4px */

/* Texto de cuerpo: Legible a distancia */
p, li, .text-sm { 
    font-size: 0.95rem !important; /* ~15.2px */
    line-height: 1.6 !important; 
    color: #cbd5e1; /* slate-300 para descanso visual */
}

/* Terminal y Código: Compacto pero claro */
.font-mono, pre, code { 
    font-size: 0.85rem !important; /* ~13.6px */
    line-height: 1.5 !important;
}

/* Etiquetas y estados */
.text-xs { font-size: 0.75rem !important; letter-spacing: 0.05em; } /* 12px */
"""

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Evitar duplicados
if "--font-size-base" not in css:
    with open('css/styles.css', 'w', encoding='utf-8') as f:
        f.write(css_payload + "\\n" + css)

# 2. SECCIÓN 5: Ajuste de Tabs
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Las alertas "[ ALERTA ]" deben usar font-size: 0.8rem
html = re.sub(
    r'<span>\\[ ALERTA \\](.*?)</span>',
    r'<span style="font-size: 0.8rem;">[ ALERTA ]\\1</span>',
    html
)

# #dynamic-lab-container padding
html = html.replace('id="dynamic-lab-container" class="md:col-span-7 relative', 'id="dynamic-lab-container" class="md:col-span-7 relative p-6')

# 3. SECCIÓN 6: Ajustar tarjetas
# Las descripciones de IaC, etc deben ir con text-[0.85rem]
cards_regex = r'<div\\s+class="p-5 border border-dynamic rounded-xl bg-black/10 hover:bg-black/20 transition-all hover:scale-\\[1.02\\]">(.*?)</div>'
def replace_card(match):
    content = match.group(0)
    # inyectar clase text-[0.85rem] sobre el contenedor de la tarjeta, así como una altura uniforme
    new_header = '<div class="p-5 border border-dynamic rounded-xl bg-black/10 hover:bg-black/20 transition-all hover:scale-[1.02] h-full flex flex-col text-[0.85rem]">'
    return new_header + match.group(1) + '</div>'

html = re.sub(cards_regex, replace_card, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Escala CSS Global + Ajustes UX en Sect 5 y 6 aplicados.")
