# import unidecode

# cidade = str(input('Digite o nome de uma cidade?'))
# cidade_for = cidade.lower()
# cidadee = unidecode.unidecode(cidade_for)
# palavras = cidadee.split()
# print(palavras[0].startswith('santo'))'''

import unidecode

cid = str(input('Digite o nome de uma cidade:')).strip()
cidd = unidecode.unidecode(cid)
ciddd = cidd.upper()
print(ciddd[:5] == 'SANTO')
