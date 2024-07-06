print('=-=' * 20)
print(f'{"Dados":^60}')
print('=-=' * 20)
dados = []
while True:
    pessoa = {'Nome': str(input('Nome: ')).strip()}
    while not pessoa['Nome'].isalpha():
        print('Digite somente letras.')
        pessoa['Nome'] = str(input('Nome: ')).strip()
    pessoa['Sexo'] = str(input('Sexo [M/F]:'))
    while pessoa['Sexo'].lower().strip() not in 'fm':
        print('Digite somente "F" ou "M"')
        pessoa['Sexo'] = str(input('Sexo [M/F]:'))
    pessoa['Idade'] = input('Idade:')
    while True:
        if not pessoa['Idade'].isdigit():
            print('Digite apenas número.')
            pessoa['Idade'] = input('Idade:')
        elif pessoa['Idade'].isdigit():
            pessoa['Idade'] = int(pessoa['Idade'])
            break
    resp = str(input('Quer Continuar?[S/N]:'))
    while resp.lower() not in 'sn':
        print('Digite somente "S" ou "N"')
        resp = str(input('Quer Continuar?[S/N]:'))
    dados.append(pessoa)
    if resp.lower() in 'n':
        break
idades = [dicionario['Idade'] for dicionario in dados]
mulheres = [dicionario['Nome'] for dicionario in dados if dicionario['Sexo'] == 'f']
print('=-=' * 20)
print('Resultado:')
print(f'    => Teve um total de {len(dados)} pessoas cadastradas')
print(f'    => A média de Idade das pessoas foi: {sum(idades) / len(dados)} anos.')
print(f'    => As mulheres cadastradas são: {', '.join(mulheres)}')
print(f'    => As pessoas acima da Média de Idade estão abaixo:')
for dicionario in dados:
    if dicionario['Idade'] > sum(idades) / len(dados):
        print(f'        => Seu nome é {dicionario['Nome']} com {dicionario['Idade']} anos')
print('=-=' * 20)
