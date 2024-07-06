import pygame
import os
import unidecode

pasta = r'C:\Users\Mathias\Desktop\Musica'
nome = str(input('Qual o nome da musica?'))
esse = unidecode.unidecode(nome.lower()) + '.mp3'
pastas = os.path.join(pasta, esse)

if os.path.join(pasta, esse):
    pygame.init()
    pygame.mixer.init()

    try:
        pygame.mixer.music.load(esse)
        pygame.mixer.music.play()
        input("Pressione Enter para encerrar.")
        pygame.event.wait()
    except pygame.error as e:
        print(f'Ocorreu um erro de busca {e}.')

else:
    print(f'O arquivo chamado {nome}, não foi encontrado')
