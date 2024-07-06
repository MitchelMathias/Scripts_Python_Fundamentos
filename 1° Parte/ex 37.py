print('\033[1;32m-=-'*13)
print('      \033[0;31m Analisador de triangulos...')
print('\033[1;32m-=-'*13)
r1 = float(input('\033[;mTamanho do 1° Seguimento?'))
r2 = float(input('Tamanho do 2° Seguimento?'))
r3 = float(input('Tamanho do 3° Seguimento?'))
if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
    print('A união desses segmentos PODEM formar um triangulo')
else:
    print('A união desses segmentos NÃO pode formar um triangulo')
