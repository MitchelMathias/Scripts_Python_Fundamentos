import random


def maior(num):
    ini = 0
    numeros = []
    while ini < num:
        temp = random.randint(0, 60)
        ini = ini + 1
        numeros.append(temp)
    if num == 0:
        print('=' * 35)
        print('Analisando os valores ...')
        print('0 Foi gerado zero valores.')
        print('=' * 35)
    else:
        print('=' * ((len(numeros) * 3) + 35))
        print('Analisando os valores ...')
        print(numeros, end=' ')
        print(f'Foi gerado {len(numeros)} valores.')
        print(f'O maior valor gerado foi {max(numeros)}.')
        print('=' * ((len(numeros) * 3) + 35))


while True:
    maior(random.randint(0, 10))
    per = input('Quer gerar novamente? [S/N]').lower()[0]
    while per not in 'sn':
        per = input('Tente novamente...').lower()[0]
    if per == 'n':
        break
