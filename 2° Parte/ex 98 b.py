import time


def contador(i, f, p):
    print('=' * 35)
    print(f'Contando de {i} até {f} de {p} em {p}.')
    cont = i
    if p == 0:
        p = 1
    if p < 0:
        p = p * -1
    if i < f:
        while cont <= f:
            print(cont, end=' ')
            cont = cont + p
            time.sleep(0.3)
        print(' Fim!!!')
    if i > f:
        while cont >= f:
            print(cont, end=' ')
            cont = cont - p
            time.sleep(0.3)
        print(' Fim!!!')
        print('=' * 35)


contador(1, 10, 1)
contador(10, 0, 2)
print('Sua Vez...')
while True:
    contador(int(input('Inicio:')), int(input('Fim:')), int(input('Passo:')))
    resp = str(input('Quer Continuar [S/N]:')).lower()[0]
    print('=' * 35)
    if resp == 'n':
        break
