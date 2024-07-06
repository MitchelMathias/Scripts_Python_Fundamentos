n = 0
soma = 0
print('Enter a qualquer momento pra encerrar.')
while True:
    numero = input('Digite um numero:')
    if numero == '':
        break
    numero = float(numero)
    soma = soma + numero
    n = n + 1
if n > 0:
    media = soma / n
    print('Sua média é:{}'.format(media))
    print('Fim')
else:
    print('Não foi inserido dados suficientes para calcular a média.')
