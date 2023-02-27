import pygame as pg
import os

# Changes the Directory of the file
os.chdir(r'C:\\Users\\darth\\Desktop\\Python_Programs\\PyGames\\PyGames\\chess')

# class for the board Squares

poly = ' '
class Square(pg.sprite.Sprite):

    def __init__(self,image,coords):
        pg.sprite.Sprite.__init__(self)
        self.pos = coords
        self.color = pg.image.load(image)
        self.has_piece = False
        self.rect = self.color.get_rect(topleft = coords)
        
    

    def Blit(self,scn):
        scn.blit(self.color,self.pos)


    def Has_Unit(self,piece):
        if self.rect.colliderect(piece):
            self.has_piece = True
    
    
    
    def Check_Click_Square(self,mouse):
        global poly

        if self.rect.collidepoint(mouse):
            print("HIT")
            poly = self
        return poly


# Squares
white = '.\\squares\\white.png'
olive = '.\\squares\\olive.png'


a8 = Square(white, (50, 50))
b8 = Square(olive, (131.75, 50))
c8 = Square(white, (213.5, 50))
d8 = Square(olive, (295.25, 50))
e8 = Square(white, (377, 50))
f8 = Square(olive, (458.75, 50))
g8 = Square(white, (540.5, 50))
h8 = Square(olive, (622.25, 50))
a7 = Square(olive, (50, 131.75))
b7 = Square(white, (131.75, 131.75))
c7 = Square(olive, (213.5, 131.75))
d7 = Square(white, (295.25, 131.75))
e7 = Square(olive, (377, 131.75))
f7 = Square(white, (458.75, 131.75))
g7 = Square(olive, (540.5, 131.75))
h7 = Square(white, (622.25, 131.75))
a6 = Square(white, (50, 213.5))
b6 = Square(olive, (131.75, 213.5))
c6 = Square(white, (213.5, 213.5))
d6 = Square(olive, (295.25, 213.5))
e6 = Square(white, (377, 213.5))
f6 = Square(olive, (458.75, 213.5))
g6 = Square(white, (540.5, 213.5))
h6 = Square(olive, (622.25, 213.5))
a5 = Square(olive, (50, 295.25))
b5 = Square(white, (131.75, 295.25))
c5 = Square(olive, (213.5, 295.25))
d5 = Square(white, (295.25, 295.25))
e5 = Square(olive, (377, 295.25))
f5 = Square(white, (458.75, 295.25))
g5 = Square(olive, (540.5, 295.25))
h5 = Square(white, (622.25, 295.25))
a4 = Square(white, (50, 377))
b4 = Square(olive, (131.75, 377))
c4 = Square(white, (213.5, 377))
d4 = Square(olive, (295.25, 377))
e4 = Square(white, (377, 377))
f4 = Square(olive, (458.75, 377))
g4 = Square(white, (540.5, 377))
h4 = Square(olive, (622.25, 377))
a3 = Square(olive, (50, 458.75))
b3 = Square(white, (131.75, 458.75))
c3 = Square(olive, (213.5, 458.75))
d3 = Square(white, (295.25, 458.75))
e3 = Square(olive, (377, 458.75))
f3 = Square(white, (458.75, 458.75))
g3 = Square(olive, (540.5, 458.75))
h3 = Square(white, (622.25, 458.75))
a2 = Square(white, (50, 540.5))
b2 = Square(olive, (131.75, 540.5))
c2 = Square(white, (213.5, 540.5))
d2 = Square(olive, (295.25, 540.5))
e2 = Square(white, (377, 540.5))
f2 = Square(olive, (458.75, 540.5))
g2 = Square(white, (540.5, 540.5))
h2 = Square(olive, (622.25, 540.5))
a1 = Square(olive, (50, 622.25))
b1 = Square(white, (131.75, 622.25))
c1 = Square(olive, (213.5, 622.25))
d1 = Square(white, (295.25, 622.25))
e1 = Square(olive, (377, 622.25))
f1 = Square(white, (458.75, 622.25))
g1 = Square(olive, (540.5, 622.25))
h1 = Square(white, (622.25, 622.25))

# Coordinates relative to PyGame screen for each squares
coords =[[          (60,60), (145,60), (225,60), (310,60), (390,60), (470,60), (550,60), (630,60)],
                   [(60,145),(145,145),(225,145),(310,145),(390,145),(470,145),(550,145),(630,145)],
                   [(60,225),(145,225),(225,225),(310,225),(390,225),(470,225),(550,225),(630,225)],
                   [(60,310),(145,310),(225,310),(310,310),(390,310),(470,310),(550,310),(630,310)],
                   [(60,390),(145,390),(225,390),(310,390),(390,390),(470,390),(550,390),(630,390)],
                   [(60,470),(145,470),(225,470),(310,470),(390,470),(470,470),(550,470),(630,470)],
                   [(60,550),(145,550),(225,550),(310,550),(390,550),(470,550),(550,550),(630,550)],
                   [(60,630),(145,630),(225,630),(310,630),(390,630),(470,630),(550,630),(630,630)]]

# Maps the coords to their respective square


squares = {
coords[7][7]:   h1, coords[7][6]:	h2, coords[7][5]:	h3, coords[7][4]:	h4, coords[7][3]:	h5, coords[7][2]:	h6, coords[7][1]:	h7, coords[7][0]:	h8,
coords[6][7]:   g1, coords[6][6]:	g2, coords[6][5]:	g3, coords[6][4]:	g4, coords[6][3]:	g5, coords[6][2]:	g6, coords[6][1]:	g7, coords[6][0]:	g8,
coords[5][7]:   f1, coords[5][6]:	f2, coords[5][5]:	f3, coords[5][4]:	f4, coords[5][3]:	f5, coords[5][2]:	f6, coords[5][1]:	f7, coords[5][0]:	f8,
coords[4][7]:   e1, coords[4][6]:	e2, coords[4][5]:	e3, coords[4][4]:	e4, coords[4][3]:	e5, coords[4][2]:	e6, coords[4][1]:	e7,  coords[4][0]:	e8,
coords[3][7]:   d1, coords[3][6]:	d2, coords[3][5]:	d3, coords[3][4]:	d4, coords[3][3]:	d5, coords[3][2]:	d6, coords[3][1]:	d7, coords[3][0]:	d8,
coords[2][7]:    c1, coords[2][6]:	c2, coords[2][5]:	c3, coords[2][4]:	c4, coords[2][3]:	c5, coords[2][2]:	c6, coords[2][1]:	c7, coords[2][0]:	c8,
coords[1][7]:    b1, coords[1][6]:	b2, coords[1][5]:	b3, coords[1][4]:	b4, coords[1][3]:	b5, coords[1][2]:	b6, coords[1][1]:	b7, coords[1][0]:   b8,
coords[0][7]:    a1, coords[0][6]:	a2, coords[0][5]:	a3, coords[0][4]:	a4, coords[0][3]:	a5, coords[0][2]:	a6,  coords[0][1]:	a7, coords[0][0]:	a8
}