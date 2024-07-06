tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 4:
    print('Seu carro é uma nave, bem novinho?')
    r = str(input('Vc ta pensando em trocar?'))
    if r.lower() == 'sim':
        print('Não vejo necessidade seu carro é novo meu amigo')
    else:
        print('Eu concordo com vc, não tem necessidade.')
else:
    print('seu carro esta ficando velho')
    rr = str(input('Vc ta pensando em trocar?'))
    if rr.lower() == 'sim':
        print('realmente devemos pensar sobre isso')
    else:
        print('Eu sugiro pensar melhor, seu carro esta velho')
print('__fim__')
