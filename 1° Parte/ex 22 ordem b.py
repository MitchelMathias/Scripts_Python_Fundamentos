import random

a1 = str(input('Digite o 1° aluno do sorteiro:'))
a2 = str(input('Digite o 2° aluno do sorteiro:'))
a3 = str(input('Digite o 3° aluno do sorteiro:'))
a4 = str(input('Digite o 4° aluno do sorteiro:'))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print('A ordem de apresentação do trabalho é')
print(lista)
