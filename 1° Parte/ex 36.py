salario = float(input('Qual o salario do funcionário? R$'))
if salario >= 1250:
    x = salario * 10 / 100 + salario
    print(f'O novo salário é de R$ {x}')
else:
    x = salario * 15 / 100 + salario
    print(f'O novo salário é de R$ {x}')
print('Parabens!!')
