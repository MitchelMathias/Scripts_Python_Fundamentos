print('Todo mundo gosta de um desconto certo?\n'
      '\n'
      'Vou te ajudar a calcular esse desconto e nunca mais entregar o valor errado.')
a = float(input('Me diga o valor do produto? R$'))
b = float(input('Agora quantos % de desconto?'))
c = (a * b) / 100
d = a - c
print('O valor que deve ser cobrado do cliente é de R${:.2f}'.format(d))
