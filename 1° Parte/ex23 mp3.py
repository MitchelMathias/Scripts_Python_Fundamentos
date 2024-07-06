from pytube import YouTube
import os
import time
import webbrowser


def baixar(link):
    try:
        yt = YouTube(link)
        audio = yt.streams.filter(only_audio=True).first()
        print(f'Baixando {yt.title}')
        audio.download()
        print('Vou executa-lo')
        time.sleep(2)
        reproduzir(audio.default_filename)

    except Exception as e:
        print('Ocorreu um Erro inesperado:{e}')


def reproduzir(nome_arquivo):
    try:
        webbrowser.open(os.path.abspath(nome_arquivo))
    except Exception as e:
        print(f'Ocorreu um erro ao reproduzir a musica: {e}')


link_video = input("Digite o link do vídeo que deseja baixar a música: ")
baixar(link_video)
