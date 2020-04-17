import pygame as pg
import time
BLACK = pg.Color(0, 0, 0)
WHITE = pg.Color(255, 255, 255)


pg.init()

screen = pg.display.set_mode((640, 480))

pg.display.set_caption('Simple Movement')

#Cria o Rect para o quadrado
square = pg.Rect(300, 230, 20, 20)

left_pad = pg.Rect(20, 210, 20, 60)
right_pad = pg.Rect(600, 210, 20, 60)

pads = [left_pad, right_pad]


#adicionado fps
velocity_x = 0.3

clock = pg.time.Clock()

while True:
    #chamacos o tick do relógio para 30 fps
    #e armazenamos o delta de tempo
    dt = clock.tick(30)
    
    event = pg.event.poll()

    if event.type == pg.QUIT:
        break


    #usa a função move inplace
    square.move_ip(velocity_x * dt, 0)
    
    #checa por colisão com pads
    if square.collidelist(pads) >= 0:
        velocity_x = -velocity_x

    screen.fill(BLACK)

    pg.draw.rect(screen, WHITE, square)

    for pad in pads:
        pg.draw.rect(screen, WHITE, pad)

    pg.display.flip()