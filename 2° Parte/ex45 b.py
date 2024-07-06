import random
import time

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = random.randint(0, 2)
print('         {{{JOKEMPO}}}')
print('''suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual a sua Jogada:'))
print('              jo')
time.sleep(0.5)
print('             kenn')
time.sleep(0.5)
print('             po!!!')
print('-=-' * 10)
print('O computador jogou {}\n'
      'E você jogou {}.'.format(itens[computador], itens[jogador]))
print('-=-' * 10)
if computador == 0:  # computador jogou pedra
    if jogador == 0:
        print('Deu empate, foi um bom jogo.')
    elif jogador == 1:
        print('Você ganhou!!')
    elif jogador == 2:
        print('Você perdeu!!')
    else:
        print('Você digitou outro item?')
elif computador == 1:  # computador jogou Papel
    if jogador == 0:
        print('Você perdeu!!')
    elif jogador == 1:
        print('Deu empate, foi um bom jogo.')
    elif jogador == 2:
        print('Você ganhou!!')
    else:
        print('Você digitou outro item?')
elif computador == 2:  # Computador jogou tesoura
    if jogador == 0:
        print('Você ganhou!!')
    elif jogador == 1:
        print('Você perdeu!!')
    elif jogador == 2:
        print('Deu empate, foi um bom jogo.')
    else:
        print('Você digitou outro item?')
