print('Bem Vindo ao conversor de Dolar, Euro e Libra Sterlina')
real = float(input('Quantos reais gostaria de converter? R$'))
dolar = real / 4.9
euro = real / 5.36
libra = real / 6.18
print('Com R${}, você pode comprar as seguintes quantidades abaixo relacionadas\n'
      '{:.2f} Dolares\n'
      '{:.2f} Euros\n'
      '{:.2f} Libras Sterlinas\n'
      '\n'
      'Desejo Sorte nas suas transações!!!'.format(real, dolar, euro, libra))
