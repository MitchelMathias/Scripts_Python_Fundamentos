p1 = int(input('Primeiro termo?'))
r = int(input('Qual a razão?'))
for c in range(p1, p1 + 10 * r, r):
    print(c, end='-')
print('\n'
      'Terminou')
