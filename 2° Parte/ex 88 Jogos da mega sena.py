from random import randint
import time
print('-'*35)
print(f'{'JOGOS DA MEGA SENA':^35}')
print('-'*35)
jogos = []
num = 0
while True:
    quant = int(input('Quantos jogos deseja sorter:'))
    print(f'-=-=-=-= Sorteando {quant} Jogos -=-=-=-=')
    for c in range(0, quant):
        jogos = []
        while len(jogos) < 6:
            num = randint(1, 60)
            if num not in jogos:
                jogos.append(num)
        time.sleep(0.5)
        print(f'o {c+1}° jogo:{sorted(jogos)}')
    print()
    encerramento = input('Quer continuar?[S/N] ')
    if encerramento.lower() in 'n':
        break
