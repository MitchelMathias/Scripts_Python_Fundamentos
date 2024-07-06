soma_idades = 0
media_idade = 0
maior_idade_homem = 0
homem_velho = ''
mulher20 = 0
for c in range(4):
    print('----- {}° PESSOA -----'.format(c+1))
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Qual sua Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper()
    soma_idades = soma_idades + idade
    if c == 1 and sexo in 'M':
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_velho = nome
    if sexo in 'F' and idade < 18:
        mulher20 = mulher20 + 1
        if mulher20 == 1:
            print('Ao todo são {} mulher com menos de 18 anos'.format(mulher20))
        else:
            print('Ao todo são {} mulheres com menos de 18 anos'.format(mulher20))
media_idade = soma_idades / 4
print('a média de idade deste grupo é de {} anos.'.format(media_idade))
print('O homem mais velho é {} com a idade de {} anos'.format(homem_velho, maior_idade_homem))
