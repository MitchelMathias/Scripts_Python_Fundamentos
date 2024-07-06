import random

print('qual sera o primeiro aluno a apresentar o trabalho?')
a1 = str(input('1° Aluno?'))
a2 = str(input('2° Aluno?'))
a3 = str(input('3° Aluno?'))
a4 = str(input('4° Aluno?'))
als = (a1, a2, a3, a4)
ordem = random.sample(als, len(als))
print('Ordem de Apresentação dos alunos conforme relação abaixo')
print('1° Aluno {}.'.format(ordem[0]))
print('2° Aluno {}.'.format(ordem[1]))
print('3° Aluno {}.'.format(ordem[2]))
print('4° Aluno {}.'.format(ordem[3]))
