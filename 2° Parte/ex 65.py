per = 'S'
n = 0
media = soma = quant = maior = menor = 0
while per in 'sS':
    n = int(input('Digite um numero:'))
    soma = soma + n
    quant = quant + 1
    media = soma / quant
    if quant == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    per = str(input('Quer continuar? [S/N]')).strip().lower()[0]
print('Voce Digitou: {}, a soma entre eles é: {} e a média é: {}.'.format(quant, soma, media))
print('O maior valor foi:{} e o menor: {}'.format(maior, menor))
