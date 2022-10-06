from os import chdir
chdir('./chess')
import pygame as pg
import sys
from chess.pieces import *

# Board Setup
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((1000,775))
pg.display.set_caption("Chess")
running = True

#Board

# Pieces
whites = ('wking','wqueen','wbishop1','wbishop2','wknight1','wknight2',
          'wrook1','wrook2','wpawn1','wpawn2','wpawn3','wpawn4','wpawn5',
          'wpawn6','wpawn7','wpawn8')

blacks = ('bking','bqueen','bbishop1','bbishop2','bknight1','bknight2',
           'brook1','brook2','bpawn1','bpawn2','bpawn3','bpawn4','bpawn5',
           'bpawn6','bpawn7','bpawn8')

turn = 'white'

while running == True:
    #Setup
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running == False
            pg.quit()
            sys.exit()
            quit
            
        screen.fill((0,104,14))
        a8.Blit(screen)
        b8.Blit(screen)

        for unit in whites:
            exec(unit+'.Blit(screen)')
        
        for unit in blacks:
            exec(unit+'.Blit(screen)')
        #Turns


    pg.event.get()
    pg.display.flip()
    pg.display.update()