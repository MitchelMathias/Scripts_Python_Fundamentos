valores = []
print('Digite "Enter" parar de adicionar números')
while True:
    val = input('Digite um valor:')
    if val == '':
        break
    if val.isdigit():
        valores.append(int(val))
valores.sort()
print(f'A lista tem {len(valores)} elementos.')
print(f'Os valores digitados em ordem decrescente são:{valores}')
qual_num = int(input('Digite o numero que deseja encontrar:'))
posições = []
for i, v in enumerate(valores):
    if v == qual_num:
        posições.append(i+1)
if posições:
    if len(posições) > 1:
        print(f'O numero {qual_num} esta nas posições {posições}')
    else:
        print(f'O numero {qual_num} esta na posição: {posições[0]}')
else:
    print(f'O numero {qual_num} não esta na lista.')
