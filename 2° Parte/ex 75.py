nun = (int(input('Digite um numero:')), int(input('Digite mais um numero:')), int(input('Digite outro numero:'))
       , int(input('Digite ultimo numero:')))
print(f'Você escolheu esses números:{nun}')
print(f'o valor nove apareceu {nun.count(9)} vezes')
if 3 in nun:
    print(f'O valor de 3 apareceu na {nun.index(3) + 1}° posição')
else:
    print('O 3 não foi digitado')

pares = False

for n in nun:
    if n % 2 == 0:
        pares = True

if pares:
    print('Os numeros pares são:', end='')
    for n in nun:
        if n % 2 == 0:
            print(n, end=' , ')
if not pares:
    print('Não tem numeros pares')
