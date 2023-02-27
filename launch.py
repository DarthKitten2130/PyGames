from pathlib import Path
import os

new_path = Path(__file__).parent
os.chdir(new_path)

def imp(name):
    module = __import__(name)
    return module


while True:

    game_names = {'rps': 'rps',
                  'Hangman': 'hangman',
                  'Tic Tac Toe': 'tic_tac_toe'
                  }


    print("Welcome to PyGames! Please choose a game to play!")
    game = input(
        "Your options are:\nRock, Paper, Scissors\nHangman\nTic Tac Toe\nChoose Wisely. ")

    imp(game_names[game])
