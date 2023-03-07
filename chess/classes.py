import pygame as pg
from board import squares


troop,name,rgb = ' ',' ',' '

class Piece(pg.sprite.Sprite):
    def __init__(self,space,img,faction):
        pg.sprite.Sprite.__init__(self)
        self.img = pg.image.load(img)
        self.alive = True
        self.moved = False
        self.colour = faction
        self.space = space
        self.rect = self.img.get_rect(topleft = squares[self.space])

    
    def Blit(self,screen):

        screen.blit(self.img,squares[self.space])
    
    
    def Check_Click(self,mouse,x):
        global troop,name,rgb
        if self.rect.collidepoint(mouse):
            print("mew")
            troop = self
            for lst in x:
                if self in lst:
                    name = x[lst]
            if self.colour == 'white':
                rgb = (255,255,255)
            elif self.colour == 'black':
                rgb = (0,0,0)
        return troop,name,rgb
            

class Pawn(Piece):

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


