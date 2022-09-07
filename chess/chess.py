import pygame as pg
from os import chdir

pg.init()

screen = pg.display.set_mode((800,800))
win = False
bgimg = pg.image.load('Chess_Board.png')
bgimg = pg.transform.scale(bgimg,(800,800))


while win == False:
    pg.event.get()
    screen.blit(bgimg,(0,0))
    pg.display.flip()