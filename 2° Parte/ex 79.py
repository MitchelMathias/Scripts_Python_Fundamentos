valores = []
print('=-='*20)
print('=-='*20)
print(f'{"Digite um numero abaixo OU enter para encerrar.":^60}')
print('=-='*20)
print('=-='*20)
while True:
    entrada = input('Digite um numero:')
    if entrada == '':
        break
    if entrada.isdigit():
        valor = int(entrada)
        if valor not in valores:
            print('Valor adicionado...')
            valores.append(valor)
        else:
            print('Valor duplicado, não vou adicionar...')
    else:
        print('Inválido tente Novamente')
print('=-='*20)
print('=-='*20)
print(f'Os valores em ordem crescente são :{sorted(valores)}')
