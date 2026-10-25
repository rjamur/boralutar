---
layout: historias
title: "Arquivo de Histórias | Boralutar"
permalink: /historias/
---

<div class="max-w-4xl mx-auto py-12 md:py-20 px-4 md:px-0">
    
    <!-- CABEÇALHO -->
    <header class="mb-16 border-b border-zinc-800 pb-10">
        <h1 class="text-4xl md:text-6xl font-black uppercase tracking-tighter text-white mb-4">
            Arquivo Geral
        </h1>
        <p class="font-mono text-zinc-400 text-sm md:text-base max-w-2xl leading-relaxed">
            Diretório indexado de relatos, manifestos, tecnologia social com IA e táticas de defesa do sistema.
        </p>
    </header>

    <!-- LISTA DE ARQUIVOS (LOOP DO JEKYLL) -->
    <section>
        <div class="flex items-center gap-4 mb-8">
            <h2 class="font-mono text-sm text-zinc-500 uppercase tracking-widest">
                // 01. A Trilha Principal
            </h2>
            <div class="h-px bg-zinc-800 flex-grow"></div>
        </div>

        <!-- Container da Lista -->
        <div class="flex flex-col border-t border-zinc-800">
            
            {% assign historias_ordenadas = site.historias | sort: 'date' | reverse %}
            {% for post in historias_ordenadas %}
            
            <!-- LINK GERAL COM CLASSE 'group' PARA CONTROLAR O HOVER -->
            <a href="{{ post.url | relative_url }}" class="group relative block py-8 px-4 md:px-8 border-b border-zinc-800/50 hover:bg-zinc-900/40 transition-colors overflow-hidden">
                
                <!-- A LINHA VERMELHA MÁGICA: Fixa na esquerda, opacidade 0 por padrão, opacidade 100 no hover -->
                <div class="absolute inset-y-0 left-0 w-1 bg-red-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                
                <!-- CONTEÚDO DO ITEM -->
                <div class="flex flex-col md:flex-row md:items-center justify-between gap-6">
                    
                    <div class="flex flex-col">
                        <!-- Etiquetas / Tags -->
                        <div class="flex items-center gap-3 mb-3">
                            <span class="px-2 py-0.5 bg-zinc-950 border border-zinc-800 text-[10px] text-zinc-500 font-mono uppercase tracking-widest rounded-sm group-hover:border-zinc-700 transition-colors">
                                [ ARQUIVO_Nº: {{ post.ordem | default: forloop.index | prepend: '00' | slice: -2, 2 }} ]
                            </span>
                            
                            {% if post.tag %}
                            <span class="text-red-500 font-mono text-[10px] uppercase font-bold tracking-widest flex items-center gap-1">
                                {{ post.tag }}
                            </span>
                            {% endif %}
                        </div>
                        
                        <!-- Título e Subtítulo -->
                        <h3 class="text-2xl md:text-3xl font-bold text-zinc-300 group-hover:text-white transition-colors tracking-tight">
                            {{ post.title }}
                        </h3>
                        <p class="text-zinc-500 mt-2 max-w-2xl text-sm md:text-base group-hover:text-zinc-400 transition-colors">
                            {{ post.subtitle | default: "Registro extraído do asfalto e da memória." }}
                        </p>
                    </div>
                    
                    <!-- Seta da direita com animação -->
                    <div class="hidden md:flex font-mono text-xs text-zinc-600 uppercase text-right group-hover:text-red-500 transition-colors flex-col items-end">
                        <span>Abrir_Arquivo</span>
                        <span class="group-hover:translate-x-2 transition-transform duration-300 ease-out inline-block mt-1">
                            ->
                        </span>
                    </div>
                    
                </div>
            </a>
            
            {% endfor %}
            
        </div>
    </section>
</div>
