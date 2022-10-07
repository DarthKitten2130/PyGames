import random

rps = ['rock', 'paper', 'scissors']
cpu = 0
user = 0
while True:
    x = input('Rock, Paper, or Scissors? (type quit to quit the game) ')
    y = random.choice(rps)

    if x.lower() == 'rock':
        print(y)
        if y == 'rock':
            print('Go again')
            continue
        elif y == 'paper':
            print('Ha Ha you lose')
            cpu += 1
        elif y == 'scissors':
            print('good for you... lucky')
            user += 1

    elif x.lower() == 'paper':
        print(y)
        if y == 'rock':
            print('good for you... lucky')
            user += 1
        elif y == 'paper':
            print('Go again')
            continue
        elif y == 'scissors':
            print('Ha Ha you lose')
            cpu += 1

    elif x.lower() == 'scissors':
        print(y)
        if y == 'rock':
            print('Ha Ha you lose')
            cpu += 1
        elif y == 'paper':
            print('good for you... lucky')
            user += 1
        elif y == 'scissors':
            print('Go again')
            continue

    elif x.lower() == 'quit':
        quit()

    else:
        print('Type it again idiot')
        continue

    if cpu % 5 == 0 and cpu != 0:
        print("The computer has an ego")
        print('The computer got', cpu, 'points')
    elif user % 5 == 0 and user != 0:
        print("You have an ego")
        print('You got', user, 'points')
