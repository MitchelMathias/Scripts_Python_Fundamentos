import random

while True:
    pa = input('pronto [S/N]:').strip().upper()[0]
    if pa == 'S':
        x = []
        for c in range(5):
            y = random.randint(0, 10)
            x.append(y)
        maior = max(x)
        menor = min(x)
        print(f'os valores sorteados são: {x}')
        print(f'o maior numero digitado foi {maior}')
        print(f'o menor numero digitado foi {menor}')
    if pa == 'N':
        print('Volte Sempre!!!')
        break
