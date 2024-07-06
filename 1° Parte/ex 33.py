km = float(input('Quantos km tem sua viagem?'))
# ou pode se fazer assim. preço = km * 0.50 if km <= 200 else *4.45
if km <= 200:
    perto = km * 0.50
    print('O valor da sua passagem é de R$ {:.2f}'.format(perto))
else:
    longe = km * 0.45
    print('O valor da sua passagem é de R$ {:.2f}.'.format(longe))
print('Tenha um ótima viagem!!')
