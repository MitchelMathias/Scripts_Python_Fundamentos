total18 = mulher_menor = homem = 0
while True:
    print('*' * 40)
    print(f'{'Cadastre uma pessoa':^40}')
    print('*' * 40)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo[F/M]:')).strip().upper()[0]
    resp = ' '
    if idade >= 18:
        total18 += 1
    if sexo == 'F' and idade < 18:
        mulher_menor += 1
    if sexo == 'M':
        homem += 1
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de pessoas acima de 18 anos é {total18}')
print(f'Ao todo temos {homem} homens cadastrado.')
print(f'Nesse grupo temos {mulher_menor} mulheres menor de idade')
