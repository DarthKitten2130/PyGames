import random
import turtle
from os import chdir
import platform
os = platform.system()

if os == 'Windows':
    chdir('.\\words')
elif os == 'Linux' or os == 'Darwin':
    chdir('./words')

# Variables:
letters_done = []
strikes = 0
Tlist = []

# Graphics
shapes = ['t.lt(90)\nt.fd(300)\nt.rt(90)\nt.fd(200)',
          't.rt(90)\nt.fd(100)',
          't.penup()\nt.goto(-40,60)\nt.pendown()\nt.circle(40)',
          't.penup()\nt.goto(0,20)\nt.pendown()\nt.fd(80)',
          't.goto(30,-100)',
          't.penup()\nt.goto(0,-60)\nt.pendown()\nt.goto(-30,-100)',
          't.penup()\nt.home()\nt.pendown()\nt.goto(-50,30)',
          't.penup()\nt.home()\nt.pendown()\nt.goto(50,30)']


while True:
    screen = turtle.getscreen()
    turtle.title("Hangman")
    t = turtle.Turtle()
    t.penup()
    t.goto(-200, -100)
    t.pendown()

    # Topic Choice

    u = input('Which topic? Your choices are:\nanimals\nfood ')
    v = input('Should we display vowels? Yes or no? ')

    with open(f'{u}.txt', 'rt') as f:
        for line in f:
            nline = line.lower()
            nline = nline.replace('\n', '')
            Tlist.append(nline)

    # Variables
    word = random.choice(Tlist)
    count = len(word)
    display = ""

    # Display
    if v.lower() == 'no':
        for w in word:
            if w == ' ':
                w = '-'
            else:
                w = '_ '
            display = display + w
    elif v.lower() == 'yes':
        for w in word:
            if w == 'a' or w == 'e' or w == 'i' or w == 'o' or w == 'u':
                w = w + ' '
            elif w == ' ':
                w = '-'
            else:
                w = '_ '
            display = display + w
    else:
        print('Error')
        continue
    print(display.replace('-', '\t'))

    # Game
    done_word = [z for z in display if z != ' ']

    while word != ''.join(done_word).replace('-', '\t'):
         x = input('Enter a letter ').lower()

         if v.lower() == 'yes':
             letters_done.extend(['a','e','i','o','u'])

         if x.isspace() == True or x.isnumeric() == True:
            print("Letters only")
            continue
         elif letters_done.count(x) != 0:
            print('Letter already used')
            continue
        # Incorrect Option
         elif word.count(x) == 0:
            print("Incorrect")
            strikes += 1
            try:
                exec(shapes[strikes-1])
            except:
                break
            letters_done.append(x)

        # Correct Option
         else:
            letters_done.append(x)
            y = 0
            for w in word:
                if w == x:
                    done_word.pop(y)
                    done_word.insert(y, x)
                y += 1
            i = ''
            for w in ''.join(done_word).replace('-', ' '):
                w = w+' '
                i = i+w
            print(i)


    if word == ''.join(done_word).replace('-', ' '):
         print('good job')
    else:
         print('Ha ha you lose')
    print('\n'*5)
    letters_done.clear()
    screen.clear()
