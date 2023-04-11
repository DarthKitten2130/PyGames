import random


cpu = 0
user = 0

def Battle(you):
    global cpu,user
    rps = ['rock', 'paper', 'scissors']
    system = {'rock':'scissors',
              'paper':'rock',
              'scissors':'paper'}
    comp = random.choice(rps)
    
    if you.lower() == 'quit':
        quit()

    elif you.lower() not in rps:
        print('type it again idiot! ')

    elif you.lower() == comp:
        print(comp)
        print('Go Again')

    elif system[comp] == you.lower():
        print(comp)
        print('Ha ha you lose!')
        cpu += 1

    elif system[you.lower()] == comp:
        print('Good for you... lucky')
        print(comp)
        user += 1


    if cpu % 5 == 0 and cpu != 0:
        print("The computer has an ego")
        print('The computer got', cpu, 'points')
    elif user % 5 == 0 and user != 0:
        print("You have an ego")
        print('You got', user, 'points')
    

while True:
    x = input('Rock, Paper, or Scissors? (type quit to quit the game) ')
    Battle(x)

   
