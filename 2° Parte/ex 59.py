n1 = float(input('Digite um numero:'))
n2 = float(input('Digite um numero:'))
opcao = 0
while opcao != 6:
    print('')
    print('Oque deseja fazer com esses numeros.\n'
          '[ 1 ] somar\n'
          '[ 2 ] multiplicar\n'
          '[ 3 ] maior\n'
          '[ 4 ] menor\n'
          '[ 5 ] novos números\n'
          '[ 6 ] sair do programa')
    opcao = int(input('Digite uma das opções:'))

    if opcao == 1:
        soma = n1 + n2
        print('')
        print('********A soma de {} e {} é =:{}********'.format(n1, n2, soma))

    elif opcao == 2:
        x = n1 * n2
        print('********A multiplicação de {} e {} é =:{}********'.format(n1, n2, x))

    elif opcao == 3:
        if n1 != n2:
            lista = [n1, n2]
            maior = max(lista)
            menor = min(lista)
            print('o maior numero entre {} e {} é {}'.format(n1, n2, maior))
        else:
            print('São iguais.')
    elif opcao == 4:
        if n1 != n2:
            lista = [n1, n2]
            maior = max(lista)
            menor = min(lista)
            print('o maior numero entre {} e {} é {}'.format(n1, n2, menor))
        else:
            print('São iguais.')
    elif opcao == 5:
        print('Digite novamente os numeros')
        n1 = float(input('Digite um numero:'))
        n2 = float(input('Digite um numero:'))
    elif opcao == 6:
        print('finalizando...')
    else:
        print('Essa opção não é valida')
print('Fim do programa')
