import datetime


def voto(n):
    res = datetime.date.today().year - n
    if 16 <= res <= 17:
        return f'Com {res} anos: O Voto é Opcional'
    elif res <= 15:
        return f'Com {res} anos: Você ainda não pode Votar'
    elif 18 <= res <= 65:
        return f'Com {res} anos: O Voto é Obrigatório'
    else:
        return f'Aida ta vivo? Tu escolhe se quer ir. '


print('=' * 55)
print(f'{'Votação':^55}')
print('=' * 55)
while True:
    num = int(input('Que ano você Nasceu:'))
    voto(num)
    enc = str(input('Você quer continuar:[S/N] ')).lower()[0]
    print('=' * 55)
    if enc in 'n':
        print('Agora vou Torar...')
        break
