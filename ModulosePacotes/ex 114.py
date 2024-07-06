import requests
from Pacot import cores


def possibilidade(url):
    try:
        conexao = requests.get(url)
        resposta = conexao.status_code
        if resposta == 200:
            print('O site esta Acessível')
        else:
            print('O sit não esta Acessível')
    except Exception as e:
        print('Ocorreu um Erro')
        x = input('Gostaria de ver Qual o Erro?')
        if x.strip().lower()[0] in 's':
            print(e)


cores.titulo('Verificador de sit', 8)

url = input('Digite o Sit: https://').strip()
if url[0:8] in 'https://':
    possibilidade(url)
else:
    url1 = 'https://' + url
    possibilidade(url1)
