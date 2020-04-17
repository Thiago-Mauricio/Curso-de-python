import pygame as pg
import time

#definindo cores
BLACK =  (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

square1 = pg.Rect(40, 100, 210, 155)
square2 = pg.Rect(255, 100, 210, 155)
square3 = pg.Rect(470, 100, 210, 155)
square4 = pg.Rect(40, 260, 210, 155)
square5 = pg.Rect(255, 260, 210, 155)
square6 = pg.Rect(470, 260, 210, 155)
square7 = pg.Rect(40, 420, 210, 155)
square8 = pg.Rect(255, 420, 210, 155)
square9 = pg.Rect(470, 420, 210, 155)

pg.init()#inicia o pygame

screen = pg.display.set_mode([720, 680])#define variavel para o tamanho da tela
#carregando fonte
font = pg.font.SysFont(None, 55)

pg.display.set_caption('JOGO DA VELHA')#define o título da janela

while True:

    event = pg.event.poll()

    if event.type == pg.QUIT:
        break
    elif event.type == pg.KEYDOWN and event.key == event.K_ESCAPE:
        break
    
    screen.fill(BLACK)

    pg.draw.rect(screen, WHITE, square1)
    pg.draw.rect(screen, WHITE, square2)
    pg.draw.rect(screen, WHITE, square3)
    pg.draw.rect(screen, WHITE, square4)
    pg.draw.rect(screen, WHITE, square5)
    pg.draw.rect(screen, WHITE, square6)
    pg.draw.rect(screen, WHITE, square7)
    pg.draw.rect(screen, WHITE, square8)
    pg.draw.rect(screen, WHITE, square9)

    

    
    pg.display.update()