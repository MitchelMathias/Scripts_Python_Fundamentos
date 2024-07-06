from datetime import date

nascimento = int(input('Que ano vc nasceu?'))
idade = date.today().year - nascimento
print(f'sua idade é de {idade} anos.')
if idade <= 5:
    print('Espere mais um pouco você ainda é jovem.')
elif idade <= 9:
    print('Portanto sua categoria é Mirim')
elif idade <= 14:
    print('Portanto sua cate2ria é Infantil')
elif idade <= 19:
    print('Portanto sua categoria é junior')
elif idade <= 25:
    print('Portanto sua categoria é Senior')
else:
    print('Portanto sua categoria é master')
