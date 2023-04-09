from os.path import join
from classes import King,Queen,Bishop,Knight,Rook,Pawn
from board import *



# White
wking = King(e1, join('.','white','white_king.png'),'white')
wqueen = Queen(d1, join('.','white','white_queen.png'),'white')
wbishop1 = Bishop(c1,join('.','white','white_bishop.png'),'white')
wbishop2 = Bishop(f1, join('.','white','white_bishop.png'),'white')
wknight1 = Knight(b1, join('.','white','white_knight.png'),'white')
wknight2 = Knight(g1, join('.','white','white_knight.png'),'white')
wrook1 = Rook(a1, join('.','white','white_rook.png'),'white')
wrook2 = Rook(h1, join('.','white','white_rook.png'),'white')

wpawn1 = Pawn(a2, join('.','white','white_pawn.png'),'white')
wpawn2 = Pawn(b2, join('.','white','white_pawn.png'),'white')
wpawn3 = Pawn(c2, join('.','white','white_pawn.png'),'white')
wpawn4 = Pawn(d2, join('.','white','white_pawn.png'),'white')
wpawn5 = Pawn(e2, join('.','white','white_pawn.png'),'white')
wpawn6 = Pawn(f2, join('.','white','white_pawn.png'),'white')
wpawn7 = Pawn(g2, join('.','white','white_pawn.png'),'white')
wpawn8 = Pawn(h2, join('.','white','white_pawn.png'),'white')

# Black
bking = King(e8, join('.','black','black_king.png'),'black')
bqueen = Queen(d8, join('.','black','black_queen.png'),'black')
bbishop1 = Bishop(c8, join('.','black','black_bishop.png'),'black')
bbishop2 = Bishop(f8, join('.','black','black_bishop.png'),'black')
bknight1 = Knight(b8, join('.','black','black_knight.png'),'black')
bknight2 = Knight(g8, join('.','black','black_knight.png'),'black')
brook1 = Rook(a8, join('.','black','black_rook.png'),'black')
brook2 = Rook(h8, join('.','black','black_rook.png'),'black')

bpawn1 = Pawn(a7, join('.','black','black_pawn.png'),'black')
bpawn2 = Pawn(b7, join('.','black','black_pawn.png'),'black')
bpawn3 = Pawn(c7, join('.','black','black_pawn.png'),'black')
bpawn4 = Pawn(d7, join('.','black','black_pawn.png'),'black')
bpawn5 = Pawn(e7, join('.','black','black_pawn.png'),'black')
bpawn6 = Pawn(f7, join('.','black','black_pawn.png'),'black')
bpawn7 = Pawn(g7, join('.','black','black_pawn.png'),'black')
bpawn8 = Pawn(h7, join('.','black','black_pawn.png'),'black')
