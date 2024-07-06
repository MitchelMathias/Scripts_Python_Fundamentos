import unidecode
frase = str(input('Digite uma frase:')).lower()
frase = unidecode.unidecode(frase)
frase_sem = ''.join(frase.split())
inverso = ''
for c in range(len(frase_sem) - 1, -1, -1):
    inverso += frase_sem[c]
print(f'A frase antes: {frase_sem} fica assim: {inverso}')
if inverso == frase_sem:
    print('Portanto é uma frase palíndroma')
else:
    print('Essa frase não é palíndroma')
