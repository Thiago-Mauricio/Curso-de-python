import pygame as pg
import time

#definindo cores
BLACK =  (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


pg.init()#inicia o pygame

screen = pg.display.set_mode([640, 480])#define variavel para o tamanho da tela

#carregando fonte
font = pg.game.font.SysFont(None, 55)

pg.display.set_caption('JOGO DA VELHA')#define o título da janela

while True:

    event = pg.event.pool()