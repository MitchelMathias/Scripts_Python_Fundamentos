lanche = 'hamburguer', 'Suco', 'Pizza', 'Pudim'
x = int(input('Numero:'))
if x == 0:
    print(lanche[0])
if x == 1:
    print(lanche[1])
if x == 2:
    print(lanche[2])
if x == 3:
    print(lanche[3])
if x == 4:
    for comida in lanche:
        print(f'Vou comer {comida}')
