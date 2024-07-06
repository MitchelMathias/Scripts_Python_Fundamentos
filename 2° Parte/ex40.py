print('vamos calcular média')
p1 = int(input('Quanto vale a 1° prova ?'))
p2 = int(input('Quanto vale a 2° Prova ?'))
soma = p1 + p2
if soma == 20:
    n1 = float(input('Qual a 1° Nota? '))
    n2 = float(input('Qual a 2° Nota? '))
    media = (n1 + n2) / 2
    if media < 5.0:
        print('Você está reprovado.')
    elif 5.0 <= media < 7.0:
        print('Você está em recuperação.')
    else:
        print('Você está aprovado.')
elif soma == 200:
    n1 = float(input('Qual a 1° Nota? '))
    n2 = float(input('Qual a 2° Nota? '))
    media = (n1 + n2) / 2
    media = media / 10.0
    if media < 5.0:
        print('Você está reprovado.')
    elif 5.0 <= media < 7.0:
        print('Você está em recuperação.')
    else:
        print('Você está aprovado.')
