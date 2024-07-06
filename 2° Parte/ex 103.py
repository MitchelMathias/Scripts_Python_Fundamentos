def lin():
    print('='*55)


def ficha(no="desconhecido", go=0):
    print(f'O jogador {no.upper().strip()} fez {go} gol(s) no campeonato.')


lin()
print(f'{'Ficha do Jogador':^55}')
lin()
n = str(input('Nome do Jogador: '))
g = str(input('Quantidade de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(go=g)
else:
    ficha(n, g)
