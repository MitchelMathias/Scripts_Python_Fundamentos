"""listagem = ('Lápis','1.75',
            'Borracha', '2.00',
            'Caderno', '15.90',
            'Estojo', '25',
            'Trasferidor', '4.20',
            'Compasso', '9.95',
            'Mochila', '120.35',
            'Canetas', '22.30',
            'Livro', '34.85')
print('-'*45)
print(f'{'LISTAGEM DE PREÇOS':^45}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<35}',end='')
    if pos % 2 != 0:
        preço = float(listagem[pos]) # assim trasnforma em número flutuante as str
        print(f'R$ {preço:>7.2f}')"""

listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 20,
            'Trasferidor', 4.20,
            'Compasso', 9.95,
            'Mochila', 120.35,
            'Canetas', 22.30,
            'Livro', 34.85)  # escrevendo os numeros fora de aspas não precisa transformar em flutuante
print('-' * 45)
print(f'{'LISTAGEM DE PREÇOS':^45}')
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<35}', end='')
    if pos % 2 != 0:
        print(f'R$ {listagem[pos]:>7.2f}')
print('')
print('-' * 45)
