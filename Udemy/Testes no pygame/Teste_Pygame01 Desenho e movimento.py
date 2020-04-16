import time
import pygame


#definindo cores
BLACK =  (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()#inicia o pygame

screen = pygame.display.set_mode([640, 480])#define variavel para o tamanho da tela

#carregando fonte
font = pygame.font.SysFont(None, 55)

pygame.display.set_caption('JOGO DA VELHA')#define o título da janela

#variaves da bola:
position_x = 300
position_y = 200
velocity_x = 1
velocity_y = 1

#iniciando loop do jogo:
while True:
    #Processamento de entrada
    
    
    #capturando eventos
    event = pygame.event.poll()
    
    #caso evento QUIT(clicar no x da janela) seja disparado
    if event.type == pygame.QUIT:
        break
    
    #Atualização do jogo

    #movendo a bola

    position_x += velocity_x
    position_y += velocity_y

    #mudando direção no eixo x nas bordas
    if position_x > 600:
        velocity_x = -1
    elif position_x < 1:
        velocity_x = 1

    #mudando a direção no eixo y nas bordas
    if position_y > 440:
        velocity_y = -1
    elif position_y < 1:
        velocity_y = 1
    
    screen.fill(BLACK)#define cor da janela no estilo RGB
    
    #desenho das linhas na tela
    pygame.draw.line(screen, WHITE, [213, 20], [213, 460], 3)
    pygame.draw.line(screen, WHITE, [427, 20], [427, 460], 3)
    pygame.draw.line(screen, WHITE, [20, 160], [620, 160], 3)
    pygame.draw.line(screen, WHITE, [20, 320], [620, 320], 3)
    pygame.draw.ellipse(screen, RED, [position_x, position_y, 40, 40]) #desenha um circulo na tela.

    # difinindo o texto
    text = font.render('pygame', True, WHITE)

    # copiando texto para superficie
    screen.blit(text, [250, 200])

    #atualizan a tela
    pygame.display.flip()

    