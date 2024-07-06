print('=-=' * 35)
print(f'{'MÉDIA DE NOTAS':^65}')
print('=-=' * 35)
ficha = []
while True:
    nome = str(input('Digite o nome:'))
    nota1 = float(input('1° Nota: '))
    nota2 = float(input('2° Nota: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer Continuar? [S/N]'))
    if resp.lower() in 'não':
        break
print('=-=' * 35)
print(f'{"Nr":^4}{"Nome":^8}{"Média":^9}')
for i, a in enumerate(ficha):
    print(f'{i + 1:<5}{a[0]:<10}{a[2]:>8.2f}')
print('=-=' * 35)
while True:
    resposta = input('Digite o numero do aluno para ver as notas?\n'
                     'ou (pressione "enter" para interromper):')
    if resposta.lower() == '':
        print('Volte Sempre...')
        break
    if resposta.isdigit():
        resposta = int(resposta) - 1
        if resposta > len(ficha):
            print(f'Notas de {ficha[resposta][0]} são {ficha[resposta][1]}')
        else:
            print('Numero inválido...')
            