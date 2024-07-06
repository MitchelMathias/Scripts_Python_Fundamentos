print('Digite quantos numeros voce quiser, apenas de um espaço de um numero para outro')
n = input(':')
nn = [float(nn) for nn in n.split()]
if nn:
    nn_max = max(nn)
    nn_min = min(nn)
    print('O maior numero digitado é {:.1f}'.format(nn_max))
    print('O menor numero digitado é {:.1f}'.format(nn_min))
else:
    print('Nenhum numero fornecido')
