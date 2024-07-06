import random

print('Eai pequeno gafanhoto')
pergunta = str('bora pro play')
numero = random.randint(0, 10)
print('ja pensei em um n° de 0 a 10.')
print('vai tentar advinhar?')
adi = int(input('Qual é ?'))
acertou = False
palpite = 0
while not acertou:
    palpite = palpite + 1
    if adi == numero:
        acertou = True
    else:
        if adi < numero:
            adi = int(input('Mais... Tente dnv:'))
        elif adi > numero:
            adi = int(input('menos... Tente dnv:'))
print('Agora foi depois de {} tentativas'.format(palpite - 1))
