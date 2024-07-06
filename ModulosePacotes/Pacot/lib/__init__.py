import ModulosePacotes.Pacot.cores
from time import sleep


def linha(tam=45, cor=0):
    c = [
        '\033[m',  # 0 sem cor
        '\033[1m',  # 1 negrito
        '\033[4m',  # 2 sublinhado
        '\033[7m',  # 3 reverso
        '\033[30m',  # 4 preto
        '\033[31m',  # 5 vermelho
        '\033[32m',  # 6 verde
        '\033[33m',  # 7 amarelo
        '\033[34m',  # 8 azul
        '\033[35m',  # 9 magenta
        '\033[36m',  # 10 ciano
        '\033[37m',  # 11 branco
        '\033[40m',  # 12 sem cor de fundo
        '\033[41m',  # 13 vermelho de fundo
        '\033[42m',  # 14 verde de fundo
        '\033[43m',  # 15 amarelo de fundo
        '\033[44m',  # 16 azul de fundo
        '\033[45m',  # 17 magenta de fundo
        '\033[46m',  # 18 ciano de fundo
        '\033[47m'  # 19 branco de fundo
    ]
    x = f'{c[cor]}{"~" * tam}\033[m'
    return x


def menu(lista, msg1='MENU PRINCIPAL', msg2='Sua opção:', msg3='ERRO!: Digite um Número Válido.',
         msg4='Encerrando o Programa... Até Logo', cor1=0, cor2=7, cor3=8, cor4=6, cor5=5, cor6=0):

    """lista= A lista que deseja atribuir (apenas uma lista)
    msg1= A 1° Mensagem (cabeçalho)
    msg2= A Escrita após a escolha da opção
    msg3= A mensagem de Erro
    msg4= A Mensagem de finalização do programa
    cor1= A cor da msg1
    cor2= A cor dos números da lista
    cor3= A cor dos itens da lista
    cor4= A cor da msg2
    cor5= A cor do msg3
    cor6= A cor da msg4

    suas cores abaixo =
      0 sem cor
      1 negrito
      2 sublinhado
      3 reverso
      4 preto
      5 vermelho
      6 verde
      7 amarelo
      8 azul
      9 magenta
      10 ciano
      11 branco
      12 sem cor de fundo
      13 vermelho de fundo
      14 verde de fundo
      15 amarelo de fundo
      16 azul de fundo
      17 magenta de fundo
      18 ciano de fundo
      19 branco de fundo """
    while True:
        ModulosePacotes.Pacot.cores.titulo(msg1, cor1)
        sleep(0.5)
        c = 1
        for item in lista:
            print(f'{ModulosePacotes.Pacot.cores.letrasCustom(c, cor2)}° - '
                  f'{ModulosePacotes.Pacot.cores.letrasCustom(item, cor3)}')
            c += 1
            sleep(0.5)
        print(linha(45, cor1))

        resp = input(ModulosePacotes.Pacot.cores.letrasCustom(msg2, cor4))
        if resp.isdigit() and 1 <= int(resp) <= len(lista):
            resp = int(resp) - 1
            break
        else:
            sleep(0.5)
            print(ModulosePacotes.Pacot.cores.letrasCustom(msg3, cor5))
            sleep(0.5)

    if int(resp) + 1 == len(lista):
        ModulosePacotes.Pacot.cores.titulo(msg4, cor6)

    else:
        ModulosePacotes.Pacot.cores.titulo(lista[resp])
