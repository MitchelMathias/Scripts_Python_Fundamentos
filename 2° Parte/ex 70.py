print('-' * 45)
print(f'{'Loja Super Baratão':^45}')
print('-' * 45)
total = totmais = totalmenos = cont = 0
nome_barato = ' '
while True:
    nome = str(input('Nome do produto:'))
    preço = float(input('Peço do Produto:R$'))
    total += preço
    cont += 1
    if preço > 1000:
        totmais += 1
    if cont == 1:
        totalmenos = preço
        nome_barato = nome
    else:
        if preço < totalmenos:
            totalmenos = preço
            nome_barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Vc quer continuar [S/N]')).strip().upper()[0]
        print('-' * 45)
    if resp == 'N':
        break
print(f'O valor total foi {total:.2f}')
print(f'{totmais} produtos custam mais de R$ 1000.00')
print(f'O produto mais barato foi {nome_barato} e custou R$ {totalmenos:.2f}')
print('FIM')
