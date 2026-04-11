import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# MSFT New Content
msft_vuln = """<h4 class="text-red-500 font-bold mb-3 flex items-center gap-2">⚠️ Ataque Foco: Azure SAS Over-permissioned</h4>
                                <p class="text-xs mb-4 opacity-90 text-slate-300">
                                    <strong>Servicio:</strong> Azure Blob Storage.<br><br>
                                    <strong>¿Qué pasó?:</strong> Un equipo de investigación publicó modelos de IA en un repositorio de GitHub. Para facilitar el acceso, generaron un token SAS (Firma de Acceso Compartido). Sin embargo, por un error de configuración manual, el token no solo daba acceso a los modelos, sino a la cuenta de almacenamiento completa, permitiendo control total (lectura, escritura y borrado).<br><br>
                                    <strong>La Consecuencia:</strong> Se expusieron 38 TB de datos internos, incluyendo copias de seguridad de estaciones de trabajo, contraseñas y mensajes de Teams de empleados.
                                </p>
                                <div
                                    class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-red-300 border border-red-900/50 lab-code-glitch relative overflow-x-auto shadow-inner group/code">
                                    <span class="text-red-500/50"># Generando token de acceso total en lugar de un
                                        archivo</span><br>
                                    <span class="text-blue-400">az</span> storage container generate-sas \\<br>
                                    &nbsp;&nbsp;--account-name research_data --name models \\<br>
                                    &nbsp;&nbsp;<span
                                        class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded">
                                        --permissions rwl
                                        <span
                                            class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-56 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                            Da permiso de (R)ead, (W)rite y (L)ist a cualquier persona anónima con la
                                            URL.
                                        </span>
                                    </span>
                                    <span
                                        class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded ml-1 mt-2 lg:mt-0">
                                        --expiry 2033-01-01
                                        <span
                                            class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-56 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                            Token válido por 10 años. Muy difícil de auditar y revocar adecuadamente.
                                        </span>
                                    </span>
                                    <!-- Tooltip ISO 27017 general -->
                                    <div class="hidden group-hover/code:flex absolute top-2 right-2 bg-red-900 text-red-100 text-xs px-2 py-1 rounded border border-red-500 animate-pulse">
                                        ¡Peligro! Esta configuración ignora las mejores prácticas de la ISO 27017
                                    </div>
                                </div>"""

msft_sec = """<h4 class="text-emerald-500 font-bold mb-3 flex items-center gap-2">🛡️ Análisis Técnico: Falla del Mínimo Privilegio</h4>
                                <p class="text-xs mb-4 opacity-90 text-slate-300">
                                    <strong>Análisis Técnico:</strong> El error fue no aplicar el Mínimo Privilegio. Se usó un "pase maestro" en lugar de una "llave de una sola puerta".
                                </p>
                                <div
                                    class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-emerald-300 border border-emerald-900/50 overflow-x-auto shadow-inner">
                                    <span class="text-emerald-500/50"># IAM: El acceso se otorga por Identidad (RBAC)
                                        sin exponer links</span><br>
                                    <span class="text-blue-400">az</span> role assignment create --assignee
                                    &lt;app-id&gt; \\<br>
                                    &nbsp;&nbsp;<span
                                        class="bg-emerald-600/40 text-emerald-100 font-bold px-1 rounded">--role
                                        "Storage Blob Data Reader"</span> \\<br>
                                    &nbsp;&nbsp;--scope /subscriptions/&lt;sub-id&gt;/...
                                </div>"""

# ATT
att_vuln = """<h4 class="text-red-500 font-bold mb-3 flex items-center gap-2">⚠️ Ataque Foco: MFA
                                    Opcional y Red Abierta</h4>
                                <p class="text-xs mb-4 opacity-90 text-slate-300">
                                    <strong>Servicio:</strong> Snowflake Data Warehouse.<br><br>
                                    <strong>¿Qué pasó?:</strong> Entre abril y mayo de 2024, una campaña de ciberataques (UNC5537) afectó a clientes de Snowflake, incluyendo a AT&T. El ataque no explotó un fallo en el software, sino la higiene de identidad. Los atacantes usaron credenciales robadas para entrar a cuentas que no tenían activado el MFA (Autenticación Multifactor) y que permitían conexiones desde cualquier IP.<br><br>
                                    <strong>La Consecuencia:</strong> Exfiltración de registros de llamadas y mensajes de más de 100 millones de clientes.
                                </p>
                                <div
                                    class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-red-300 border border-red-900/50 lab-code-glitch relative overflow-x-auto shadow-inner group/code">
                                    <span class="text-blue-400">ALTER USER</span> "admin"
                                    <span
                                        class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded ml-1">
                                        SET MIN_MFA_DAYS = 0
                                        <span
                                            class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-56 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                            Omitió el uso de MFA. Atacantes con contraseña robada entraron al data
                                            warehouse libremente.
                                        </span>
                                    </span>
                                    <br><br>
                                    <span class="text-blue-400">CREATE NETWORK POLICY</span> "open" <br>
                                    &nbsp;&nbsp;ALLOWED_IP_LIST =
                                    <span
                                        class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded">
                                        ('0.0.0.0/0')
                                        <span
                                            class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-56 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                            Mala configuración del Firewall: Abre la interfaz de base de datos a TODO el
                                            internet.
                                        </span>
                                    </span>
                                    <div class="hidden group-hover/code:flex absolute top-2 right-2 bg-red-900 text-red-100 text-xs px-2 py-1 rounded border border-red-500 animate-pulse">
                                        ¡Peligro! Esta configuración ignora las mejores prácticas de la ISO 27017
                                    </div>
                                </div>"""

att_sec = """<h4 class="text-emerald-500 font-bold mb-3 flex items-center gap-2">🛡️ Análisis Técnico: Acceso Condicionado</h4>
                                <p class="text-xs mb-4 opacity-90 text-slate-300">
                                    <strong>Análisis Técnico:</strong> La falta de una política de "Acceso Condicionado" convirtió las credenciales robadas en llaves funcionales para los atacantes.
                                </p>
                                <div
                                    class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-emerald-300 border border-emerald-900/50 overflow-x-auto shadow-inner">
                                    <span class="text-emerald-500/50">-- Zero trust enforcing</span><br>
                                    <span class="text-blue-400">ALTER USER</span> "admin" <span
                                        class="bg-emerald-600/40 text-emerald-100 font-bold px-1 rounded">SET
                                        MIN_MFA_DAYS = 1</span>;<br><br>
                                    <span class="text-blue-400">CREATE NETWORK POLICY</span> "att_only" <br>
                                    &nbsp;&nbsp;ALLOWED_IP_LIST = <span
                                        class="bg-emerald-600/40 text-emerald-100 font-bold px-1 rounded">('10.2.0.0/16')</span>;
                                </div>"""

# LAT
lat_vuln = """<h4 class="text-red-500 font-bold mb-3 flex items-center gap-2">⚠️ Ataque Foco: AWS S3 y
                                    ACL Global</h4>
                                <p class="text-xs mb-4 opacity-90 text-slate-300">
                                    <strong>Servicio:</strong> Amazon S3.<br><br>
                                    <strong>¿Qué pasó?:</strong> Un bucket de S3 que servía archivos estáticos para el sitio web del periódico fue configurado con una ACL (Lista de Control de Acceso) que permitía escritura pública. Atacantes detectaron esta apertura y reemplazaron un archivo JavaScript legítimo por uno malicioso que minaba criptomonedas (Coinhive) usando el procesador de los visitantes.<br><br>
                                    <strong>La Consecuencia:</strong> Miles de lectores fueron víctimas de Cryptojacking, degradando el rendimiento de sus equipos y dañando la reputación del medio.
                                </p>
                                <div
                                    class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-red-300 border border-red-900/50 lab-code-glitch relative overflow-x-auto shadow-inner group/code">
                                    <span class="text-blue-400">aws</span> s3api put-bucket-acl --bucket
                                    web-assets \\<br>
                                    &nbsp;&nbsp;
                                    <span
                                        class="group relative inline-block cursor-help bg-red-600/40 text-white font-bold px-1 rounded mt-2">
                                        --grant-write uri=http://acs.amazonaws.com/groups/global/AllUsers
                                        <span
                                            class="hidden group-hover:block absolute bottom-full left-0 mb-2 w-64 p-3 bg-red-950/95 text-red-100 text-[11px] rounded shadow-2xl border border-red-500 z-50">
                                            Permite a todos (AllUsers) subir y editar los archivos HTML/JS del balde.
                                            Los atacantes inyectaron mineros web.
                                        </span>
                                    </span>
                                    <div class="hidden group-hover/code:flex absolute top-2 right-2 bg-red-900 text-red-100 text-xs px-2 py-1 rounded border border-red-500 animate-pulse">
                                        ¡Peligro! Esta configuración ignora las mejores prácticas de la ISO 27017
                                    </div>
                                </div>"""

lat_sec = """<h4 class="text-emerald-500 font-bold mb-3 flex items-center gap-2">🛡️ Análisis Técnico: Legado Peligroso</h4>
                                <p class="text-xs mb-4 opacity-90 text-slate-300">
                                    <strong>Análisis Técnico:</strong> El hardening falló al permitir permisos de escritura a nivel de "AllUsers", una configuración "heredada" que hoy es bloqueada por defecto en AWS.
                                </p>
                                <div
                                    class="bg-black/90 flex-1 p-4 rounded-xl font-mono text-xs text-emerald-300 border border-emerald-900/50 overflow-x-auto shadow-inner">
                                    <span class="text-emerald-500/50"># Invalidando las ACLs en favor del control
                                        IAM</span><br>
                                    <span class="text-blue-400">aws</span> s3control put-public-access-block
                                    --public-access-block-configuration "BlockPublicAcls=true,BlockPublicPolicy=true"
                                </div>"""

# Reemplazos via regex muy generales basados en id="lab-content-..."
html = re.sub(r'(<div id="lab-content-msft".*?<div[^>]*lab-view-vuln[^>]*>).*?(</div>\s*<!-- Vista Hardened -->\s*<div[^>]*lab-view-sec[^>]*>)', r'\g<1>' + msft_vuln + r'\g<2>', html, flags=re.DOTALL)
html = re.sub(r'(<!-- Vista Hardened -->\s*<div[^>]*lab-view-sec[^>]*>).*?(</div>\s*</div>)', r'\g<1>' + msft_sec + r'\g<2>', html, count=1, flags=re.DOTALL)

# Reemplazos manuales mas directos son dificiles si repite div, asi que usamos split y join o patrones especificos:
html_parts = html.split('id="lab-content-att"')
att_part = html_parts[1].split('id="lab-content-lat"')
html_att = att_part[0]
html_att = re.sub(r'(<div[^>]*lab-view-vuln[^>]*>).*?(</div>\s*<div[^>]*lab-view-sec[^>]*>)', r'\g<1>' + att_vuln + r'\g<2>', html_att, flags=re.DOTALL)
html_att = re.sub(r'(<div[^>]*lab-view-sec[^>]*>).*?(</div>\s*</div>)', r'\g<1>' + att_sec + r'\g<2>', html_att, flags=re.DOTALL)

html_lat = html_parts[1].split('id="lab-content-lat"')[1]
html_lat = re.sub(r'(<div[^>]*lab-view-vuln[^>]*>).*?(</div>\s*<div[^>]*lab-view-sec[^>]*>)', r'\g<1>' + lat_vuln + r'\g<2>', html_lat, flags=re.DOTALL)
html_lat = re.sub(r'(<div[^>]*lab-view-sec[^>]*>).*?(</div>\s*</div>)', r'\g<1>' + lat_sec + r'\g<2>', html_lat, flags=re.DOTALL)

html = html_parts[0] + 'id="lab-content-att"' + html_att + 'id="lab-content-lat"' + html_lat

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("HTML actualizado")
