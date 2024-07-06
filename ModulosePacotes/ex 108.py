from Pacot import numeros, cores

cores.titulo('Modularização', 16)
resp = 0
n = float(input('Digite um preço: R$ ').replace(',', '.'))
print('Escolha uma opção: ')
while True:
    while True:
        resp = int(input('   [1] Dobro'
                         '\n   [2] Metade'
                         '\n   [3] Aumentar'
                         '\n   [4] Diminuir'
                         '\nEscolha: '))
        if resp not in [1, 2, 3, 4]:
            print('Tente Novamente !!!')
        else:
            break

    if resp == 1:
        print(numeros.dobro(n, True))
    elif resp == 2:
        print(numeros.metade(n))
    elif resp == 3 or resp == 4:
        quanto = float(input('Quantos %: '))
        if resp == 3:
            print(numeros.aumenta(n, quanto))
        elif resp == 4:
            print(numeros.diminui(n, quanto))

    continua = input('Quer Continuar [S/N]').upper().strip()[0]
    if continua == 'N':
        break
