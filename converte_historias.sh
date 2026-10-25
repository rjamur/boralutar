#!/bin/bash
# O trator do XP: varrendo o Bosque e convertendo HTML em Markdown puro.

# Entra na pasta das histórias
cd historias || exit

# Encontra todos os .html (inclusive em subpastas)
find . -type f -name "*.html" | while read -r arquivo; do
    # Tira a extensão .html para criar o nome do .md
    novo_arquivo="${arquivo%.html}.md"
    
    echo "Lâmina descendo em: $arquivo -> $novo_arquivo"
    
    # O comando pro Gemini CLI (ajuste se o seu alias for diferente, ex: gemini-cli)
    cat "$arquivo" | gemini --model gemini-1.5-flash "Atue como um compilador Jekyll de Extreme Programming. Converta o seguinte HTML para Markdown puro. Arranque o lixo estrutural (html, head, body, links de css). Adicione EXATAMENTE este frontmatter no topo:
---
layout: dossie
title: \"[Extraia o título principal do HTML aqui]\"
---
Retorne APENAS o código final em Markdown, sem explicações, sem introduções e sem formatação de bloco de código (crases)." > "$novo_arquivo"
    
    # sleep 5
    # Se quiser que a máquina já queime as pontes (apague o HTML original):
    # rm "$arquivo"
done

echo "O Bosque foi convertido em Markdown. O asfalto está limpo."
