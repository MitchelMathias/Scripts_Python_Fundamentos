import random
c = [
    '\033[m',   # 0 sem cor
    '\033[1m',  # 1 negrito
    '\033[4m',  # 2 sublinhado
    '\033[7m',  # 3 reverso
    '\033[30m', # 4 preto
    '\033[31m', # 5 vermelho
    '\033[32m', # 6 verde
    '\033[33m', # 7 amarelo
    '\033[34m', # 8 azul
    '\033[35m', # 9 magenta
    '\033[36m', # 10 ciano
    '\033[37m', # 11 branco
    '\033[40m', # 12 sem cor de fundo
    '\033[41m', # 13 vermelho de fundo
    '\033[42m', # 14 verde de fundo
    '\033[43m', # 15 amarelo de fundo
    '\033[44m', # 16 azul de fundo
    '\033[45m', # 17 magenta de fundo
    '\033[46m', # 18 ciano de fundo
    '\033[47m'  # 19 branco de fundo
]


def ajuda(com):
    print(c[19], c[4], end='')
    help(com)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')
    return


comando = ''
while True:
    titulo('Esclarecendo Função ou Biblioteca', 14)
    comando = input('Digite aqui:')
    print(titulo(comando, random.randint(13, 19)))
    if comando.upper().strip() == 'FIM':
        print(titulo('fim', 13))
        break
    else:
        ajuda(comando)

