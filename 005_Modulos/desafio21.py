#Faça um arquivo que abra e reproduza o áudio de um arquivo MP3. 

import pygame 

pygame.init()

pygame.mixer.music.load('baby get on your knees') #colocar o nome do arquivo mp3
pygame.mixer.music.play()
pygame.event.wait()