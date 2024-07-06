print('Vamos calcular seu IMC')
sexo = str(input('Qual seu sexo?')).lower().strip()
peso = float(input('Qual o seu peso?'))
altura = float(input('Qual a sua altura?'))
imc = peso / (altura ** 2)
print('Seu IMC é {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está abaixo do peso.')
    # if sexo == 'homem':
    # peso_ideal = altura * 72.7 - 58
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))
    # elif sexo == 'mulher':
    # peso_ideal = altura * 62.1 - 44.7
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))
elif 18.5 < imc <= 25.0:
    print('Você está no peso ideal.')
    # if sexo == 'homem':
    # peso_ideal = altura * 72.7 - 58
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))
    # elif sexo == 'mulher':
    # peso_ideal = altura * 62.1 - 44.7
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))
elif 25.0 < imc <= 30.0:
    print('Você está com sobrepeso.')
    # if sexo == 'homem':
    # peso_ideal = altura * 72.7 - 58
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))
    # elif sexo == 'mulher':
    # peso_ideal = altura * 62.1 - 44.7
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))
elif 30.0 < imc <= 40.0:
    print('Você está com obesidade.')
    # if sexo == 'homem':
    # peso_ideal = altura * 72.7 - 58
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))
    # elif sexo == 'mulher':
    # peso_ideal = altura * 62.1 - 44.7
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))
elif imc > 40:
    print('Você está com obesidade mórbida.')
    # if sexo == 'homem':
    # peso_ideal = altura * 72.7 - 58
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))
    # elif sexo == 'mulher':
    # peso_ideal = altura * 62.1 - 44.7
    # print('Seu peso ideal é {:.2f}'.format(peso_ideal))


if sexo in ['homem', 'masculino', 'm', 'macho']:
    peso_ideal = altura * 72.7 - 58
    print('Seu peso ideal é {:.2f}'.format(peso_ideal))
elif sexo in ['mulher', 'femea', 'f']:
    peso_ideal = altura * 62.1 - 44.7
    print('Seu peso ideal é {:.2f}'.format(peso_ideal))
x = peso - peso_ideal
if x < 0:
    print('Voce deve engordar {:.2f}kg'.format(-x))
elif x > 0:
    print('Voce deve emagrecer {:.2f}kg'.format(x))
else:
    print('Você esta no peso ideal')
