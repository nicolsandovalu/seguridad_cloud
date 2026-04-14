import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_grid_pattern = r'(<div class="max-w-4xl mx-auto space-y-3">.*?</div>)(\s*</div>\s*<!-- ========================================= -->\s*<!-- VISTA 3: REFERENCIAS)'

new_html_block = r"""<div class="max-w-4xl mx-auto space-y-3">
                
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11V7.159c0-1.255-1.042-2.274-2.29-2.274H5c-1.105 0-2 .895-2 2v3.84m9 3.517c0 3.517 1.009 6.799 2.753 9.571m3.44-2.04l-.054-.09A13.916 13.916 0 0116 11V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84m-9 3.517V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84"></path></svg>
                            1. Hardening
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Proceso de reducir la superficie de   ataque de un sistema eliminando configuraciones innecesarias, aplicando restricciones y   siguiendo guías de mejores prácticas de seguridad.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M3 10V21M21 10V21M3 10L12 3L21 10M12 11V21M12 11H8M12 11H16"></path></svg>
                            2. Superficie de ataque
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Conjunto de todos los puntos de   entrada por los que un atacante podría intentar acceder a un sistema. Más configuraciones   abiertas = mayor superficie de ataque.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path></svg>
                            3. Principio de menor

                        privilegio
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Regla de seguridad que indica que   cada usuario, proceso o sistema debe tener solo los permisos mínimos necesarios para realizar su   tarea, y nada más.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
                            4. Buckets/Blobs
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Es el contenedor lógico básico de   almacenamiento en la nube (ej. AWS S3).   <span class="block mt-2"><strong class="text-red-400">Buckets Públicos / Brechas por buckets           expuestos:</strong> Riesgo muy       común de exponer datos sensibles por no cambiar la visibilidad a "privada". Ocurren por mala       configuración del contenedor, permitiendo a quien sea ver o descargar archivos sin       contraseñas</span>
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M3 10V21M21 10V21M3 10L12 3L21 10M12 11V21M12 11H8M12 11H16"></path></svg>
                            5. Shadow IT
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Servicios levantados por   desarrolladores sin pasar por el proceso de hardening (ej. bases de datos sin contraseña).
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M3 10V21M21 10V21M3 10L12 3L21 10M12 11V21M12 11H8M12 11H16"></path></svg>
                            6. Movimiento Lateral
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Si una instancia comprometida no   tiene hardening de red, el atacante puede saltar a otros servidores críticos.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M13.828 10.172a4 4 0 00-5.656 0l-4 4a4 4 0 105.656 5.656l1.102-1.101m-.758-4.899a4 4 0 005.656 0l4-4a4 4 0 00-5.656-5.656l-1.1 1.1"></path></svg>
                            7. Endpoints
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Cualquier dispositivo o punto de   conexión que se comunica con una red. En Cloud piensa en un endpoint como una "puerta de   entrada" a tus servicios. Si está "expuesto", cualquiera en Internet podría intentar "tocar la   puerta".
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
                            8. CSPM
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Cloud Security Posture Management   (Gestión de la Postura de Seguridad en la Nube):   Categoría de herramientas de seguridad que escanean continuamente tu infraestructura en la nube   para detectar malas configuraciones, riesgos de cumplimiento y vulnerabilidades.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
                            9. CNAPP
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Cloud-Native Application Protection   Platforms (Plataformas de Protección de Aplicaciones Nativas de la Nube):   Evolución del CSPM que unifica múltiples herramientas de seguridad para proteger todo   el ciclo de vida de una aplicación en la nube.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                            10. MFA
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Multi-Factor Authentication:   Método de seguridad que requiere que el usuario proporcione dos o más pruebas (factores)   diferentes para   verificar su identidad antes de acceder a una cuenta o sistema.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                            11. Modelo de responsabilidad

                        compartida
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Define quién es responsable de qué,   dividiendo el trabajo entre el proveedor de la nube y el cliente.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
                            12. Bucket Policies (AWS)
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Documentos JSON que se adjuntan a   un contenedor completo en AWS S3. En lugar de dar permisos archivo por archivo, definen reglas a   nivel general.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11V7.159c0-1.255-1.042-2.274-2.29-2.274H5c-1.105 0-2 .895-2 2v3.84m9 3.517c0 3.517 1.009 6.799 2.753 9.571m3.44-2.04l-.054-.09A13.916 13.916 0 0116 11V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84m-9 3.517V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84"></path></svg>
                            13. Block Public Access
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Interruptor de seguridad de máxima   prioridad en   AWS. Cuando se activa, bloquea instantáneamente cualquier acceso público, ignorando y anulando   cualquier política   o ACL previa.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
                            14. Blob Storage (Azure)
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Servicio de almacenamiento de   objetos de Azure. Diseñado para almacenar cantidades masivas de datos no estructurados, como   texto, imágenes o videos.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 01-.707.293h-3.172a1 1 0 01-.707-.293l-2.414-2.414A1 1 0 006.586 13H4"></path></svg>
                            15. allow-blob-public-access

                        false
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Configuración específica en Azure   que desactiva el acceso anónimo y público a todos los contenedores. Equivalente al Block Public   Access.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                            16. SAS (Azure)
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Shared Access Signatures: Token o   URL firmada criptográficamente para otorgar acceso temporal y limitado a un recurso específico   sin exponer la contraseña principal.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>
                            17. UBLA (GCP)
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Uniform Bucket-Level Access:   Unifica el control de acceso. Al activarla, deshabilita las antiguas ACLs y fuerza a que toda   seguridad se gestione mediante IAM.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                            18. (ACL) Access Control List
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Método de seguridad heredado. Lista   adjunta a un archivo que dice quién tiene permisos. Es propensa a errores humanos a escala   Cloud.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path></svg>
                            19. Managed Identities
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Identidades Administradas (Azure):   Da a una aplicación su propia identidad para conectarse a bases de datos sin guardar contraseñas   en el código.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11V7.159c0-1.255-1.042-2.274-2.29-2.274H5c-1.105 0-2 .895-2 2v3.84m9 3.517c0 3.517 1.009 6.799 2.753 9.571m3.44-2.04l-.054-.09A13.916 13.916 0 0116 11V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84m-9 3.517V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84"></path></svg>
                            20. Security Groups (AWS)
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Actúan como firewall virtual a   nivel de la instancia. Son stateful: si aprueban la entrada de un dato, aprueban su salida.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11V7.159c0-1.255-1.042-2.274-2.29-2.274H5c-1.105 0-2 .895-2 2v3.84m9 3.517c0 3.517 1.009 6.799 2.753 9.571m3.44-2.04l-.054-.09A13.916 13.916 0 0116 11V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84m-9 3.517V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84"></path></svg>
                            21. NSG (Azure)
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Network Security Groups: Asociables   a subredes completas o interfaces. Filtran el tráfico determinando qué IPs y puertos pueden   comunicarse con los recursos.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                            22. SSH (Puerto 22)
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Secure Shell. Es un protocolo de   red criptográfico   utilizado por los administradores de sistemas para conectarse de forma remota y segura a la   consola de comandos de un servidor Linux.   Si este protocolo para servidores Linux se deja abierto a todo Internet (0.0.0.0/0), atacantes   buscarán tomar   control por fuerza bruta.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                            23. RDP (Puerto 3389)
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Remote Desktop Protocol de Windows.   Es el equivalente de SSH pero para servidores Windows; proporciona una interfaz gráfica para   manejar el servidor con mouse y teclado a distancia.   Si está expuesto públicamente, es uno de los principales vectores de entrada para ataques de   Ransomware.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M3 10V21M21 10V21M3 10L12 3L21 10M12 11V21M12 11H8M12 11H16"></path></svg>
                            24. Exfiltración
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Transferencia o robo no autorizado   de datos desde un sistema hacia el exterior (robando información confidencial masivamente).
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M3 10V21M21 10V21M3 10L12 3L21 10M12 11V21M12 11H8M12 11H16"></path></svg>
                            25. Cryptojacking
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Ciberataque donde el intruso   logr acceder a los servirdores de la nube de una víctima y utiliza el poder de procesamiento   (CPU/GPU) de servidores Cloud para minar   criptomonedas a expensas de facturas astronómicas. Esto puede suceder, por ejemplo, si dejan el   puerto 22 abierto o   el permiso IAM es demasiado amplio
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #22d3ee; text-shadow: 0 0 5px rgba(34,211,238,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M15 7a2 2 0 012 2m4 0a6 6 0 01-7.743 5.743L11 17H9v2H7v2H4a1 1 0 01-1-1v-2.586a1 1 0 01.293-.707l5.964-5.964A6 6 0 1121 9z"></path></svg>
                            26. IAM
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Identity and Access Management:   Capa fundamental de seguridad en la nube que se encarga de gestionar quién puede acceder a qué   recursos y bajo qué condiciones. En lugar de ser un simple   sistema de "usuario y contraseña", es un marco robusto que define la identidad de personas y   servicios, y los permisos exactos que poseen.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
                            27. IaC
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Infraestructura como Código   (Terraform, AWS CloudFormation). Gestionar y aprovisionar toda la nube utilizando archivos de   código legibles, en lugar de configuraciones manuales.
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #10b981; text-shadow: 0 0 5px rgba(16,185,129,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>
                            28. Shift-Left
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Mover los controles de seguridad lo   más al inicio del desarrollo, integrándolos desde el momento en que se escribe el código   (Checkov, tfsec).
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                            29. Tokens SAS
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Tokens (Shared Access Signatures)   Es una URL firmada que otorga acceso limitado y delegado a los recursos de una cuenta de   almacenamiento   (Blobs, archivos, tablas) sin exponer las claves maestras de la cuenta..
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"></path></svg>
                            30. Shift-Left
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        En una línea de tiempo de   desarrollo de software (que se lee de izquierda a   derecha: Diseño ➡️ Código ➡️ Pruebas ➡️ Producción), "Shift-Left" significa mover los controles   de seguridad lo más a la izquierda posible,   integrándolos desde el momento en que el desarrollador está escribiendo el código. (Checkov,   Terrascan, tfsec)
                    </div>
                </details>
                <details class="group bg-black/40 border border-dynamic rounded-lg overflow-hidden transition-all duration-300 hover:border-cyan-500/50">
                    <summary class="flex justify-between items-center font-bold cursor-pointer list-none p-5 outline-none">
                        <span class="font-mono text-[1.05rem] flex items-center" style="color: #ef4444; text-shadow: 0 0 5px rgba(239,68,68,0.5);">
                            <svg fill="none" class="w-5 h-5 mr-3 inline-block" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24"><path d="M12 11c0 3.517-1.009 6.799-2.753 9.571m-3.44-2.04l.054-.09A13.916 13.916 0 008 11V7.159c0-1.255-1.042-2.274-2.29-2.274H5c-1.105 0-2 .895-2 2v3.84m9 3.517c0 3.517 1.009 6.799 2.753 9.571m3.44-2.04l-.054-.09A13.916 13.916 0 0116 11V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84m-9 3.517V7.159c0-1.255 1.042-2.274 2.29-2.274h.71c1.105 0 2 .895 2 2v3.84"></path></svg>
                            31. S3 Block Public Access
                        </span>
                        <span class="transition-transform duration-300 group-open:rotate-180 text-cyan-500">
                            <svg fill="none" height="24" stroke="currentColor" stroke-width="1.5" viewBox="0 0 24 24" width="24"><path d="M6 9l6 6 6-6"></path></svg>
                        </span>
                    </summary>
                    <div class="p-5 text-slate-300 text-[0.85rem] border-t border-dynamic leading-relaxed bg-[#050505]">
                        Configuración en AWS que bloquea   cualquier   intento de hacer público un bucket S3, ya sea por política o por ACL (lista de control de   acceso).
                    </div>
                </details>

            </div>\g<2>"""

html_nuevo = re.sub(old_grid_pattern, new_html_block, html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_nuevo)

print("¡index.html actualizado exitosamente con los 31 ítems interactivos y sus iconos correspondientes!")
