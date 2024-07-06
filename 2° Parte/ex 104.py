def leiaInt(msg):
    while True:
        nu = input(msg)
        if nu.isnumeric():
            return nu
        else:
            print('ERROR! Digite um numero válido')


n = leiaInt('Digite um numero:')
print(f'O valor que você digitou foi {n}.')
