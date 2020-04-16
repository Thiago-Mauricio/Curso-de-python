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

#carregando fonte
font = pygame.font.SysFont(None, 55)

pygame.display.set_caption('JOGO DA VELHA')#define o título da janela
screen.fill(BLACK)#define cor da janela no estilo RGB

#desenho das linhas na tela
pygame.draw.line(screen, WHITE, [213, 20], [213, 460], 3)
pygame.draw.line(screen, WHITE, [427, 20], [427, 460], 3)
pygame.draw.line(screen, WHITE, [20, 160], [620, 160], 3)
pygame.draw.line(screen, WHITE, [20, 320], [620, 320], 3)

#pygame.draw.rect(screen, BLUE, [300, 30, 20, 20]) desenha uma quadrado na tela [poshor, posver, TamL, TamA]
pygame.draw.ellipse(screen, RED, [200, 200, 40, 40]) #desenha um circulo na tela.
#pygame.draw.polygon(screen, RED, [[400, 240], [440, 240], [400, 200]]) desenha um triangulo na tela

pygame.display.flip()#atualiza a tela

time.sleep(5)

# difinindo o texto
text = font.render('pygame', True, WHITE)

# copiando texto para superficie
screen.blit(text, [250, 200])

#atualizan a tela
pygame.display.flip()

time.sleep(5)