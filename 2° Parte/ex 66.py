cont = 0
soma = 0
n = 0
print('clique Enter sem numero para parar.')
while True:
    n = input('Digite um numero:')
    if not n:
        break
    if n.isdigit():
        n = int(n)
        cont += 1
        soma += n
    else:
        print('Valor invalido digite novamente')
print(f'Foram digitados {cont} numeros e sua soma é {soma}')
