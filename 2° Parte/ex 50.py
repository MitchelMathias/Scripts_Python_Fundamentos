s = 0
contp = 0
cont = 0
so_par = 0
so_imp = 0
for c in range(6):
    n = int(input('Digite o {}° número inteiro:'.format(c+1)))
    s = s + n
    if n % 2 == 0:
        contp += 1
        so_par += n
    else:
        cont += 1
        so_imp += n
print(' ')
print('A soma dos {} números pares são:{}'.format(contp, so_par))
print('A soma dos {} números impares são:{}'.format(cont, so_imp))
print('soma de todos os numeros é: {}'.format(s))
