print('Click no Enter com a expressão vazia para encerrar.')
while True:
    expre = str(input('Digite sua expressão:'))
    lista = []
    if expre == '':
        break
    for simb in expre:
        if simb == '(':
            lista.append('(')
        elif simb == ')':
            if len(lista) > 0:
                lista.pop()
            else:
                lista.append(')')
                break
    if len(lista) == 0:
        print('Sua expressão é válida')
    else:
        print('Sua expressão é inválida')
