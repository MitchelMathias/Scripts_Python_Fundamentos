"""print('************** Squencia de Fibonati **************')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
num = int(input('Quantos Numeros você quer mostrar?'))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
t1 = 0
t2 = 1
print(f'{t1} - {t2} -', end='')
cont = 3
total = 0
mais = num
while mais != 0:
    total = total + mais
    while cont <= total:
        t3 = t1 + t2
        print(f'{t3} - ', end='')
        t1 = t2
        t2 = t3
        cont = cont + 1
    mais = int(input('mais quantos:'))
print('Foram expostos {} numeros'.format(cont - 1))
print('fim')"""
print('Sequencia Fibonati')
num = int(input('Digite a quantidade:'))
t1 = 0
t2 = 1
print(f'{t1} - {t2} - ', end='')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(f'{t3} - ', end='')
    cont += 1
    t1 = t2
    t2 = t3
print('Fim')
