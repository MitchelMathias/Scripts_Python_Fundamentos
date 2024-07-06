valores = []
for c in range(0, 5):
    while True:
        try:
            entrada = input('Digite um valor:')
            if entrada.isdigit():
                entrada1 = int(entrada)
                if c == 0:
                    valores.append(entrada1)
                elif entrada1 > valores[-1]:
                    valores.append(entrada1)
                else:
                    pos = 0
                    while pos < len(valores):
                        if entrada1 <= valores[pos]:
                            valores.insert(pos, entrada1)
                            break
                        pos += 1
                break
            else:
                print('Valor invalido digite novamente!!')
        except ValueError:
            print('valor invalido')
print(f'A ordem é: {valores}')
