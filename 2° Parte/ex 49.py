a = int(input('Você quer a tabuada completa de qual número?'))
for s in range(0, 11):
    r = a * s
    print('{} x {} = {}'.format(a, s, r))
