from Pacot import numeros, cores

cores.titulo('Programa Fatorial', 14)
n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é {numeros.fatorial(n)}')
cores.titulo('Agora o Dobro', 14)
print(f'O dobro de {n} é {numeros.dobro(n)}')
cores.titulo('Agora o Triplo', 14)
print(f'O triplo de {n} é {numeros.triplo(n)}')