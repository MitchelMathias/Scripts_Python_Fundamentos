print('=' * 35)
print(f'{"Boletin final":^36}')
print('=' * 35)
boletins = []
while True:
    dados = {'Nome': str(input('Digite o Nome: ')), '1° Nota': float(input('1° Prova: ')),
             '2° Nota': float(input('2° Prova: '))}
    media = (dados['1° Nota'] + dados['2° Nota']) / 2
    dados['Média'] = media
    boletins.append(dados)
    resp = str(input('Quer Continuar? [S/N]'))
    print('=' * 35)
    if resp.lower() in 'n':
        break
for d in boletins:
    for k, v in d.items():
        print(f'    - {k} é igual {v}')
    if d['Média'] >= 7:
        d['Situação'] = 'Aprovado'
    elif 5 >= d['Média'] < 7:
        d['Situação'] = 'Recuperação'
    elif d['Média'] < 5:
        d['Situaação'] = ['Reprovado']
    print('=' * 35)
