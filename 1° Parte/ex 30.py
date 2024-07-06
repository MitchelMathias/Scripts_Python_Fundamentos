import random
from time import sleep

n = int(random.randint(0, 1))
print('-=-' * 13)
print('Vou pensar em um numero de 0 a 1')
print('          Pensando...')
sleep(1)
print('    ja sei, duvido acertar')
print('      tente adivinhar?')
print('-=-' * 13)
adv = int(input(':'))
if adv == n:
    print('Meu deus vc é bom nesse jogo!!!')
else:
    print('você errou, execute e tente dnv')
    print('Eu venci venceu')
print(f'O numero era {n} mesmo')
