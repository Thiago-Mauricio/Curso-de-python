import time
import pygame
#definindo cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


pygame.init()#inicia o pygame
screen = pygame.display.set_mode([640, 480])#define variavel para o tamanho da tela
pygame.display.set_caption('JOGO DA VELHA')#define o título da janela
screen.fill([0, 0, 0])#define cor da janela no estilo RGB

pygame.draw.line(screen, WHITE, [213, 20], [213, 460], 3)
pygame.draw.line(screen, WHITE, [427, 20], [427, 460], 3)
pygame.draw.line(screen, WHITE, [20, 160], [620, 160], 3)
#pygame.draw.line(screen, WHITE, [180, 40], [180, 440], 3)





pygame.display.flip()#atualiza a tela

time.sleep(5)