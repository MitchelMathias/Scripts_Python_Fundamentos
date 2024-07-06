import os
import webbrowser
import unidecode


def remover(texto):
    return unidecode.unidecode(texto)


def reproduzir(nome_arquivo):
    try:
        webbrowser.open(os.path.abspath(nome_arquivo))
    except Exception as e:
        print(f'Ocorreu um erro ao reproduzir a musica: {e}')


pasta = r'C:\Users\Mathias\Desktop\Musica'
nome = str(input('Qual o nome do arquivo?'))
arquivos = os.listdir(pasta)
for arquivo in arquivos:
    if remover(nome.lower()) in remover(arquivo.lower()):
        caminho = os.path.join(pasta, arquivo)
        reproduzir(caminho)
        break
else:
    print(f'A musica {nome} não foi encontrada na {pasta}')
