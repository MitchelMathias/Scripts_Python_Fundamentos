import uex_115.cores
import uex_115.lib
import uex_115.numeros


def Arq(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError or FileExistsError:
        return False
    else:
        return True


def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        uex_115.cores.titulo(f'Houve um Erro na Criação do arquivo {nome}')
    else:
        uex_115.cores.titulo(f'O arquivo {nome}, Foi criado!!')


def ler(nome):
    try:
        a = open(nome, 'rt')
    except:
        uex_115.cores.letrasCustom('Erro!!', 5)
    else:
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<36}{dado[1]:>3} anos')


def cadastrar(nomearq, nome='Desconhecido', idade=0):
    try:
        a = open(nomearq, 'at')
        a.write(f'{nome};{idade}\n')
        a.close()
    except:
        uex_115.cores.letrasCustom('Erro ao abrir o arquivo!!!', 5)

