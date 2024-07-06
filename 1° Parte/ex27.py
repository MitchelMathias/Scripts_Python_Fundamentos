import unidecode

nome = str(input('Digite todos nomes:')).strip()
nomee = unidecode.unidecode(nome)
print('silva' in nomee.lower())
