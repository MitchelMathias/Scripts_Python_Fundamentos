

def fatorial(n, formato=False):
    nu = 1
    for c in range(1, n + 1):
        nu = nu * c
    return nu if formato is False else moeda(nu)


def dobro(n, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def triplo(n, formato=False):
    res = n * 3
    return res if formato is False else moeda(res)


def metade(n, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def aumenta(n, por, formato=False):
    res = n + (n * por / 100)
    return res if formato is False else moeda(res)


def diminui(n, por, formato=False):
    res = n - (n * por / 100)
    return res if not formato else moeda(res)


def moeda(preco=0, tipo='R$'):
    return f'{tipo}{preco:.2f}'.replace('.', ',')


def resumo(preço, aumento=0, redução=0):
    print('=' * 45)
    print(f'{"Resumo":^45}')
    print('=' * 45)
    print(f'Preço analisado:\t\t\t\t{moeda(preço,)}')
    print(f'Dobro do Preço:\t\t\t\t\t{dobro(preço, True)}')
    print(f'Dobro do Preço:\t\t\t\t\t{metade(preço, True)}')
    print(f'Aumentado em {aumento}%:\t\t\t\t{aumenta(preço, aumento, True)}')
    print(f'Reduzido em {redução}%:\t\t\t\t{diminui(preço, redução, True)}')
    print('=' * 45)
