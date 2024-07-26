nome = str(input('Qual seu nome?')).lower().strip()
if nome == 'mitchel':
    print('bem vindo de volta meu criador!')
    print('vc é tão lindo e inteligente')
elif nome == 'mathias':  # junção de if e else
    print('Tambm adoro esse nome meu amor')
    print('Voce é lindo')
elif nome == 'rodrigues':  # if + else, pode ter infinitos sinão
    print('não gosto desse nome amorzinho')
# elif nome == 'welber' or nome == 'italo' or nome == 'giordani':
elif nome in 'welber italo giordani':
    print('Se vc mecher no computador do meu criador eu vou contar')
else:
    print('só cumpro ordens do meu mestre e criador sai daqui')
