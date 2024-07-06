valor = float(input('Qual o valor da Casa?R$'))
salario = float(input('Qual seu sálario?R$'))
anos = int(input('Quantos anos de deseja pagar esse financiamento?'))
parcelas = valor / (anos * 12)
minimo = salario * 30 / 100
if parcelas <= minimo:
    print('parabens pela compra!!!')
    print('O valor da parcela é de {:.2f}'.format(parcelas))
else:
    print('O valor da parcela exede 30% da sua renda')
    print('Ficaria uma parcela de {:.2f}'.format(parcelas))
print('Obrigado pela preferência')
