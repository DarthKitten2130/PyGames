import platform

os = platform.system()

def imp(name):
        module = __import__(name)
        return module

while True:

    game_names = {'rps':'rps',
                'Hangman':'hangman',
                'Tic Tac Toe':'tic_tac_toe','Chess':''}

    if os == 'Windows':
        game_names['Chess'] = 'chess_windows'
    elif os == 'Linux' or os == 'Darwin':
        game_names['Chess'] = 'chess_linux'

    print("Welcome to PyGames! Please choose a game to play!")
    game = input("Your options are:\nRock, Paper, Scissors\nHangman\nTic Tac Toe\nChoose Wisely. ")
    

    

    imp(game_names[game])