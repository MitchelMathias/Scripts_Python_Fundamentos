n1 = int(input('Digite um numero:'))
n2 = int(input('Digite um numero:'))
n3 = int(input('Digite um numero:'))
lis = [n1, n2, n3]
if lis:
    nn_max = max(lis)
    nn_min = min(lis)
    print('O maior numero digitado é {:.1f}'.format(nn_max))
    print('O menor numero digitado é {:.1f}'.format(nn_min))
else:
    print('Nenhum numero fornecido')
