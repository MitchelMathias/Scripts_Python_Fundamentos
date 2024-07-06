n = cont = soma = 0 # todos recebem 0
n = float(input('Digite um numero ou 999 pra parar:')) # Serve pra excluir o 999 da variavel soma e da varivael cont
while n != 999:
    cont = cont + 1
    soma = soma + n
    n = float(input('Digite um numero ou 999 pra parar:')) # Serve pra excluir o 999 da variavel soma e da varivael cont
print('Vc digitou {} e a soma foi {}'.format(cont, soma))
