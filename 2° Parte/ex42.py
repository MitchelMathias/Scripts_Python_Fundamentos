print('-=-'*13)
print('      Analisador de triangulos...')
print('-=-'*13)
r1 = float(input('Tamanho do 1° Seguimento?'))
r2 = float(input('Tamanho do 2° Seguimento?'))
r3 = float(input('Tamanho do 3° Seguimento?'))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('A união desses segmentos PODEM formar um triangulo')
    if r1 == r2 and r2 == r3:
        print('O triangulo formado é um triangulo Equilátero')
    elif r1 != r2 and r2 != r3 and r3 != r1:
        print('O triangulo formado é um triangulo Escaleno')
    else:
        print('O triangulo formado é um triangulo Isósceles')
else:
    print('A união desses segmentos NÃO pode formar um triangulo')
