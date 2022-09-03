import random

rps= ['rock','paper','scissors']
cpu = 0
user= 0
while True:
    x = input('Rock, Paper, or Scissors? ')
    y = random.choice(rps)
    print(y)

    if x.lower()=='rock':
        if y=='rock':
            print('Go again')
            continue
        elif y=='paper':
            print('Ha Ha you lose')
            cpu+=1
        elif y=='scissors':
            print('good for you... lucky')
            user+=1
        
    elif x.lower()=='paper':
        if y=='rock':
            print('good for you... lucky')
            user+=1
        elif y=='paper':
            print('Go again')
            continue
        elif y=='scissors':
            print('Ha Ha you lose')
            cpu+=1


    elif x.lower()=='scissors':
        if y=='rock':
            print('Ha Ha you lose')
            cpu+=1
        elif y=='paper':
            print('good for you... lucky')
            user+=1
        elif y=='scissors':
            print('Go again')
            continue
        
    else:
        print('Type it again idiot')
        continue

    if cpu%5==0 and cpu!=0:
        print("The computer has an ego")
        print('The computer got',cpu,'points')
    elif user%5==0 and user !=0:
        print("You have an ego")
        print('You got',user,'points')
