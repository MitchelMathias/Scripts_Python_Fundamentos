import random
import time


def lin():
    atraso = 55
    for c in range(atraso):
        print('=', end='')
        time.sleep(0.05)
    print()


def valores(quant):
    sort = []
    for c in range(quant):
        sort.append(random.randint(0, 40))
    print(f'Os valores sorteados foram {sort}')
    time.sleep(0.2)
    return sort


def par(sort):
    par1 = cont = 0
    for n in sort:
        if n % 2 == 0:
            cont = cont + 1
            par1 = par1 + n
    print(f'Temos {cont} números pares e a soma é: {par1}')
    time.sleep(0.2)


while True:
    lin()
    print(f'{'Sorteando Valores...':^55}')
    time.sleep(0.3)
    lin()
    quant = int(random.randint(1, 10))
    print(f'Vamos sortear {quant} valores.')
    time.sleep(0.2)
    sort = valores(quant)
    par(sort)
    resp = input('Quer continuar? [S/N]').lower()[0]
    time.sleep(0.2)
    if resp in 'n':
        break
