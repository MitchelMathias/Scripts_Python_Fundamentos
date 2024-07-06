a = float(input('Quantos metros você gostaria de converter para todas unidades de medida?'))
cm = a * 100
mm = a * 1000
dm = a * 10
dam = a / 10
hm = a / 100
km = a / 1000
print('O valor de {} metros\n'
      '10em centimetros é de {}\n'
      'em milimetros é {}\n'
      'em decimetro é {}\n'
      'em decâmetro é {}\n'
      'em hectômetro é {}\n'
      'e por fim em kilometro é de {}.\n'
      '\n'
      'espero ter ajudado!!'.format(a, cm, mm, dm, dam, hm, km))
