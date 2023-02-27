from pygame import display
from classes import King,Queen,Bishop,Knight,Rook,Pawn
from board import coords

screen = display.set_mode((1000, 775))

# White
wking = King(screen, '.\\white\\white_king.png', coords[7][4], 'white')
wqueen = Queen(screen, '.\\white\\white_queen.png',coords[7][3], 'white')
wbishop1 = Bishop(screen, '.\\white\\white_bishop.png', coords[7][2], 'white')
wbishop2 = Bishop(screen, '.\\white\\white_bishop.png', coords[7][5], 'white')
wknight1 = Knight(screen, '.\\white\\white_knight.png', coords[7][1], 'white')
wknight2 = Knight(screen, '.\\white\\white_knight.png', coords[7][6], 'white')
wrook1 = Rook(screen, '.\\white\\white_rook.png', coords[7][0], 'white')
wrook2 = Rook(screen, '.\\white\\white_rook.png', coords[7][7], 'white')

wpawn1 = Pawn(screen, '.\\white\\white_pawn.png', coords[6][0], 'white')
wpawn2 = Pawn(screen, '.\\white\\white_pawn.png', coords[6][1], 'white')
wpawn3 = Pawn(screen, '.\\white\\white_pawn.png', coords[6][2], 'white')
wpawn4 = Pawn(screen, '.\\white\\white_pawn.png', coords[6][3], 'white')
wpawn5 = Pawn(screen, '.\\white\\white_pawn.png', coords[6][4], 'white')
wpawn6 = Pawn(screen, '.\\white\\white_pawn.png', coords[6][5], 'white')
wpawn7 = Pawn(screen, '.\\white\\white_pawn.png', coords[6][6], 'white')
wpawn8 = Pawn(screen, '.\\white\\white_pawn.png', coords[6][7], 'white')

# Black
bking = King(screen, '.\\black\\black_king.png', coords[0][4], 'black')
bqueen = Queen(screen, '.\\black\\black_queen.png', coords[0][3], 'black')
bbishop1 = Bishop(screen, '.\\black\\black_bishop.png', coords[0][2], 'black')
bbishop2 = Bishop(screen, '.\\black\\black_bishop.png', coords[0][5], 'black')
bknight1 = Knight(screen, '.\\black\\black_knight.png', coords[0][1], 'black')
bknight2 = Knight(screen, '.\\black\\black_knight.png', coords[0][6], 'black')
brook1 = Rook(screen, '.\\black\\black_rook.png', coords[0][0], 'black')
brook2 = Rook(screen, '.\\black\\black_rook.png', coords[0][7], 'black')

bpawn1 = Pawn(screen, '.\\black\\black_pawn.png', coords[1][0], 'black')
bpawn2 = Pawn(screen, '.\\black\\black_pawn.png', coords[1][1], 'black')
bpawn3 = Pawn(screen, '.\\black\\black_pawn.png', coords[1][2], 'black')
bpawn4 = Pawn(screen, '.\\black\\black_pawn.png', coords[1][3], 'black')
bpawn4 = Pawn(screen, '.\\black\\black_pawn.png', coords[1][3], 'black')
bpawn5 = Pawn(screen, '.\\black\\black_pawn.png', coords[1][4], 'black')
bpawn6 = Pawn(screen, '.\\black\\black_pawn.png', coords[1][5], 'black')
bpawn7 = Pawn(screen, '.\\black\\black_pawn.png', coords[1][6], 'black')
bpawn8 = Pawn(screen, '.\\black\\black_pawn.png', coords[1][7], 'black')