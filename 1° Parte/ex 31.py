vel = float(input('Qual a velocidade que o veiculo estava?'))
if vel >= 80:
    print('Voce foi Multado')
    multa = vel * 7 - 560  # ou multa = (vel - 80) * 7
    print(f'R${multa}, esse é o valor em reais da sua multa')
else:
    print('Prossiga tranquilamente')
