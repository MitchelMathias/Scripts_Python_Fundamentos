print('=-='*18)
print(f'{"Dicionario":^35}')
print('=-='*18)
dicionario = {}
while True:
    resp = str(input('Inserir integrante [S/N]:'))
    if resp.lower() == 'n':
        break
    elif resp.isdigit():
        print('Comando Inválido')
    else:
        print()
        dicionario['Nome'] = str(input('Qual o Nome: '))
        dicionario['idade'] = 2024 - int(input('Que ano Nasceu: '))
        dicionario['Carteira'] = input('Registro da Carteira de trabalho (Caso não tenha Digite Não): ')
        if dicionario['Carteira'].lower() in 'não':
            dicionario['Carteira'] = 'Não tem'
            print('=-=' * 18)
            break
        if dicionario['Carteira'].isdigit():
            dicionario['Ano de contratação'] = str(input('Qual o Ano de Contratação:'))
            dicionario['Salário'] = float(input('Digite o Sálario:'))
            dicionario['Falta '] = 65 - dicionario['idade']
            print('=-='*18)
            break
print('Dados:')
for key, valor in dicionario.items():
    print(f'    - {key}: {valor}')
print('=-='*18)
