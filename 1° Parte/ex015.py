print('Hora de calcular o valor de aumento pra cada funcionario da empresa?\n'
      '\n'
      'Vou te ajudar a calcular de maneira automatizada e economizar seu tempo!!.')
a = float(input('Qual o salário do funcionário? R$'))
b = float(input('Agora quantos % de aumento? %'))
c = (a * b) / 100 + a
print('O valor do novo salário é de R${:.2f}'.format(c))
