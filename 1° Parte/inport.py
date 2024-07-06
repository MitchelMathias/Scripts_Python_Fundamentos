from math import sqrt

num = int(input('Digite o número que deseja achar a '
                'raiz quadrada:'))
raiz = sqrt(num)
print('A raiz Quadrada de {} é igual a {:.3f}'.format(
    num, raiz))
