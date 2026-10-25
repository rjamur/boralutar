import os
import re
import shutil

# Configurações das trincheiras
DIR_HISTORIAS = '_historias'
DIR_LAYOUTS = '_layouts'
# O arquivo que tem a vitrine e a ordem exata (ajuste se o nome for diferente na raiz)
ARQUIVO_INDEX = 'index_2.md'

def forjar_o_asfalto():
    print("Iniciando o Trator XP. A lâmina está descendo...")
    
    # Garante que a pasta de layouts existe
    os.makedirs(DIR_LAYOUTS, exist_ok=True)
    
    # 1. Mapear a Ordem pelo índice
    ordem_map = {}
    if os.path.exists(ARQUIVO_INDEX):
        with open(ARQUIVO_INDEX, 'r', encoding='utf-8') as f:
            conteudo_index = f.read()
            
        # Puxa todos os links href="nome-da-pasta/"
        slugs = re.findall(r'href="([^/"]+)/?"', conteudo_index)
        for i, slug in enumerate(slugs):
            ordem_map[slug] = i + 1
        print(f"✔ Mapa do Bosque lido: {len(ordem_map)} histórias encontradas no índice.")
    else:
        print(f"⚠ Aviso: {ARQUIVO_INDEX} não encontrado na raiz. Ordem será 999.")

    # 2. Varrer as pastas dentro de _historias
    for nome_pasta in os.listdir(DIR_HISTORIAS):
        caminho_pasta = os.path.join(DIR_HISTORIAS, nome_pasta)
        
        # Só opera se for diretório (ignora arquivos soltos)
        if os.path.isdir(caminho_pasta):
            index_html_path = os.path.join(caminho_pasta, 'index.html')
            
            if os.path.exists(index_html_path):
                with open(index_html_path, 'r', encoding='utf-8') as f:
                    html_cru = f.read()

                # 3. Separar o Layout da Carne (Buscando a tag <body>)
                # O Regex tenta achar o corpo para isolar o texto.
                body_match = re.search(r'(<body[^>]*>)(.*?)(</body>)', html_cru, re.IGNORECASE | re.DOTALL)
                
                nome_layout = f"layout_{nome_pasta}"
                
                if body_match:
                    tag_abertura = body_match.group(1)
                    carne_texto = body_match.group(2).strip()
                    tag_fechamento = body_match.group(3)
                    
                    # Constrói o layout injetando o {{ content }} do Jekyll
                    layout_html = html_cru[:body_match.start(1)] + tag_abertura + "\n    {{ content }}\n    " + tag_fechamento + html_cru[body_match.end(3):]
                else:
                    # Se não achar body, assume que o arquivo todo é texto e não extrai layout
                    carne_texto = html_cru
                    layout_html = None

                # 4. Salvar o Layout
                if layout_html:
                    caminho_layout = os.path.join(DIR_LAYOUTS, f"{nome_layout}.html")
                    with open(caminho_layout, 'w', encoding='utf-8') as f:
                        f.write(layout_html)
                    layout_final = nome_layout
                else:
                    layout_final = "dossie" # Fallback para o layout padrão

                # 5. Forjar o arquivo .md com o Frontmatter
                ordem = ordem_map.get(nome_pasta, 999)
                titulo = nome_pasta.replace('-', ' ').title()
                
                frontmatter = f"""---
layout: {layout_final}
title: "{titulo}"
category: historia
ordem: {ordem}
---

{carne_texto}
"""
                caminho_md = os.path.join(DIR_HISTORIAS, f"{nome_pasta}.md")
                with open(caminho_md, 'w', encoding='utf-8') as f:
                    f.write(frontmatter)

                print(f"✔ Sangue extraído e ordenado [{ordem}]: {nome_pasta}.md")

                # 6. Incinerar a pasta inútil
                shutil.rmtree(caminho_pasta)

    print("\nO manicômio de pastas caiu. A coleção está plana. O asfalto está limpo.")

if __name__ == "__main__":
    forjar_o_asfalto()