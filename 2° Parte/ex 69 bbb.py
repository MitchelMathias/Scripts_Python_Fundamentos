homem = mulher_menor = maior_idade = 0

while True:
    print('*' * 40)
    print(f'{"Cadastre uma pessoa":^40}')
    print('*' * 40)
    nome = str(input('Qual seu nome:')).capitalize().strip()
    idade = int(input('Qual sua idade:'))
    sexo = str(input('Qual seu sexo:[F/M]')).upper()

    if idade > 18:
        maior_idade += 1

    if sexo == 'F' and idade < 18:
        mulher_menor += 1

    if sexo == 'M':
        homem += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas acima de 18 anos é {maior_idade}')
print(f'Ao todo temos {homem} homens cadastrados.')
print(f'Nesse grupo temos {mulher_menor} mulheres menores de idade.')
