import pygame

# 1. Definir a variável encurta o caminho e deixa o código limpo
# 2. Agora o código fica legível e não "corta" a visualização
pygame.mixer.init()
pygame.mixer.music.load('assets/audio/musica.mp3')
pygame.mixer.music.play()

input("Pressione Enter para parar...")
