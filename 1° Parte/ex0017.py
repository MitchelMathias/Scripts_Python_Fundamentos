d = int(input('Quantos dias você utilizou o carro?'))
km = float(input('Quantos Km você percorreu?'))
dc = d * 60
dk = km * 0.15
#pode se usar qualquer um dos dois métodos, com 3 variaveis ou uma variavel completa
cc = (d * 60) + (km * 0.15)
c = dc + dk
print('O custo total do aluguel do veículo pelo uso de {:.0f} '
      'dias acrescentando o valor de {:.2f}km percorrido é '
      'de um total de R${:.2f}'.format(d, km, cc))
