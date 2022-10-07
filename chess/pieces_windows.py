from chess.classes import *
from pygame import display

screen = display.set_mode((1000, 775))

# Squares
white = '.\\squares\\white.png'
olive = '.\\squares\\olive.png'
a1 = Square(olive, (50, 50))
b1 = Square(white, (131.75, 50))
c1 = Square(olive, (213.5, 50))
d1 = Square(white, (295.25, 50))
e1 = Square(olive, (377, 50))
f1 = Square(white, (458.75, 50))
g1 = Square(olive, (540.5, 50))
h1 = Square(white, (622.25, 50))
a2 = Square(white, (50, 131.75))
b2 = Square(olive, (131.75, 131.75))
c2 = Square(white, (213.5, 131.75))
d2 = Square(olive, (295.25, 131.75))
e2 = Square(white, (377, 131.75))
f2 = Square(olive, (458.75, 131.75))
g2 = Square(white, (540.5, 131.75))
h2 = Square(olive, (622.25, 131.75))
a3 = Square(olive, (50, 213.5))
b3 = Square(white, (131.75, 213.5))
c3 = Square(olive, (213.5, 213.5))
d3 = Square(white, (295.25, 213.5))
e3 = Square(olive, (377, 213.5))
f3 = Square(white, (458.75, 213.5))
g3 = Square(olive, (540.5, 213.5))
h3 = Square(white, (622.25, 213.5))
a4 = Square(white, (50, 295.25))
b4 = Square(olive, (131.75, 295.25))
c4 = Square(white, (213.5, 295.25))
d4 = Square(olive, (295.25, 295.25))
e4 = Square(white, (377, 295.25))
f4 = Square(olive, (458.75, 295.25))
g4 = Square(white, (540.5, 295.25))
h4 = Square(olive, (622.25, 295.25))
a5 = Square(olive, (50, 377))
b5 = Square(white, (131.75, 377))
c5 = Square(olive, (213.5, 377))
d5 = Square(white, (295.25, 377))
e5 = Square(olive, (377, 377))
f5 = Square(white, (458.75, 377))
g5 = Square(olive, (540.5, 377))
h5 = Square(white, (622.25, 377))
a6 = Square(white, (50, 458.75))
b6 = Square(olive, (131.75, 458.75))
c6 = Square(white, (213.5, 458.75))
d6 = Square(olive, (295.25, 458.75))
e6 = Square(white, (377, 458.75))
f6 = Square(olive, (458.75, 458.75))
g6 = Square(white, (540.5, 458.75))
h6 = Square(olive, (622.25, 458.75))
a7 = Square(olive, (50, 540.5))
b7 = Square(white, (131.75, 540.5))
c7 = Square(olive, (213.5, 540.5))
d7 = Square(white, (295.25, 540.5))
e7 = Square(olive, (377, 540.5))
f7 = Square(white, (458.75, 540.5))
g7 = Square(olive, (540.5, 540.5))
h7 = Square(white, (622.25, 540.5))
a8 = Square(white, (50, 622.25))
b8 = Square(olive, (131.75, 622.25))
c8 = Square(white, (213.5, 622.25))
d8 = Square(olive, (295.25, 622.25))
e8 = Square(white, (377, 622.25))
f8 = Square(olive, (458.75, 622.25))
g8 = Square(white, (540.5, 622.25))
h8 = Square(olive, (622.25, 622.25))


# White
wking = Units.King(screen, '.\\white\\white_king.png', coords[7, 4], 'white')
wqueen = Units.Queen(screen, '.\\white\\white_queen.png',
                     coords[7, 3], 'white')
wbishop1 = Units.Bishop(
    screen, '.\\white\\white_bishop.png', coords[7, 2], 'white')
wbishop2 = Units.Bishop(
    screen, '.\\white\\white_bishop.png', coords[7, 5], 'white')
wknight1 = Units.Knight(
    screen, '.\\white\\white_knight.png', coords[7, 1], 'white')
wknight2 = Units.Knight(
    screen, '.\\white\\white_knight.png', coords[7, 6], 'white')
wrook1 = Units.Rook(screen, '.\\white\\white_rook.png', coords[7, 0], 'white')
wrook2 = Units.Rook(screen, '.\\white\\white_rook.png', coords[7, 7], 'white')

wpawn1 = Units.Pawn(screen, '.\\white\\white_pawn.png', coords[6, 0], 'white')
wpawn2 = Units.Pawn(screen, '.\\white\\white_pawn.png', coords[6, 1], 'white')
wpawn3 = Units.Pawn(screen, '.\\white\\white_pawn.png', coords[6, 2], 'white')
wpawn4 = Units.Pawn(screen, '.\\white\\white_pawn.png', coords[6, 3], 'white')
wpawn5 = Units.Pawn(screen, '.\\white\\white_pawn.png', coords[6, 4], 'white')
wpawn6 = Units.Pawn(screen, '.\\white\\white_pawn.png', coords[6, 5], 'white')
wpawn7 = Units.Pawn(screen, '.\\white\\white_pawn.png', coords[6, 6], 'white')
wpawn8 = Units.Pawn(screen, '.\\white\\white_pawn.png', coords[6, 7], 'white')

# Black
bking = Units.King(screen, '.\\black\\black_king.png', coords[0, 4], 'black')
bqueen = Units.Queen(screen, '.\\black\\black_queen.png',
                     coords[0, 3], 'black')
bbishop1 = Units.Bishop(
    screen, '.\\black\\black_bishop.png', coords[0, 2], 'black')
bbishop2 = Units.Bishop(
    screen, '.\\black\\black_bishop.png', coords[0, 5], 'black')
bknight1 = Units.Knight(
    screen, '.\\black\\black_knight.png', coords[0, 1], 'black')
bknight2 = Units.Knight(
    screen, '.\\black\\black_knight.png', coords[0, 6], 'black')
brook1 = Units.Rook(screen, '.\\black\\black_rook.png', coords[0, 0], 'black')
brook2 = Units.Rook(screen, '.\\black\\black_rook.png', coords[0, 7], 'black')

bpawn1 = Units.Pawn(screen, '.\\black\\black_pawn.png', coords[1, 0], 'black')
bpawn2 = Units.Pawn(screen, '.\\black\\black_pawn.png', coords[1, 1], 'black')
bpawn3 = Units.Pawn(screen, '.\\black\\black_pawn.png', coords[1, 2], 'black')
bpawn4 = Units.Pawn(screen, '.\\black\\black_pawn.png', coords[1, 3], 'black')
bpawn4 = Units.Pawn(screen, '.\\black\\black_pawn.png', coords[1, 3], 'black')
bpawn5 = Units.Pawn(screen, '.\\black\\black_pawn.png', coords[1, 4], 'black')
bpawn6 = Units.Pawn(screen, '.\\black\\black_pawn.png', coords[1, 5], 'black')
bpawn7 = Units.Pawn(screen, '.\\black\\black_pawn.png', coords[1, 6], 'black')
bpawn8 = Units.Pawn(screen, '.\\black\\black_pawn.png', coords[1, 7], 'black')
