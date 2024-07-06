num = [[], []]
temp = 0
print('Pressione enter para deixar de adicionar valores.')
while True:
    temp = input('Digite um numero:')
    if temp == '':
        break
    if temp.isdigit():
        if int(temp) % 2 == 0:
            num[0].append(temp)
        else:
            num[1].append(temp)
print(f'Os números pares são {sorted(num[0])}')
print(f'Os números ímpares são {sorted(num[1])}')
