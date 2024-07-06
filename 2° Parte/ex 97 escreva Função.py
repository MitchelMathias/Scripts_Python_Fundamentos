def escreva(txt):
    centralizador = len(txt) * 2
    print('~'*(len(txt) * 2))
    print(f'{txt.upper():^{centralizador}}')
    print('~' * (len(txt) * 2))


escreva('Personalize sua Frase.')
while True:
    escreva(str(input('Digite sua frase:')))
    resp = str(input('Quer continuar [S/N]:'))[0]
    if resp.lower() == 'n':
        break