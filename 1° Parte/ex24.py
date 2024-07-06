nome = str(input('Digite seu nome completo:')).strip()  # strip tira os espaço antes e final
print('Analisando seu nome ...')
maiusculo = (nome.upper())  # print('Seu nome maiusculo é {}'.format(nome.upper()))
minusculo = (nome.lower())  # print('Seu nome maiusculo é {}'.format(nome.lower()))
letras = nome.split()
sem_espaco = (len(nome) - nome.count(' '))
primeiro = letras[0]
quantidade = len(letras[0])
print(f'Seu nome em maiúsculas é {maiusculo}')
print(f'Seu nome em minusculo é {minusculo}')
print(f'Seu nome tem ao todo {sem_espaco} letras.')
print(f'seu primeiro nome é {primeiro}, e ele tem {quantidade} letras')
