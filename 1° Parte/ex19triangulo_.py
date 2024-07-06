import math

catO = float(input('Qual o comprimento do cateto Oposto deste triangulo?(oque esta na vertical)'))
catA = float(input('Qual o comprimento do cateto adjacente deste triangulo?(Oque esta na horizontal)'))
hip = math.hypot(catO, catA)
print('A hipotenusa é de {:.2f}.'.format(hip))
