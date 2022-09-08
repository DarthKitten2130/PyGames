import pygame as pg
import numpy as np
from os import chdir
from pieces import Units


# Board Setup
pg.init()
chdir('.\\chess')
screen = pg.display.set_mode((1000,800))
pg.display.set_caption("Chess")
running = True
bgimg = pg.image.load('Chess_Board.png')
bgimg = pg.transform.scale(bgimg,(700,700))

coords = np.array([[(70,70),(155,70),(240,70),(325,70),(410,70),(495,70),(580,70),(665,70)],
                   [],
                   [],
                   [],
                   [],
                   [],
                   [],
                   []])

# Pieces
wpawn1 = Units.Pawn('.\\white\\white_pawn.png',(70,70))
wpawn2 = Units.Pawn('.\\white\\white_pawn.png',(155,70))
wpawn3 = Units.Pawn('.\\white\\white_pawn.png',(240,70))
wpawn4 = Units.Pawn('.\\white\\white_pawn.png',(325,70))
wpawn5 = Units.Pawn('.\\white\\white_pawn.png',(410,70))
wpawn6 = Units.Pawn('.\\white\\white_pawn.png',(495,70))
wpawn7 = Units.Pawn('.\\white\\white_pawn.png',(580,70))
wpawn8 = Units.Pawn('.\\white\\white_pawn.png',(665,70))

while running == True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running == False
            
    screen.fill((0,104,14))
    screen.blit(bgimg,(50,50))
    wpawn1.Blit(screen)
    wpawn2.Blit(screen)
    wpawn3.Blit(screen)
    wpawn4.Blit(screen)
    wpawn5.Blit(screen)
    wpawn6.Blit(screen)
    wpawn7.Blit(screen)
    wpawn8.Blit(screen)

    pg.event.get()
    pg.display.flip()
    pg.display.update()