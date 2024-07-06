n = int(input('Digite um numero de 0 a 99999:'))
unidade = n % 10
dezena = (n // 10) % 10
centena = (n // 100) % 10
milhar = (n // 1000) % 10
dezena_milhar = (n // 10000) % 10
print(f'unidade:{unidade}')
print(f'dezena:{dezena}')
print(f'centena:{centena}')
print(f'milhar:{milhar}')
print((f'dezena de milhar: {dezena_milhar}'))

# ou
# n = int(input('Digite um numero de 0 a 99999:'))
# n = str(num)
# print('Analisando o numero {}.'.format(num))
# print(f'unidade:{}'.format(n[4]))
# print(f'dezena:{}'.format(n[3]))
# print(f'centena:{}'.format(n[2]))
# print(f'milhar:{}'.format(n[1]))
# print((f'dezena de milhar: {}'.format(n[0]))
