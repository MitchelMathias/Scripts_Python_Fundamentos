frase = str(input('Digite uma frase:')).strip().lower()
qua = frase.count('a')
l1 = frase.find('a') + 1
l2 = frase.rfind('a') + 1
dividido = frase.split()
try:
    print(f'Ele repete a letra (a) {qua} vezes, aparece a primeira vez em {l1} e a ultima vez em {l2}')
    print(dividido[1])
except:
    print('o nome não tem 4 repartiçoes')
