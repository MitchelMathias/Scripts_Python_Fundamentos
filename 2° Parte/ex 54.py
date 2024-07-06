from datetime import date

atual = date.today().year
totmaior = 0
totmenor = 0
for c in range(7):
    nasc = int(input('Em que ano a {}° pessoa nasceu?'.format(c + 1)))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print('temos {} pessoas maior de idade'.format(totmaior))
print('temos {} pessoas menor de idade'.format(totmenor))
