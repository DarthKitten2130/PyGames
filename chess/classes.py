import pygame as pg
import numpy as np

coords = np.array([[(65,70),(155,70),(240,70),(325,70),(410,70),(495,70),(580,70),(665,70)],
                   [(65,150),(155,150),(240,150),(325,150),(410,150),(495,150),(580,150),(665,150)],
                   [(65,240),(155,240),(240,240),(325,240),(410,240),(495,240),(580,240),(665,240)],
                   [(65,325),(155,325),(240,325),(325,325),(410,325),(495,325),(580,325),(665,325)],
                   [(65,410),(155,410),(240,410),(325,410),(410,410),(495,410),(580,410),(665,410)],
                   [(65,500),(155,500),(240,500),(325,500),(410,500),(495,500),(580,500),(665,500)],
                   [(65,580),(155,580),(240,580),(325,580),(410,580),(495,580),(580,580),(665,580)],
                   [(65,670),(155,670),(240,670),(325,670),(410,670),(495,670),(580,670),(665,670),]])

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
    
class Units:
    
    class Pawn(Piece):
        
        def move (self):
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

squares = pg.sprite.Group()

class Square(pg.sprite.Sprite):

    def __init__(self,image,coords):
        pg.sprite.Sprite.__init__(self)
        self.pos = coords
        self.color = pg.image.load(image)
        
    

    def Blit(self,scn):
        scn.blit(self.color,self.pos)

