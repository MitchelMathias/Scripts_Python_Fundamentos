import unidecode

media = 0
idade_h_velho = 0
nome_h_velho = 0
soma_menor = 0
for c in range(4):
    print('----- {}° Pessoa -----'.format(c + 1))
    nome = str(input('Nome:')).strip().capitalize()
    nome = unidecode.unidecode(nome)
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().lower()
    media = media + idade / 4
    if c == 1 and sexo in 'm':
        idade_h_velho = idade
        nome_h_velho = nome
    elif sexo in 'm' and idade > idade_h_velho:
        idade_h_velho = idade
        nome_h_velho = nome
    if sexo in 'f' and idade < 18:
        soma_menor = soma_menor + 1
print('A média deste grupo é de: {} anos'.format(media))
print('O homem mais velho é: {}, com {}'.format(nome_h_velho, idade_h_velho))
print('Ao todo temos: {} mulheres menor de 18 Anos'.format(soma_menor))
