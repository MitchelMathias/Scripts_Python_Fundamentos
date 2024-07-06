n1 = int(input('Digite um valor:'))
n2 = int(input('Digite o outro valor:'))
nome = str(input('Cade minha educação.\nQual o seu nome?'))
print(
    'A soma, subitração,divisão e multiplicação dos seu numeros é nessa ordem.\n{},{},{},{}, gostou dos carcteries que '
    'eu coloquei no seu {} pra ficar bonito sr {:=^15}?'.format(
        n1 + n2, n1 - n2, n1 / n2, n1 * n2, nome, nome))
print('Quase esqueci, a exponeciação dos valores é {}'.format(n1 ** n2))