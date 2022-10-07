from chess.classes import *
from pygame import display

screen = display.set_mode((1000, 775))

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


# White
wking = King(screen, '.\\white\\white_king.png', coords[7, 4], 'white')
wqueen = Queen(screen, '.\\white\\white_queen.png',
               coords[7, 3], 'white')
wbishop1 = Bishop(
    screen, '.\\white\\white_bishop.png', coords[7, 2], 'white')
wbishop2 = Bishop(
    screen, '.\\white\\white_bishop.png', coords[7, 5], 'white')
wknight1 = Knight(
    screen, '.\\white\\white_knight.png', coords[7, 1], 'white')
wknight2 = Knight(
    screen, '.\\white\\white_knight.png', coords[7, 6], 'white')
wrook1 = Rook(screen, '.\\white\\white_rook.png', coords[7, 0], 'white')
wrook2 = Rook(screen, '.\\white\\white_rook.png', coords[7, 7], 'white')

wpawn1 = Pawn(screen, '.\\white\\white_pawn.png', coords[6, 0], 'white')
wpawn2 = Pawn(screen, '.\\white\\white_pawn.png', coords[6, 1], 'white')
wpawn3 = Pawn(screen, '.\\white\\white_pawn.png', coords[6, 2], 'white')
wpawn4 = Pawn(screen, '.\\white\\white_pawn.png', coords[6, 3], 'white')
wpawn5 = Pawn(screen, '.\\white\\white_pawn.png', coords[6, 4], 'white')
wpawn6 = Pawn(screen, '.\\white\\white_pawn.png', coords[6, 5], 'white')
wpawn7 = Pawn(screen, '.\\white\\white_pawn.png', coords[6, 6], 'white')
wpawn8 = Pawn(screen, '.\\white\\white_pawn.png', coords[6, 7], 'white')

# Black
bking = King(screen, '.\\black\\black_king.png', coords[0, 4], 'black')
bqueen = Queen(screen, '.\\black\\black_queen.png',
               coords[0, 3], 'black')
bbishop1 = Bishop(
    screen, '.\\black\\black_bishop.png', coords[0, 2], 'black')
bbishop2 = Bishop(
    screen, '.\\black\\black_bishop.png', coords[0, 5], 'black')
bknight1 = Knight(
    screen, '.\\black\\black_knight.png', coords[0, 1], 'black')
bknight2 = Knight(
    screen, '.\\black\\black_knight.png', coords[0, 6], 'black')
brook1 = Rook(screen, '.\\black\\black_rook.png', coords[0, 0], 'black')
brook2 = Rook(screen, '.\\black\\black_rook.png', coords[0, 7], 'black')

bpawn1 = Pawn(screen, '.\\black\\black_pawn.png', coords[1, 0], 'black')
bpawn2 = Pawn(screen, '.\\black\\black_pawn.png', coords[1, 1], 'black')
bpawn3 = Pawn(screen, '.\\black\\black_pawn.png', coords[1, 2], 'black')
bpawn4 = Pawn(screen, '.\\black\\black_pawn.png', coords[1, 3], 'black')
bpawn4 = Pawn(screen, '.\\black\\black_pawn.png', coords[1, 3], 'black')
bpawn5 = Pawn(screen, '.\\black\\black_pawn.png', coords[1, 4], 'black')
bpawn6 = Pawn(screen, '.\\black\\black_pawn.png', coords[1, 5], 'black')
bpawn7 = Pawn(screen, '.\\black\\black_pawn.png', coords[1, 6], 'black')
bpawn8 = Pawn(screen, '.\\black\\black_pawn.png', coords[1, 7], 'black')
