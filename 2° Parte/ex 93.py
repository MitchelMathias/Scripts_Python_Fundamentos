print('='*45)
print(f'{"Goleadores":^35}')
print('='*45)
goleador = {}
while True:
    goleador['Nome'] = str(input('Nome do Jogador:'))
    goleador['Partidas'] = int(input(f'Quantas partidas o {goleador['Nome']} jogou:'))
    goleador['Gols'] = []
    for c in range(0, goleador['Partidas']):
        golss = int(input(f'    - Quantos gols na {c+1}° Partida?'))
        goleador['Gols'].append(golss)
    goleador['total'] = sum(goleador['Gols'])
    print('='*45)
    print(f'{goleador}')
    print(f'O total de Gols foi de: {goleador['total']}')
    print('='*45)
    for k, v in goleador.items():
        print(f'O campo {k} tem o valor {v}')
    print('='*45)
    print(f'O jogador {goleador['Nome']}, jogou {goleador['Partidas']} partidas.')
    for i, v in enumerate(goleador['Gols']):
        print(f'    => Na {i+1}° partida o jogador {goleador['Nome']} fez {v} gols.')
    print(f'Foi um total de {goleador['total']} gols.')
    break
