valores = []
mai = 0
men = 0
for c in range(0, 5):
    while True:
        try:
            valores.append(int(input('Digite um valor:')))
            break
        except ValueError:
            print('Valor Errado, Digite novamente:')
    if c == 0:
        mai = men = valores[c]
    else:
        if valores[c] > mai:
            mai = valores[c]
        if valores[c] < men:
            men = valores[c]
print('*' * 45)
print(f'O maior valor foi: {max(valores)} nas posições', end='')
for i, v in enumerate(valores):
    if v == mai:
        print(f' {i + 1}...', end='')
print()
print(f'O menor valor foi: {min(valores)} nas posições', end='')
for i, v in enumerate(valores):
    if v == men:
        print(f' {i + 1}...', end='')
print()
print('*' * 45)
