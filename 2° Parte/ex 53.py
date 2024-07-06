import unidecode
frase = str(input('Digite uma frase:')).lower()
frase = unidecode.unidecode(frase)
frase_sem = ''.join(frase.split())
invertido = frase_sem[::-1]
print(f'A frase atnes: {frase_sem} fica assim: {invertido}')
if invertido == frase_sem:
    print('Portanto é uma frase palíndroma')
else:
    print('Essa frase não é palíndroma')
