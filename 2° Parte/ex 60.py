"""import math

numero = int(input('Digite um numero que deseja saber seu fatorial?'))
fatorial = math.factorial(numero)
print('fatorial de {} é igual a :{}'.format(numero,fatorial))"""

'''numero = int(input('Digite um numero que deseja saber seu fatorial?'))
print(f'Calculando o fatorial {numero} = !',end='')
c = numero
fatorial = 1
while c > 0:
    print(f'{c}', end='')
    fatorial = fatorial * c
    c = c - 1
    print(' x ' if c > 0 else ' = ', end='')
print(f'{fatorial}')'''

numero = int(input('Digite um numero que deseja saber seu fatorial?'))
print(f'Calculando fatorial {numero}! = ', end='')
c = 1
for f in range(numero, 0, -1):
    c = c * f
    if f > 1:
        print(f'{f} x ', end='')
    else:
        print(f'{f} = ', end='')
print(f'{c}')
