import sys
import pygame as pg
import platform
from os import chdir
if platform.system() == "Linux" or platform.system() == "Darwin":
    chdir('./chess')
    from chess.pieces_linux import *
elif platform.system() == "Windows":
    chdir('.\\chess')
    from chess.pieces_windows import *



# Board Setup
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((1000, 800))
pg.display.set_caption("Chess")
running = True


# Pieces
whites = ('wking', 'wqueen', 'wbishop1', 'wbishop2', 'wknight1', 'wknight2',
          'wrook1', 'wrook2', 'wpawn1', 'wpawn2', 'wpawn3', 'wpawn4', 'wpawn5',
          'wpawn6', 'wpawn7', 'wpawn8')

blacks = ('bking', 'bqueen', 'bbishop1', 'bbishop2', 'bknight1', 'bknight2',
          'brook1', 'brook2', 'bpawn1', 'bpawn2', 'bpawn3', 'bpawn4', 'bpawn5',
          'bpawn6', 'bpawn7', 'bpawn8')

squares = ( 'a1','b1','c1','d1','e1','f1','g1','h1',
            'a2','b2','c2','d2','e2','f2','g2','h2',
            'a3','b3','c3','d3','e3','f3','g3','h3',
            'a4','b4','c4','d4','e4','f4','g4','h4',
            'a5','b5','c5','d5','e5','f5','g5','h5',
            'a6','b6','c6','d6','e6','f6','g6','h6',
            'a7','b7','c7','d7','e7','f7','g7','h7',
            'a8','b8','c8','d8','e8','f8','g8','h8')

turn = 'white'

while running == True:
    # Setup
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running == False
            pg.quit()
            sys.exit()
            break

        screen.fill((0, 104, 14))
        for square in squares:
            exec(square+'.Blit(screen)')
            
        for unit in whites:
            exec(unit+'.Blit(screen)')

        for unit in blacks:
            exec(unit+'.Blit(screen)')
        
        
        # Turns

    pg.event.get()
    pg.display.flip()
    pg.display.update()
quit
