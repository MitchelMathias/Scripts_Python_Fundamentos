extenso = ('zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
           'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
x = ''
while True:
    x = input('Digite um numero ou enter para sair:')
    if x == '':
        print('Encerrando o programa')
        break
    elif not x.isdigit():
        print('Entrada invalida.')
    else:
        x = int(x)
        if x < 0 or x > 20:
            print('Numero Inválido')
        else:
            print(f'você digitou o numero {extenso[x]}')
