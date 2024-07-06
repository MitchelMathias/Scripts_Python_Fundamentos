from datetime import date
print('''Escolha uma opção:
[1] Homem
[2] mulher''')
sexo = int(input(':'))
if sexo == 1:
    ano = int(input('Em qual ano você nasceu?'))
    calculo = date.today().year - ano
    print(f'Quem nasceu em {ano} tem {calculo} anos em {date.today().year}')
    if calculo >= 19:
        calculos = calculo - 18
        print('Você ja serviu ou deveria ter servido a {} anos'.format(date.today().year - calculos))
    elif calculo <= 17:
        calculos = 18 - calculo
        print('Você ainda deve se alistar em {} anos no ano {}'.format(calculos, calculos + date.today().year))
    else:
        print('Você deve se alistar o quanto antes')
else:
    print('Você não precisa Servir')
