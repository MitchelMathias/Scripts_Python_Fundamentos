def lin():
    print('=-='*15)


def area(list):
    ar = list[0] * list[1]
    print(f'A área do terreno {list[0]} x {list[1]} é {ar}m²')


lin()
print(f'{'Calculando a area do terreno':^40}')
lin()
while True:
    d1 = [float(input('Digite o Comprimento:')), float(input('Digite a Altura:'))]
    area(d1)
    lin()
    resp = str(input('Quer Continuar?[S/N]'))
    lin()
    if resp == 'N':
        break
