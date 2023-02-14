import os
import sys
import pygame as pg
from board import *
from pieces import *

os.chdir(r'C:\\Users\\darth\\Desktop\\Python_Programs\\PyGames\\PyGames\\chess')

# Board Setup
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((1000, 800))
pg.display.set_caption("Chess")
running = True


# Pieces

white_sprites = pg.sprite.Group()
black_sprites = pg.sprite.Group()

units = (wking, wqueen, wbishop1, wbishop2, wknight1, wknight2,
          wrook1, wrook2, wpawn1, wpawn2, wpawn3, wpawn4, wpawn5,
          wpawn6, wpawn7, wpawn8,bking, bqueen, bbishop1, bbishop2, bknight1, bknight2,
          brook1, brook2, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5,
          bpawn6, bpawn7, bpawn8)

whites = (wking, wqueen, wbishop1, wbishop2, wknight1, wknight2,
          wrook1, wrook2, wpawn1, wpawn2, wpawn3, wpawn4, wpawn5,
          wpawn6, wpawn7, wpawn8)

blacks = (bking, bqueen, bbishop1, bbishop2, bknight1, bknight2,
          brook1, brook2, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5,
          bpawn6, bpawn7, bpawn8)



start_squares = ( a1,b1,c1,d1,e1,f1,g1,h1,
                  a2,b2,c2,d2,e2,f2,g2,h2,
                  a7,b7,c7,d7,e7,f7,g7,h7,
                  a8,b8,c8,d8,e8,f8,g8,h8)

for square in start_squares:
    square.Has_Piece = True

turn = 'white'

while running == True:
    # Setup
    for event in pg.event.get():

        screen.fill((0, 104, 14))
        for square in squares.values():
            square.Blit(screen)

        for unit in whites:
            unit.Blit(screen)

        for unit in blacks:
            unit.Blit(screen)
        
        if event.type == pg.MOUSEBUTTONUP and turn == 'white':
            mouse = pg.mouse.get_pos()
            bpawn1.Select(mouse)

        elif event.type == pg.QUIT:
                    running == False
                    pg.quit()
                    sys.exit()

        for unit in units:
            square.Has_Unit(unit.rect)
        # Turns
    pg.event.get()
    pg.display.flip()
    pg.display.update()