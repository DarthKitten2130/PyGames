from chess.classes import *
from pygame import display

screen = display.set_mode((1000,775))

# Squares
white = './squares/white.png'
olive = './squares/olive.png'
a8 = Square((50,50), white)
b8 = Square((104.5,50),olive)

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

