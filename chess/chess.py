import pygame as pg
from os import chdir

pg.init()
chdir('.\\chess')
screen = pg.display.set_mode((1000,800))
win = False
bgimg = pg.image.load('Chess_Board.png')
bgimg = pg.transform.scale(bgimg,(700,700))


while win == False:
    pg.event.get()
    screen.fill((0,104,14))
    screen.blit(bgimg,(50,50))
    pg.display.flip()