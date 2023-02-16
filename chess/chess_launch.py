import os
import sys
import pygame as pg
from board import *
from pieces import *

# Sets File Directory
os.chdir(r'C:\\Users\\darth\\Desktop\\Python_Programs\\PyGames\\PyGames\\chess')

# Board Setup
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((1000, 800))
pg.display.set_caption("Chess")
pg.font.init()
running = True


# Pieces

white_sprites = pg.sprite.Group(wking, wqueen, wbishop1, wbishop2, wknight1, wknight2,
          wrook1, wrook2, wpawn1, wpawn2, wpawn3, wpawn4, wpawn5,
          wpawn6, wpawn7, wpawn8)
black_sprites = pg.sprite.Group(bking, bqueen, bbishop1, bbishop2, bknight1, bknight2,
          brook1, brook2, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5,
          bpawn6, bpawn7, bpawn8)

units = pg.sprite.Group(wking, wqueen, wbishop1, wbishop2, wknight1, wknight2,
          wrook1, wrook2, wpawn1, wpawn2, wpawn3, wpawn4, wpawn5,
          wpawn6, wpawn7, wpawn8,bking, bqueen, bbishop1, bbishop2, bknight1, bknight2,
           brook1,brook2, bpawn1, bpawn2, bpawn3, bpawn4, bpawn5,
          bpawn6, bpawn7, bpawn8)

names = {(wking,bking): "King",(wqueen,bqueen): "Queen",(wbishop1,wbishop2,bbishop1,bbishop2): "Bishop",
         (wknight1,wknight2,bknight1,bknight2): "Knight",(wrook1,wrook2,brook1,brook2): "Rook",
         (wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,
          bpawn6,bpawn7,bpawn8): "Pawn"}

start_squares = pg.sprite.Group( a1,b1,c1,d1,e1,f1,g1,h1,
                  a2,b2,c2,d2,e2,f2,g2,h2,
                  a7,b7,c7,d7,e7,f7,g7,h7,
                  a8,b8,c8,d8,e8,f8,g8,h8)

'''
location = {a1: wrook2,
a2: ,
b1: wknight2,
c1:,
d1:,
e1:,
f1:,
g1:,
h1:,
a2:,
b2:,
c2:,
d2:,
e2:,
f2:,
g2:,
h2:
}
'''

# Text and Fonts
white_rgb = (255,255,255)
black_rgb = (0,0,0)
myfont = pg.font.SysFont("Times New Roman",20)



for square in start_squares:
    square.has_piece = True

turn = 'white'

while running == True:
    # Setup
    for event in pg.event.get():

        screen.fill((0, 104, 14))

        # Renders in Board
        for square in squares.values():
            square.Blit(screen)

        # Renders in units
        for unit in units:
            unit.Blit(screen)
        
        
        
        if event.type == pg.MOUSEBUTTONUP:
             for s in units:
                 unity, y = s.check_click(event.pos,x=names)

        if event.type == pg.QUIT:
                    running == False
                    pg.quit()
                    sys.exit()
        
        try:
            label = myfont.render(y,1,white_rgb)
            screen.blit(label,(800,100))
        except:
            pass

        for unit in units:
            square.Has_Unit(unit.rect)
        # Turns
    pg.event.get()
    pg.display.flip()
    pg.display.update()