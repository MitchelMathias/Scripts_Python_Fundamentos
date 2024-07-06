matriz = []
soma = soma_col = 0
print(f'{"=-="*7}BEM VINDO A MATRIZ{"=-="*7}')
while True:
    tamanho = input('Digite o tamanho da matriz OU (enter para encerrar):')
    if tamanho == '':
        break
    elif tamanho.isdigit():
        tamanho = int(tamanho)
        if tamanho == 0:
            print('Valor invalido')
        elif tamanho > 0:
            matriz = [[0] * tamanho for _ in range(tamanho)]
            for linha in range(tamanho):
                for coluna in range(tamanho):
                    matriz[linha][coluna] = int(input(f'Digite um valor para [{linha+1},{coluna+1}]:'))
            print('Matriz logo abaixo:')
            for linha in range(tamanho):
                for coluna in range(tamanho):
                    print(f'[{matriz[linha][coluna]:^7}]', end='')
                print()
            for linha in matriz:
                for elemento in linha:
                    if elemento % 2 == 0:
                        soma += elemento
            print(f'A soma dos números pares desta matriz é: {soma}')
            maior = matriz[1][0]
            for elemento in matriz[1]:
                if elemento > maior:
                    maior = elemento
            print(f'O maior numero na segunda linha é o Nr: {maior}')
            for linha in matriz: # amanha vamos perguntar qual coluna o usuário quer somar.
                soma_col += linha[2]
            print(f'A soma da coluna 3 é: {soma_col}')