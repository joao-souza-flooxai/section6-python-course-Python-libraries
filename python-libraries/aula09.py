import os

caminho = os.path.join('Desktop','curso', 'arquivo.txt' )
print(caminho)
diretorio, arquivo = os.path.split(caminho)
print(diretorio, arquivo)
caminho_arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(caminho_arquivo, extensao_arquivo)
print(os.path.basename(caminho))
print(os.path.basename(diretorio))
print(os.path.dirname(caminho))
