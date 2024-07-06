from time import sleep

s = 0
for c in range(1, 51):
    if c % 2 == 0:
        print(c, end='-')
        sleep(0.5)
        s += c
print('\n'
      'soma =', s)
