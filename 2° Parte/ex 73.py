classificacao = (
    '1° lugar Palmeiras', '2° lugar Grêmio', '3° lugar Atlético-MG', '4° lugar Flamengo',
    '5° lugar Botafogo', '6° lugar Bragantino', '7° lugar Fluminense', '8° lugar Athletico-PR',
    '9° lugar Internacional', '10° lugar Fortaleza', '11° lugar São Paulo', '12° lugar Cuiabá',
    '13° lugar Corinthians', '14° lugar Cruzeiro', '15° lugar Vasco', '16° lugar Bahia',
    '17° lugar Santos', '18° lugar Goiás', '19° lugar Coritiba', '20° lugar América-MG')
while True:
    print('=-=' * 50)
    resp = int(input('Escolha uma das opções:\n'
                     '[1] os 5 primeiros colocados\n'
                     '[2] os ultimos 4 colocados\n'
                     '[3] ordem alfabética\n'
                     '[4] a posição do Grêmio\n'
                     '[5] encerre o programa\n'
                     'digite sua escolha:'))
    if resp == 5:
        break
    if resp > 5 or resp < 1:
        print('opção invalida')
    if resp == 1:
        print(classificacao[:5])
    if resp == 2:
        print(classificacao[16:20])
    if resp == 3:
        nome_times = [time.split(' ')[-1] for time in
                      classificacao]  # nome_times é uma varival que recebe o time da varivel da classificação o cmd
        # responsavel por recolher a informação time é a fusão do .split com o -1 que recolhe o ultimo termo da
        # varivel time dentro de classificação e o for time in classificação serve pra repetir em todos times
        print(sorted(nome_times))  # serve pra colocar em ordem alfabética
    if resp == 4:
        print(f' O Grêmio esta na {classificacao.index("2° lugar Grêmio")+1}° Posição')
