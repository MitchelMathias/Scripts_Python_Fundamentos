print('*********** Bem vindo a tabuada ***********')
while True:
    print('->' * 10)
    n = input('De qual numero:')
    if not n:
        break
    if n.isdigit():
        n = int(n)
        for c in range(1, 11):
            multi = n * c
            print(f'{n} x {c} = {multi}')
    else:
        print('valor inválido')
        resp = str(input('Quer Cancelar? [S/N]')).strip()[0].upper()
        if resp == 'S':
            break
