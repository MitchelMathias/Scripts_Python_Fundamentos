import unidecode

print('-=-' * 20)
print('              Calculador de juros e descontos')
print('-=-' * 20)
preco = float(input('Qual o preço do produto?'))
pagamento = str(input('Qual a condição de pagamento?').lower().strip())
pagamento = unidecode.unidecode(pagamento)
if pagamento == 'dinheiro' or pagamento == 'cheque' or pagamento == 'a vista' or pagamento == 'debito':
    desconto_10 = preco * 10 / 100
    print('O valor final do produto é R${}.'.format(preco - desconto_10))
elif pagamento == 'credito':
    vezes = int(input('Quantas vezes?'))
    if vezes == 1:
        desconto_5 = preco * 5 / 100
        print('O valor final do produto é R${}.'.format(preco - desconto_5))
    elif vezes == 2:
        print('O valor do produto é 2x de R${}'.format(preco / 2))
    elif vezes >= 3:
        xxx = (preco * 20 / 100 + preco) / vezes
        print(f'O valor final do produto é {vezes}x de R$ {xxx}')
else:
    print('Esse valor não é valido')
