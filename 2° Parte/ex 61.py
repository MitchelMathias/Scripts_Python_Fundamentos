print('********* Progreção Aritimética *********')
primeiro = int(input('Digite o 1° termo da PA:'))
razao = int(input('Digite a razão:'))

termo = primeiro
contador = 1
while contador <= 10:
    termo = termo + razao
    contador = contador + 1
    print('{} - '.format(termo), end='')
