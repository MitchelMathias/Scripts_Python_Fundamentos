def nota(x):
    obje = {'Total de notas': len(x), 'Maior nota': max(x), 'Média': sum(x) / len(x)}
    if obje['Média'] <= 5.9:
        obje['Situação'] = 'Burros'
    elif 5.9 < obje['Média'] <= 7.9:
        obje['Situação'] = 'Passados'
    else:
        obje['Situação'] = 'Gênios'
    return obje


print('='*45)
print(f'{'Média e Situação':^45}')
print('='*45)
notas = []
quant = 1
print(F'{'DIGITE "0" PARA PROSSEGUIR':^45}')
while True:
    temp = input(f'Digite a {quant}° Nota:')
    try:
        temp = float(temp)
        notas.append(temp)
        quant += + 1
    except ValueError:
        print('Digite um número real.')
    if notas and notas[-1] == 0:
        break
del notas[-1]
resultado = nota(notas)
print('='*45)
for chave, valor in resultado.items():
    print(f'{chave}: {valor}')
print('='*45)
