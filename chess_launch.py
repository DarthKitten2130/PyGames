import os
import sys
import pygame as pg
import platform
from os import chdir
#from chess.pieces_windows import *
print(os.getcwd())


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

squares = {coords[7,	7]:	a1,
           coords[6,	7]:	b1,
           coords[5,	7]:	c1,
           coords[4,	7]:	d1,
           coords[3,	7]:	e1,
           coords[2,	7]:	f1,
           coords[1,	7]:	g1,
           coords[0,	7]:	h1,
           coords[7,	6]:	a2,
           coords[6,	6]:	b2,
           coords[5,	6]:	c2,
           coords[4,	6]:	d2,
           coords[3,	6]:	e2,
           coords[2,	6]:	f2,
           coords[1,	6]:	g2,
           coords[0,	6]:	h2,
           coords[7,	5]:	a3,
           coords[6,	5]:	b3,
           coords[5,	5]:	c3,
           coords[4,	5]:	d3,
           coords[3,	5]:	e3,
           coords[2,	5]:	f3,
           coords[1,	5]:	g3,
           coords[0,	5]:	h3,
           coords[7,	4]:	a4,
           coords[6,	4]:	b4,
           coords[5,	4]:	c4,
           coords[4,	4]:	d4,
           coords[3,	4]:	e4,
           coords[2,	4]:	f4,
           coords[1,	4]:	g4,
           coords[0,	4]:	h4,
           coords[7,	3]:	a5,
           coords[6,	3]:	b5,
           coords[5,	3]:	c5,
           coords[4,	3]:	d5,
           coords[3,	3]:	e5,
           coords[2,	3]:	f5,
           coords[1,	3]:	g5,
           coords[0,	3]:	h5,
           coords[7,	2]:	a6,
           coords[6,	2]:	b6,
           coords[5,	2]:	c6,
           coords[4,	2]:	d6,
           coords[3,	2]:	e6,
           coords[2,	2]:	f6,
           coords[1,	2]:	g6,
           coords[0,	2]:	h6,
           coords[7,	1]:	a7,
           coords[6,	1]:	b7,
           coords[5,	1]:	c7,
           coords[4,	1]:	d7,
           coords[3,	1]:	e7,
           coords[2,	1]:	f7,
           coords[1,	1]:	g7,
           coords[0,	1]:	h7,
           coords[7,	0]:	a8,
           coords[6,	0]:	b8,
           coords[5,	0]:	c8,
           coords[4,	0]:	d8,
           coords[3,	0]:	e8,
           coords[2,	0]:	f8,
           coords[1,	0]:	g8,
           coords[0,	0]:	h8
}

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
        for square in squares.keys():
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
                    break

        for unit in units:
            square.Has_Unit(unit.rect)
        # Turns
    pg.event.get()
    pg.display.flip()
    pg.display.update()
quit
