from datetime import date
ano = int(input('Você deseja saber se qual ano é, foi ou será um ano bissexto?'))
bis = (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0
if ano == 0:
    ano = date.today().year
if bis:
    print(f'O ano {ano} é Bissexto.')
else:
    print(f'O ano {ano}, não é Bissexto')
print('Espero ter ajudado!!')
