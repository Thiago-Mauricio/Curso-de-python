from typing import List

import pygame
#iniciando o mixer do pygame
pygame.mixer.init()
#iniciando o pygame
pygame.init()
pygame.mixer.music.load('ex21.mp3')
pygame.mixer.music.play()
pygame.event.wait()
