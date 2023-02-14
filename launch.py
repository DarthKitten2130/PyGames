import platform

os = platform.system()


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

    imp(game_names[game])
