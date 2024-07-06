completa = []
temp = []
cadastrados = maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso:')))
    resp = str(input('Quer Cadastrar outra pessoa: [S/N]'))
    print('=-=' * 35)
    if len(completa) == 0:
        maior = menor = temp[1]
    elif temp[1] > maior:
        maior = temp[1]
    elif temp[1] < menor:
        menor = temp[1]
    completa.append(temp[:])
    temp.clear()
    cadastrados += 1
    if resp in 'Nn':
        break
print(f'Ao todo foram cadastradas {len(completa)} pessoas.')
print(f'O maior peso é de {maior}Kg do ', end='')
for p in completa:
    if p[1] == maior:
        print(f'[{p[0]}]', end=', ')
print(f'\nO menor peso é de {menor}Kg do ', end='')
for p in completa:
    if p[1] == menor:
        print(f'[{p[0]}]', end=', ')
