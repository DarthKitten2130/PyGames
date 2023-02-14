import pygame as pg
import numpy as np
from board import squares
from pieces import *




class Piece(pg.sprite.Sprite):
    def __init__(self,screen,img,pos,faction):
        pg.sprite.Sprite.__init__(self)
        self.img = pg.image.load(img)
        self.coord = pos
        self.alive = True
        self.moved = False
        self.colour = faction
        self.rect = self.img.get_rect(topleft = pos)


    
    def Blit(self,screen):

        screen.blit(self.img,self.coord)
            

class Pawn(Piece):

    def Select(self,mouse):
        if  self.rect.collidepoint(mouse):
            if self.moved == True and self.colour == 'white':
                selected_squares = [squares[c] for c in squares.keys() if c ==coords[self.coord[0]+1,self.coord[1]]]
                print(selected_squares)
                #for c in squares.keys():
                   # if c == coords[self.coord[0]+1,self.coord[1]]:
                        



class Rook(Piece):
    pass

class Knight(Piece):
    pass

class Bishop(Piece):
    pass

class Queen(Piece):
    pass

class King(Piece):
    pass


