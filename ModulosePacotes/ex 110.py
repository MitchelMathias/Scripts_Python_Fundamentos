from Pacot import numeros

print('=' * 45)

while True:
    p = input('Digite um preço: ').replace(',', '.')
    try:
        conversao = float(p)
        p = float(p)
        break
    except ValueError:
        print('Digite novamente!!')

numeros.resumo(p, 50, 50)

