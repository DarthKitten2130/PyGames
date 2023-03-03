import os
import sys
from pathlib import Path
import pygame as pg
from board import *
from pieces import *

# Sets File Directory
mod_path = Path(__file__).parent
os.chdir(mod_path)

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
squares_list = pg.sprite.Group(squares.keys())
names = {(wking,bking): "King",(wqueen,bqueen): "Queen",(wbishop1,wbishop2,bbishop1,bbishop2): "Bishop",
         (wknight1,wknight2,bknight1,bknight2): "Knight",(wrook1,wrook2,brook1,brook2): "Rook",
         (wpawn1,wpawn2,wpawn3,wpawn4,wpawn5,wpawn6,wpawn7,wpawn8,bpawn1,bpawn2,bpawn3,bpawn4,bpawn5,
          bpawn6,bpawn7,bpawn8): "Pawn"}

# Text and Fonts
white_rgb = (255,255,255)
black_rgb = (0,0,0)
myfont = pg.font.SysFont("Times New Roman",30,bold=True)



for square in pg.sprite.Group( a1,b1,c1,d1,e1,f1,g1,h1,
                  a2,b2,c2,d2,e2,f2,g2,h2,
                  a7,b7,c7,d7,e7,f7,g7,h7,
                  a8,b8,c8,d8,e8,f8,g8,h8):
    square.has_piece = True

turn = 'white'
label = ''

def Play():
    global turn,label
    if event.type == pg.MOUSEBUTTONDOWN:
            for s in units:
                unit, y, color = s.Check_Click(event.pos,x=names)

        
            for q in squares_list:
                    sq = q.Check_Click_Square(event.pos)
            
            occupied = getattr(sq,'has_piece')
            if occupied == False:
                new_pos = squares[sq]
                print(new_pos)
                
                # Moves Unit  
                setattr(unit,'coord',new_pos)

    
    
    try:
        print(sq.has_piece)
    except:
         pass
    # Creates Name
    try:
        label = myfont.render(y,1,color)
    except NameError:
        pass
    return label

while running == True:
    # Setup
    for event in pg.event.get():

        # BG Colour
        screen.fill((0, 104, 14))

        # Game
        label1 = Play()
        turn = 'black'
        for square in squares_list:
            for unit in units:
                square.Has_Unit(unit.rect)
        label1 = Play()
        turn = 'white'
        '''Checks whether each square has a piece on it by 
       cross-referencing the piece rects with the Square Rects'''
        for square in squares_list:
                for unit in units:
                    square.Has_Unit(unit.rect)
        # Renders in board
        for square in squares.keys():
            square.Blit(screen)

        # Renders in units
        for unit in units:
            unit.Blit(screen)
        
        # Exit Sequence
        if event.type == pg.QUIT:
                    running == False
                    pg.quit()
                    sys.exit()
        
        # Piece Labelling System
        try:
            screen.blit(label1,(336.125,740))
        except:
             pass
        
        
    pg.event.get()
    pg.display.flip()
    pg.display.update()