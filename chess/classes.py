import pygame as pg
import numpy as np

coords = np.array([[(60,60),(145,60),(225,60),(310,60),(390,60),(470,60),(550,60),(630,60)],
                   [(60,145),(145,145),(225,145),(310,145),(390,145),(470,145),(550,145),(630,145)],
                   [(60,225),(145,225),(225,225),(310,225),(390,225),(470,225),(550,225),(630,225)],
                   [(60,310),(145,310),(225,310),(310,310),(390,310),(470,310),(550,310),(630,310)],
                   [(60,390),(145,390),(225,390),(310,390),(390,390),(470,390),(550,390),(630,390)],
                   [(60,470),(145,470),(225,470),(310,470),(390,470),(470,470),(550,470),(630,470)],
                   [(60,550),(145,550),(225,550),(310,550),(390,550),(470,550),(550,550),(630,550)],
                   [(60,630),(145,630),(225,630),(310,630),(390,630),(470,630),(550,630),(630,630),]])

class Piece(pg.sprite.Sprite):
    def __init__(self,screen,img,pos,faction):
        pg.sprite.Sprite.__init__(self)
        self.img = pg.image.load(img)
        self.coord = pos
        self.alive = True
        self.moved = False
        self.colour = faction
        self.rect = self.img.get_rect()


    
    def Blit(self,screen):

        screen.blit(self.img,self.coord)
    

class Pawn(Piece):

    def move(self):
        pass

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


class Square(pg.sprite.Sprite):

    def __init__(self,image,coords):
        pg.sprite.Sprite.__init__(self)
        self.pos = coords
        self.color = pg.image.load(image)
        self.has_piece = False
        
    

    def Blit(self,scn):
        scn.blit(self.color,self.pos)

