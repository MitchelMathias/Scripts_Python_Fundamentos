def fat(n, show=False):
    """- Calcula o fatorial de N
    show = True, Mostra o calculo
    Show = False, Mostra apenas o resultado
    return c = retorna o valor pra quando a função foi chamada.
    """
    c = 1
    f = 1
    mostra = input('Quer ver o calculo?')
    if mostra.lower()[0] in 's':
        show = True
    else:
        show = False
    while n >= f:
        c *= f
        if show:
            print(f, end='')
            if f == n:
                print('=', end='')
            else:
                print('x', end='')
        f += 1
    else:
        return c


print('='*35)
print(f'{'Calculando fatorial':^35}')
print('='*35)
while True:
    n = int(input('Qual numero deseja saber o fatorial? '))
    print(fat(n))
    print('=' * 35)
    resp = str(input('Quer saber de outro número [S/N] ')).lower().strip()[0]
    print('=' * 35)
    while resp not in 'sn':
        print('Tente novamente')
        resp = str(input('Quer saber de outro número [S/N] ')).lower().strip()[0]
    if resp in 'n':
        break
