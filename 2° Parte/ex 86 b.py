matriz = []
while True:
    tamanho = input('Digite o Tamanho da matriz ou (enter para encerrar):')
    if tamanho == '':
        break
    if tamanho.isdigit():
        tamanho = int(tamanho)
        if tamanho == 0:
            break
        elif tamanho > 0:
            matriz = [[0] * tamanho for _ in range(tamanho)]
            for linha in range(tamanho):
                for coluna in range(tamanho):
                    matriz[linha][coluna] = int(input(f'Digite um numero em [{linha+1},{coluna+1}]:'))
            print('=-='*30)
            print('Resultado da Matriz abaixo:')
            for linha in range(tamanho):
                for coluna in range(tamanho):
                    print(f'[{matriz[linha][coluna]:^7}]', end='')
                print()
