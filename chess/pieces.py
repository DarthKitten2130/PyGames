import pygame as pg


class Piece:
    def __init__(self,img,pos):
        self.piece = pg.image.load(img)
        self.x = pos[0]
        self.y = pos[1]
        self.alive = True
    
    def Blit(self,screen):

        screen.blit(self.piece,(self.x,self.y))

    
class Units:
    
    class Pawn(Piece):
        def __init__(self, img, pos):
            super().__init__(img, pos)
            self.first_move = False

    class Rook(Piece):
        def __init__(self, img, pos):
            super().__init__(img, pos)
            self.first_move = False

    
    class Knight(Piece):
        pass
    
    class Bishop(Piece):
        pass
    
    class Queen(Piece):
        pass
    
    class King(Piece):
        def __init__(self, img, pos):
            super().__init__(img, pos)
            self.first_move = False

