import random
import time

print('-=-' * 10)
print('-=-' * 10)
print('         {{{JOKEMPO}}}')
print('-=-' * 10)
print('-=-' * 10)
jogador = str(input('      Digite sua escolha.\n'
                    '      eu não  vou  olhar:')).lower().strip()
print('           jokempooo...')
time.sleep(1)
opções = ('pedra', 'papel', 'tesoura')
maquina = random.choice(opções)
resultados = {
    ('pedra', 'pedra'): 'Empate!',
    ('pedra', 'papel'): 'Você perdeu! Papel cobre pedra.',
    ('pedra', 'tesoura'): 'Você ganhou! Pedra quebra tesoura.',
    ('papel', 'pedra'): 'Você ganhou! Papel cobre pedra.',
    ('papel', 'tesoura'): 'Você perdeu! Tesoura corta papel.',
    ('tesoura', 'pedra'): 'Você perdeu! Pedra quebra tesoura.',
    ('tesoura', 'papel'): 'Você ganhou! Tesoura corta papel.', }
resultado = resultados.get((jogador, maquina), 'Escolha inválida. Tente novamente.')
print(resultado)
