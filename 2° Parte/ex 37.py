numero = input('Digite um número inteiro:')

if not numero.isdigit():
    print('Por favor, insira um número inteiro válido:')
else:
    numero = int(numero)
    print('''Escolha uma das bases de conversão:
    [1] Converter para binário
    [2] Converter para octal
    [3] Converter para hexadecimal''')

    opcao = int(input('Sua opção:'))

    if opcao == 1:
        print('{} convertido para binário é igual a {}'.format(numero, bin(numero)[2:]))
    elif opcao == 2:
        print('{} convertido para octal é igual a {}'.format(numero, oct(numero)[2:]))
    elif opcao == 3:
        print('{} convertido para hexadecimal é igual a {}'.format(numero, hex(numero)[2:]))
    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
