print('='*47)
print(f'{"Goleadores":^47}')
print('='*47)
time = []
while True:
    jogador = {'Nome': str(input(' Nome do Jogador: ')).strip()}
    while not jogador['Nome'].isalpha():
        print('Digite somente letras em Nome: ')
        jogador['Nome'] = str(input('Nome do Jogador: ').strip())
    jogador['Partidas'] = input(f'  - Quantas partidas {jogador['Nome']} jogou: ').strip()
    while True:
        if jogador['Partidas'].isalpha():
            print('Digite somente Números...')
            jogador['Partidas'] = input(f'  - Quantas partidas {jogador['Nome']} jogou: ').strip()
        elif jogador['Partidas'].isdigit():
            jogador['Partidas'] = int(jogador['Partidas'])
            break
    jogador['Gols'] = []
    for c in range(0, jogador['Partidas']):
        golss = input(f'    - Quantos Gols na {c+1}° partida:').strip()
        while not golss.isdigit():
            golss = input(f'    - Quantos Gols na {c + 1}° partida:').strip()
        if golss.isdigit():
            golss = int(golss)
        jogador['Gols'].append(golss)
    resp = str(input('Quer continuar [S/N]:')).strip()[0]
    while not resp.lower() in 'sn':
        print('Digite "S" ou "N".')
        resp = str(input('Quer continuar [S/N]:')).strip()[0]
    print('='*47)
    jogador['Total'] = sum(jogador['Gols'])
    del jogador['Partidas']
    time.append(jogador)
    if resp.lower() in 'n':
        break
print(f'{'Ord.':<6}{'Nome':<18}{'Gols':<16}{'Total'}')
for i, valor in enumerate(time):
    print(f'{i+1:>2}°', end='  ')
    for d in valor.values():
        print(f'{str(d):<18}', end='')
    print()
print('='*47)
while True:
    per = input('Digite o Nr Ord. do jogador para mais dados\n'
                '(pressione Enter para cancelar)').strip()[0]
    if per == '':
        break
    if int(per) > len(time):
        print('Jogador não cadastrado')
    if int(per) <= len(time):
        per = int(per)
        break
print(f'-- Desempenho do jogador {time[per-1]['Nome']}')
for i, v in enumerate(time[per-1]['Gols']):
    print(f'    => {i+1}° partida o jogador {time[per-1]['Nome']}, fez {v} gols. ')
print(f'    => O total de gols foi {time[per-1]['Total']}')
print('='*47)
