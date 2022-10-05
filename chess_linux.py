from os import chdir
chdir('./chess')
import pygame as pg
import sys
from chess.pieces import *

# Board Setup
pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((1000,800))
pg.display.set_caption("Chess")
running = True
bgimg = pg.image.load('Chess_Board.png')
bgimg = pg.transform.scale(bgimg,(700,700))



# Pieces
whites = ('wking','wqueen','wbishop1','wbishop2','wknight1','wknight2',
          'wrook1','wrook2','wpawn1','wpawn2','wpawn3','wpawn4','wpawn5',
          'wpawn6','wpawn7','wpawn8')

blacks = ('bking','bqueen','bbishop1','bbishop2','bknight1','bknight2',
           'brook1','brook2','bpawn1','bpawn2','bpawn3','bpawn4','bpawn5',
           'bpawn6','bpawn7','bpawn8')
#White
wking = Units.King(screen,'./white/white_king.png',coords[7,4],'white')
wqueen = Units.Queen(screen,'./white/white_queen.png',coords[7,3],'white')
wbishop1 = Units.Bishop(screen,'./white/white_bishop.png',coords[7,2],'white')
wbishop2 = Units.Bishop(screen,'./white/white_bishop.png',coords[7,5],'white')
wknight1 = Units.Knight(screen,'./white/white_knight.png',coords[7,1],'white')
wknight2 = Units.Knight(screen,'./white/white_knight.png',coords[7,6],'white')
wrook1 = Units.Rook(screen,'./white/white_rook.png',coords[7,0],'white')
wrook2 = Units.Rook(screen,'./white/white_rook.png',coords[7,7],'white')

wpawn1 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,0],'white')
wpawn2 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,1],'white')
wpawn3 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,2],'white')
wpawn4 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,3],'white')
wpawn5 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,4],'white')
wpawn6 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,5],'white')
wpawn7 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,6],'white')
wpawn8 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,7],'white')

#Black
bking = Units.King(screen,'./black/black_king.png',coords[0,4],'black')
bqueen = Units.Queen(screen,'./black/black_queen.png',coords[0,3],'black')
bbishop1 = Units.Bishop(screen,'./black/black_bishop.png',coords[0,2],'black')
bbishop2 = Units.Bishop(screen,'./black/black_bishop.png',coords[0,5],'black')
bknight1 = Units.Knight(screen,'./black/black_knight.png',coords[0,1],'black')
bknight2 = Units.Knight(screen,'./black/black_knight.png',coords[0,6],'black')
brook1 = Units.Rook(screen,'./black/black_rook.png',coords[0,0],'black')
brook2 = Units.Rook(screen,'./black/black_rook.png',coords[0,7],'black')

bpawn1 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,0],'black')
bpawn2 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,1],'black')
bpawn3 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,2],'black')
bpawn4 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,3],'black')
bpawn4 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,3],'black')
bpawn5 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,4],'black')
bpawn6 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,5],'black')
bpawn7 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,6],'black')
bpawn8 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,7],'black')

turn = 'white'

while running == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running == False
            pg.quit()
            sys.exit()
            
        screen.fill((0,104,14))
        screen.blit(bgimg,(50,50))

        for unit in whites:
            exec(unit+'.Blit(screen)')
        
        for unit in blacks:
            exec(unit+'.Blit(screen)')

        if event.type == pg.MOUSEBUTTONUP and turn == 'white':
            pos = pg.mouse.get_pos
            selected_piece = [s for s in whites if eval(s+'.rect.collidepoint(event.pos)')]
            print(selected_piece)
            try:
                unit = selected_piece[0]
            except:
                pass
            
            eval(unit+f'.piece.transform.scale({unit}.piece (100,100), DestSurface = None)')

        
        elif event.type == pg.MOUSEBUTTONUP and turn == 'black':
            pos = pg.mouse.get_pos
            selected_piece = [s for s in blacks if eval(s+'.rect.collidepoint(event.pos)')]
            print(selected_piece)


    pg.event.get()
    pg.display.flip()
    pg.display.update()