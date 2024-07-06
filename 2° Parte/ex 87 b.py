matriz = []
soma_par = coluna3 = maior2 = 0
while True:
    tamanho = input('Digite o Tamanho da Matriz ou (enter para encerrar):')
    if tamanho == '':
        break
    if tamanho.lower() in 'abcdefghijklmnopqrstuvxyz':
        print('Inválido, tente novamente.')
    if tamanho.isdigit():
        tamanho = int(tamanho)
        if tamanho >= 1:
            matriz = [[0] * tamanho for _ in range(tamanho)]
            for linha in range(tamanho):
                for coluna in range(tamanho):
                    while True:
                        try:
                            matriz[linha][coluna] = int(input(f'Digite um valor para posição [{linha+1}, {coluna+1}]:'))
                            break
                        except ValueError:
                            print('Valor inválido, tente novamente.')
            print('=-='*35)
            print('Matriz logo abaixo:')
            for linha in range(tamanho):
                for coluna in range(tamanho):
                    print(f'[{matriz[linha][coluna]:^7}]', end='')
                    if matriz[linha][coluna] % 2 == 0:
                        soma_par += matriz[linha][coluna]
                if tamanho >= 3:
                    coluna3 += matriz[linha][2]
                else:
                    coluna3 = 0
                print()
            for elemento in matriz[1]:
                if elemento > maior2:
                    maior2 = elemento
            print('=-=' * 35)
            print(f'A soma dos números pares são: {soma_par}')
            print(f'A soma da coluna 3 é :{coluna3}')
            print(f'O maior numero na segunda linha é {maior2}')
            print('=-=' * 35)
