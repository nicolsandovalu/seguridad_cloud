import sys
import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace style block
content = re.sub(r'<style>.*?</style>', '<link rel="stylesheet" href="css/styles.css">', content, flags=re.DOTALL)

# Replace script block
content = re.sub(r'<script(?! src).*?</script>', '<script src="js/main.js"></script>', content, flags=re.DOTALL)

# Add Meta tags and Favicon before closing </head>
seo_tags = """
    <!-- SEO & Social Meta Tags -->
    <meta name="description" content="Simulador Interactivo de Hardening y Prevención de Brechas en la Nube.">
    <meta property="og:title" content="Cloud SecOps - Hardening y Prevención de Brechas">
    <meta property="og:description" content="Aprende y experimenta el proceso de Hardening a través de un panel interactivo.">
    <meta property="og:type" content="website">
    <link rel="icon" type="image/svg+xml" href="favicon.svg\">
"""
content = content.replace('</head>', seo_tags + '</head>')

# Fix Navbar responsive
content = content.replace('<nav class="flex gap-6 font-display text-sm">', '<nav class="flex flex-wrap justify-center gap-4 md:gap-6 font-display text-sm mt-4 md:mt-0">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Index optimized and split.')
