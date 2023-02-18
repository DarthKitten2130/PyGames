import pygame as pg
from board import squares
from pieces import *

troop,name,rgb = ' ',' ',' '

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
    
    
    def Check_Click(self,mouse,x):
        global troop,name
        if self.rect.collidepoint(mouse):
            print("mew")
            troop = self
            for lst in x:
                for unit in lst:
                    if unit is self:
                        name = x[lst]
            if self.colour == 'white':
                rgb = (255,255,255)
            elif self.colour == 'black':
                rgb = (0,0,0)
        return troop,name,rgb
            

class Pawn(Piece):

    def Select(self,mouse):
        if  self.rect.collidepoint(mouse):
            print("Hi")
            '''if self.moved == True and self.colour == 'white':
                selected_squares = [squares[c] for c in squares.keys() if c ==coords[self.coord[0]+1,self.coord[1]]]
                print(selected_squares)
                #for c in squares.keys():
                   # if c == coords[self.coord[0]+1,self.coord[1]]:
                    '''    



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


