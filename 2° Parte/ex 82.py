valores = []
print('Click no Enter para encerrar os valores.')
while True:
    val = input('Digite um valor:')
    if val == '':
        break
    if val.isdigit():
        valores.append(int(val))
print(f'Os valores digitados foram {valores}')
pares = []
impares = []
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print(f'Os números pares são:{pares}')
print(f'Os números impares são:{impares}')
