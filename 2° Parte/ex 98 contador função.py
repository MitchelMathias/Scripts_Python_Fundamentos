import time


def contagem():
    print('=' * 40)
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1, 11):
        time.sleep(0.3)
        print(c, end=' ')
    print('Fim!!!')
    print('=' * 40)
    print('Contagem de 10 até 0 de 2 em 2')
    for a in range(10, -1, -2):
        time.sleep(0.3)
        print(a, end=' ')
    print()
    while True:
        print('=' * 40)
        print('Agora é a sua vez!')
        i = int(input('Inicio: '))
        f1 = int(input('Fim: '))
        if f1 < i:
            f = f1 - 1
        elif f1 > i:
            f = f1 + 1
        p = int(input('Passo: '))
        print('=' * 40)
        print(f'Contagem de {i} até {f1} de {p} em {p}')
        if p == 0:
            p = 1
        for u in range(i, f, p):
            time.sleep(0.3)
            print(u, end=' ')
        if i > f:
            for d in range(i, f, -p):
                time.sleep(0.3)
                print(d, end=' ')
            print()
            print('=' * 40)

        print()
        respp = str(input('Quer Continuar [S/N]:'))
        if respp.lower()[0] in 'n':
            break


contagem()
print('Fim!!!')
