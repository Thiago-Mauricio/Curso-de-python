import pygame as pg

BLACK =  (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pg.init()

menu = pg.display.set_mode([720, 680])

while True:
    
    event = pg.event.poll()
    if event.type == pg.QUIT:
        break
    elif event.type == pg.KEYDOWN and event.key == event.K_ESCAPE:
        break

    menu.fill(BLUE)

    pg.display.update()
