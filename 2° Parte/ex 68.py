import random
import time

print('*' * 40)
print(f'{'PAR OU IMPAR':^40}')  # Centralizar uma frase muito bacana
print('*' * 40)
cont = 0
while True:
    cont = cont + 1
    print('-' * 40)
    PouI = ' '
    while PouI not in 'pi':
        PouI = str(input('Par ou impar: [P/I]')).strip()[0].lower()
    jogador = int(input('Digite um numero:'))
    print('-' * 40)
    maquina = random.randint(0, 10)
    soma = maquina + jogador
    print(f'Eu joguei {maquina}, vc jogou {jogador} o total é {soma}!!!')
    print(f'{'Deu par' if soma % 2 == 0 else 'Deu Impar':^40}')
    if soma % 2 == 0 and PouI == 'p':
        print(f'{'Voce ganhou!!!':^40}')
    if soma % 2 == 0 and PouI == 'i':
        print(f'{'voce perdeu!!!':^40}')
        break
    if soma % 2 != 0 and PouI == 'i':
        print(f'{'Voce Ganhou!!!':^40}')
    if soma % 2 != 0 and PouI == 'p':
        print(f'{'voce perdeu!!!':^40}')
        break
print(f'{'°_° pode chorar kskskks':^40}')
time.sleep(1)
print(f'  GAME OVER!!!! depois de {cont} tentativas')
time.sleep(1)
print(f'{'SEU FRACO SEM IDEAL':^40}')
