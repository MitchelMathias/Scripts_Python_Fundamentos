import lib
from uex_115.cores import *
from uex_115.numeros import *
from lib.arquivo import *


arq = 'pessoas.txt'
while True:
    if Arq(arq):
        a = lib.menu(['Cadastrar Pessoa', 'Listar Pessoa', 'Encerrar Programa'])
    else:
        criar(arq)
        a = lib.menu(['Cadastrar Pessoa', 'Listar Pessoa', 'Encerrar Programa'])
    if a == 0:
        nome = str(input('Nome:'))
        idade = leiaint('Idade:')
        print(letrasCustom('Pessoa Cadastrada com Sucesso!!', 1))
        cadastrar(arq, nome, idade)
    if a == 1:
        ler(arq)
    if a == 2:
        break
