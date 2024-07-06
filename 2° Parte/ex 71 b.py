import time
print('=' * 45)
print(f'{'Banco Ladrão':^45}')
time.sleep(1)
print(f'{'Porrada Solução!':^45}')
time.sleep(1)
print(f'{'Agiota passa vergonha':^45}')
time.sleep(1)
print('=' * 45)
saque = int(input('Qual valor do saque: R$'))
total = saque
ced = 200
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            time.sleep(1)
            print(f'total de {totced} de R$ {ced}')
        if ced == 200:
            ced = 100
        elif ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 45)
time.sleep(1)
print(f'{'Volte sempre!!!':^45}')
time.sleep(1)
print(f'{'Ou não, tu que sabe':^45}')
time.sleep(1)
print(f'{'banco é tudo ladrão':^45}')
time.sleep(1)
print(f'{'  Pergunta pro Alex... Deve R$ 250 Mil Reais':^45}')
time.sleep(1)
