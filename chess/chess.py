import pygame as pg
from pieces import Units
from pieces import coords
#from os import chdir


# Board Setup
pg.init()
#chdir('.\\chess')
screen = pg.display.set_mode((1000,800))
pg.display.set_caption("Chess")
running = True
bgimg = pg.image.load('Chess_Board.png')
bgimg = pg.transform.scale(bgimg,(700,700))



# Pieces

#White
wking = Units.King('.\\white\\white_king.png',coords[7,4])
wqueen = Units.Queen('.\\white\\white_queen.png',coords[7,3])
wbishop1 = Units.Bishop('.\\white\\white_bishop.png',coords[7,2])
wbishop2 = Units.Bishop('.\\white\\white_bishop.png',coords[7,5])
wknight1 = Units.Knight('.\\white\\white_knight.png',coords[7,1])
wknight2 = Units.Knight('.\\white\\white_knight.png',coords[7,6])
wrook1 = Units.Rook('.\\white\\white_rook.png',coords[7,0])
wrook2 = Units.Rook('.\\white\\white_rook.png',coords[7,7])

wpawn1 = Units.Pawn('.\\white\\white_pawn.png',coords[6,0])
wpawn2 = Units.Pawn('.\\white\\white_pawn.png',coords[6,1])
wpawn3 = Units.Pawn('.\\white\\white_pawn.png',coords[6,2])
wpawn4 = Units.Pawn('.\\white\\white_pawn.png',coords[6,3])
wpawn5 = Units.Pawn('.\\white\\white_pawn.png',coords[6,4])
wpawn6 = Units.Pawn('.\\white\\white_pawn.png',coords[6,5])
wpawn7 = Units.Pawn('.\\white\\white_pawn.png',coords[6,6])
wpawn8 = Units.Pawn('.\\white\\white_pawn.png',coords[6,7])

#Black
bking = Units.King('.\\black\\black_king.png',coords[0,4])
bqueen = Units.Queen('.\\black\\black_queen.png',coords[0,3])
bbishop1 = Units.Bishop('.\\black\\black_bishop.png',coords[0,2])
bbishop2 = Units.Bishop('.\\black\\black_bishop.png',coords[0,5])
bknight1 = Units.Knight('.\\black\\black_knight.png',coords[0,1])


while running == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running == False
            
    screen.fill((0,104,14))
    screen.blit(bgimg,(50,50))


    wking.Blit(screen)
    wqueen.Blit(screen)
    wbishop1.Blit(screen)
    wbishop2.Blit(screen)
    wknight1.Blit(screen)
    wknight2.Blit(screen)
    wrook1.Blit(screen)
    wrook2.Blit(screen)

    wpawn1.Blit(screen)
    wpawn2.Blit(screen)
    wpawn3.Blit(screen)
    wpawn4.Blit(screen)
    wpawn5.Blit(screen)
    wpawn6.Blit(screen)
    wpawn7.Blit(screen)
    wpawn8.Blit(screen)

    bking.Blit(screen)
    bqueen.Blit(screen)

    pg.event.get()
    pg.display.flip()
    pg.display.update()