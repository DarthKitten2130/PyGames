from chess.classes import *
from pygame import display

screen = display.set_mode((1000,775))

# Squares
white = './squares/white.png'
olive = './squares/olive.png'
a1 = Square(olive, (50, 50))
b1 = Square(white, (50, 104.5))
c1 = Square(olive, (50, 159))
d1 = Square(white, (50, 213.5))
e1 = Square(olive, (50, 268))
f1 = Square(white, (50, 322.5))
g1 = Square(olive, (50, 377))
h1 = Square(white, (50, 431.5))
a2 = Square(white, (104.5, 50))
b2 = Square(olive, (104.5, 104.5))
c2 = Square(white, (104.5, 159))
d2 = Square(olive, (104.5, 213.5))
e2 = Square(white, (104.5, 268))
f2 = Square(olive, (104.5, 322.5))
g2 = Square(white, (104.5, 377))
h2 = Square(olive, (104.5, 431.5))
a3 = Square(olive, (159, 50))
b3 = Square(white, (159, 104.5))
c3 = Square(olive, (159, 159))
d3 = Square(white, (159, 213.5))
e3 = Square(olive, (159, 268))
f3 = Square(white, (159, 322.5))
g3 = Square(olive, (159, 377))
h3 = Square(white, (159, 431.5))
a4 = Square(white, (213.5, 50))
b4 = Square(olive, (213.5, 104.5))
c4 = Square(white, (213.5, 159))
d4 = Square(olive, (213.5, 213.5))
e4 = Square(white, (213.5, 268))
f4 = Square(olive, (213.5, 322.5))
g4 = Square(white, (213.5, 377))
h4 = Square(olive, (213.5, 431.5))
a5 = Square(olive, (268, 50))
b5 = Square(white, (268, 104.5))
c5 = Square(olive, (268, 159))
d5 = Square(white, (268, 213.5))
e5 = Square(olive, (268, 268))
f5 = Square(white, (268, 322.5))
g5 = Square(olive, (268, 377))
h5 = Square(white, (268, 431.5))
a6 = Square(white, (322.5, 50))
b6 = Square(olive, (322.5, 104.5))
c6 = Square(white, (322.5, 159))
d6 = Square(olive, (322.5, 213.5))
e6 = Square(white, (322.5, 268))
f6 = Square(olive, (322.5, 322.5))
g6 = Square(white, (322.5, 377))
h6 = Square(olive, (322.5, 431.5))
a7 = Square(olive, (377, 50))
b7 = Square(white, (377, 104.5))
c7 = Square(olive, (377, 159))
d7 = Square(white, (377, 213.5))
e7 = Square(olive, (377, 268))
f7 = Square(white, (377, 322.5))
g7 = Square(olive, (377, 377))
h7 = Square(white, (377, 431.5))
a8 = Square(white, (431.5, 50))
b8 = Square(olive, (431.5, 104.5))
c8 = Square(white, (431.5, 159))
d8 = Square(olive, (431.5, 213.5))
e8 = Square(white, (431.5, 268))
f8 = Square(olive, (431.5, 322.5))
g8 = Square(white, (431.5, 377))
h8 = Square(olive, (431.5, 431.5))


# White
wking = Units.King(screen,'./white/white_king.png',coords[7,4],'white')
wqueen = Units.Queen(screen,'./white/white_queen.png',coords[7,3],'white')
wbishop1 = Units.Bishop(screen,'./white/white_bishop.png',coords[7,2],'white')
wbishop2 = Units.Bishop(screen,'./white/white_bishop.png',coords[7,5],'white')
wknight1 = Units.Knight(screen,'./white/white_knight.png',coords[7,1],'white')
wknight2 = Units.Knight(screen,'./white/white_knight.png',coords[7,6],'white')
wrook1 = Units.Rook(screen,'./white/white_rook.png',coords[7,0],'white')
wrook2 = Units.Rook(screen,'./white/white_rook.png',coords[7,7],'white')

wpawn1 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,0],'white')
wpawn2 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,1],'white')
wpawn3 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,2],'white')
wpawn4 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,3],'white')
wpawn5 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,4],'white')
wpawn6 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,5],'white')
wpawn7 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,6],'white')
wpawn8 = Units.Pawn(screen,'./white/white_pawn.png',coords[6,7],'white')

# Black
bking = Units.King(screen,'./black/black_king.png',coords[0,4],'black')
bqueen = Units.Queen(screen,'./black/black_queen.png',coords[0,3],'black')
bbishop1 = Units.Bishop(screen,'./black/black_bishop.png',coords[0,2],'black')
bbishop2 = Units.Bishop(screen,'./black/black_bishop.png',coords[0,5],'black')
bknight1 = Units.Knight(screen,'./black/black_knight.png',coords[0,1],'black')
bknight2 = Units.Knight(screen,'./black/black_knight.png',coords[0,6],'black')
brook1 = Units.Rook(screen,'./black/black_rook.png',coords[0,0],'black')
brook2 = Units.Rook(screen,'./black/black_rook.png',coords[0,7],'black')

bpawn1 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,0],'black')
bpawn2 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,1],'black')
bpawn3 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,2],'black')
bpawn4 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,3],'black')
bpawn4 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,3],'black')
bpawn5 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,4],'black')
bpawn6 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,5],'black')
bpawn7 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,6],'black')
bpawn8 = Units.Pawn(screen,'./black/black_pawn.png',coords[1,7],'black')
