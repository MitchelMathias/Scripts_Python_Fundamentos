sexo = str(input('Digite seu sexo [M/F]:')).upper()
while sexo not in ['M', 'F']:
    print('dados invalidos')
    sexo = str(input('Digite seu sexo [M/F]:')).upper()
print('Sexo {} resgistrado comc sucesso.'.format(sexo))
