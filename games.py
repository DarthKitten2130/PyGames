import os


print("Welcome to PyGames! Please choose a game to play!")
game = input("Your options are:\nRock, Paper, Scissors\nHangman\nTic Tac Toe\nChoose Wisely. ")
game_names = {'Rock, Paper, Scissors':'rps',
              'Hangman':'hangman',
              'Tic Tac Toe':'tic_tac_toe'}

def imp(name):
    module = __import__(name)
    return module

imp(game_names[game])