print('****** PA ******')
primeiro = int(input('1° Termo:'))
razão = int(input('Razão:'))
termo = primeiro
contador = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while contador <= total:
        termo = termo + razão
        contador = contador + 1
        print(f' {termo} - ', end='')
    print('Pausa', end='')
    mais = int(input('\nQuantos numeros a mais (pressione 0 para sair): '))
