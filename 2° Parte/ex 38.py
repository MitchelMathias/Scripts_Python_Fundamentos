n1 = float(input('Qual o 1° Numero?'))
n2 = float(input('Qual o 2° numero?'))
lista = [n1, n2]
if n1 > n2:
    print('O primeiro valor digitado é maior que o segundo.')
elif n2 > n1:
    print('O segundo valor digitado é maior que o primeiro.')
else:
    print('Ambos os numeros são iguais.')
