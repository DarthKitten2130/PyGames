import os

def imp(name):
        module = __import__(name)
        return module

while True:

    print("Welcome to PyGames! Please choose a game to play!")
    game = input("Your options are:\nRock, Paper, Scissors\nHangman\nTic Tac Toe\nChoose Wisely. ")
    game_names = {'rps':'rps',
                'Hangman':'hangman',
                'Tic Tac Toe':'tic_tac_toe'}

    

    imp(game_names[game])