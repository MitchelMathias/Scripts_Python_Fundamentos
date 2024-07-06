import math

ang = float(input('Qual ângulo você gostaria de saber seu seno, cos, tan?'))
angg = math.radians(ang)
seno = math.sin(angg)
cos = math.cos(angg)
tang = math.tan(angg)
print('Referente ao ângulo {}°\n'
      'seu seno é {:.2f}\n'
      'seu coseno é {:.2f}\n'
      'sua tangente é {:.2f}'.format(ang, seno, cos, tang))
