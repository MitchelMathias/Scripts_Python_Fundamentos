palavras = ('MERCADO', 'QUEIJO', 'SERVIÇO', 'HORA', 'CHIMARRAO', 'RADIO')
for p in palavras:
    cont = 0
    print(f'Na palavra {p.upper()} temos. ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end='-')
            cont = cont + 1
    print(f'\ntotal de {cont} vogais.')
