print('********* Progreção Aritimética *********')
primeiro = int(input('Digite o 1° termo da PA:'))
razao = int(input('Digite a razão:'))

termo = primeiro
contador = 1
total = 0
mais = 10
mensagem_exibida = False # faz ser repitida apenas uma vez
while mais != 0: # enquanto foi diferente de 0 vai repetir o programa
    total = total + mais
    while contador <= total:
        print('{} - '.format(termo), end='')
        termo = termo + razao
        contador = contador + 1
    print('Pausa.')

    if not mensagem_exibida: # faz ser repitida apenas uma vez
        print('Aqui estão os {} primeiros termos'.format(total))
        mensagem_exibida = True # faz ser repitida apenas uma vez

    usuario = input('\nDigite o numero de termos que vc quer a mais?\n'
                    'Ou digite 0 para finalizar o programa.')
    if usuario.strip() == '': # verifica se é uma string vazia se sim ele encerra
        mais = 0
    elif usuario.isdigit(): # verifica se é um numero se sim ele transforma mais nesse numero
        mais = int(usuario)
    else: # verifica se é uma string qualquer, se sim ele encerra o programa
        print('')
        mais = 0
print('Progressão finalizada com {} temos no total'.format(total))
