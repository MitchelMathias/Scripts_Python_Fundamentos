from random import randint
import time
from operator import itemgetter
print('=' * 35)
print(f'{"Gerador de Dados":^35}')
print('=' * 35)
gerados = {}
ordem = {}
cont = 0
print('Valores Sorteados:')
for c in range(0, 4):
    gerados[f'{c + 1}° Jogador'] = randint(1, 6)
for k, v in gerados.items():
    print(f'{k} sortou o numero {v}')
    time.sleep(0.5)
print('=' * 35)
print('Classificação:')
ordem = sorted(gerados.items(), key=itemgetter(1), reverse=True)
'''for cont, (jogador, numero) in enumerate(ordem):
    print(f'O {cont+1}° Colocado foi o {jogador} com {numero}')
    time.sleep(0.5)
print('=' * 35)'''
for key, chave in ordem:
    cont += 1
    print(f'o {cont}° Colocado foi o {key} com {chave}')
    time.sleep(0.5)
