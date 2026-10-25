import os
import re
from datetime import datetime

# Caminhos base (ajuste os caminhos relativos de acordo com onde você vai rodar o script)
PASTA_ORIGEM = "../criptoca/historias" # Caminho para as pastas originais
PASTA_DESTINO = "_historias"           # Caminho da coleção do Jekyll

def recuperar_datas():
    for filename in os.listdir(PASTA_DESTINO):
        if not (filename.endswith(".html") or filename.endswith(".md")):
            continue
            
        slug = os.path.splitext(filename)[0]
        pasta_antiga = os.path.join(PASTA_ORIGEM, slug)
        
        # Verifica se a pasta antiga com o mesmo nome (slug) existe
        if os.path.isdir(pasta_antiga):
            # Prioriza pegar a data do index.html original. Se não achar, pega da pasta.
            index_antigo = os.path.join(pasta_antiga, "index.html")
            path_para_data = index_antigo if os.path.exists(index_antigo) else pasta_antiga
            
            # Pega o timestamp de modificação
            timestamp = os.path.getmtime(path_para_data)
            # Formata no padrão aceito pelo Jekyll (com timezone de Brasília)
            data_formatada = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S -0300')
            
            caminho_novo = os.path.join(PASTA_DESTINO, filename)
            
            # Lê o arquivo do Jekyll
            with open(caminho_novo, 'r', encoding='utf-8') as f:
                conteudo = f.read()
                
            # Verifica se já tem uma tag 'date:' para não duplicar
            if "\ndate:" not in conteudo:
                # Separa o conteúdo pelos delimitadores do Frontmatter '---'
                partes = conteudo.split('---', 2)
                
                if len(partes) >= 3:
                    # Injeta a data formatada no final do Frontmatter
                    novo_frontmatter = partes[1].rstrip() + f"\ndate: {data_formatada}\n"
                    novo_conteudo = f"---{novo_frontmatter}---{partes[2]}"
                    
                    with open(caminho_novo, 'w', encoding='utf-8') as f:
                        f.write(novo_conteudo)
                    print(f"[SUCESSO] Data {data_formatada} injetada em {filename}")
                else:
                    print(f"[ERRO] Frontmatter não encontrado em {filename}")
            else:
                print(f"[PULO] Arquivo {filename} já possui data configurada.")
        else:
            print(f"[AVISO] Pasta correspondente não encontrada para: {slug}")

if __name__ == "__main__":
    recuperar_datas()