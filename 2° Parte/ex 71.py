print('=' * 45)
print(f'{'O Banco ladrão do Mitchel':^45}')
print('=' * 45)
saque = int(input('Quanto vc quer sacar: R$'))
print('=' * 45)
total = saque
ced = 100
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'total de {totalced} cedulas de R$ {ced}')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('=' * 45)
print('Volte sempre!!!')
