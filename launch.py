import platform
import os

def imp(name):
    module = __import__(name)
    return module


while True:

    game_names = {'rps': 'rps',
                  'Hangman': 'hangman',
                  'Tic Tac Toe': 'tic_tac_toe',
                  'Chess': 'chess.chess_launch'}


    print("Welcome to PyGames! Please choose a game to play!")
    game = input(
        "Your options are:\nRock, Paper, Scissors\nHangman\nTic Tac Toe\nChess\nChoose Wisely. ")

    if game == 'Chess':
        os.chdir(r'C:\\Users\\darth\\Desktop\\Python_Programs\\PyGames\\PyGames\\chess')


    imp(game_names[game])
