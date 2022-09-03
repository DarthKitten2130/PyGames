import random
import turtle
import numpy as np

# Board
screen = turtle.getscreen()
screen.bgcolor("black")
t = turtle.Turtle()
t.pencolor("white")
t.hideturtle()
t.speed(10)
t.penup()
t.goto(-150,-150)
t.pendown()
t.lt(90)
t.fd(300)
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(300)
t.rt(90)
t.fd(300)

t.penup()
t.goto(-50,-150)
t.pendown()
t.rt(90)
t.fd(300)
t.penup()
t.goto(50,-150)
t.pendown()
t.fd(300)
t.rt(90)
t.penup()
t.goto(-150,-50)
t.pendown()
t.fd(300)
t.penup()
t.goto(-150,50)
t.pendown()
t.fd(300)
t.width(4)
t.pencolor("pink")
 
# Game
def O(x,y):
     t.penup()
     t.goto(x,y)
     t.pendown()
     t.circle(40)

def X(x,y):
     t.penup()
     t.goto(x,y)
     t.fd(25)
     t.lt(135)
     t.pendown()
     t.fd(75)
     t.penup()
     t.rt(135)
     t.fd(50)
     t.rt(135)
     t.pendown()
     t.fd(75)
     t.lt(135)
  
# Win Conditions:
def Hcheck():
    global filled
    global win
    xcount = 0
    ocount = 0
    for y in range(0,3):
        for x in range(0,3):
            if filled[x,y]=='X':
                xcount+=1
            elif filled[x,y]=='O':
                ocount+=1
        if xcount==3:
            win = True
        elif ocount==3:
            win = True
        xcount = 0
        ocount = 0
    return(win)

squares = {"1" : [-100,75], "2" : [0,75], "3" : [100,75],
           "4" : [-100,-25], "5" : [0,-25], "6" : [100,-25],
           "7" : [-100,-125], "8" : [0,-125], "9" : [100,-125]}

coords = {'1':(0,0),'2':(0,1),'3':(0,2),
          '4':(1,0),'5':(1,1),'6':(1,2),
          '7':(2,0),'8':(2,1),'9':(2,2)}

filled = np.array([['n','n','n'],
                   ['n','n','n'],
                   ['n','n','n']])

turn  = 1
win = False

while True:
     print('''1   2   3

4   5   6

7   8   9''')
     print("Welcome to Tic Tac Toe")
     players = int(input("How many players? Max 2 "))
     if players==2:
        p1 = input("X or O? ").upper()
        if p1=='X':
            p2 = 'O'
        elif p1=='O':
            p2 = 'X'
        else:
            print("Error")
            continue
        while win==False: 
             while turn == 1:
                  Hcheck()
                  place1 = input(f"Player 1, where will you place your {p1} ? (Choose a number). ")

                  if place1.isnumeric()==False:
                      print("Try again")
                      continue
                  elif int(place1)>9 or int(place1)<1:
                      print('Try again')

                  elif filled[coords[place1]] != 'n':
                       print('Spot already taken!')
                       continue
                  elif p1=='X':
                       X(squares[place1][0],squares[place1][1])
                       filled[coords[place1]]='X'
                  else:
                       O(squares[place1][0],squares[place1][1]-20)
                       filled[coords[place1]]='O'
                  turn = 2
                  
             while turn == 2:
                  Hcheck()
                  place2 = input(f"Player 2, where will you place your {p2} ? (Choose a number). ")
                  if place2.isnumeric()==False:
                       print("Try again")
                       continue
                  elif int(place2)>9 or int(place1)<1:
                       print('Try again')
                       continue
                 
                  elif filled[coords[place2]] != 'n':
                       print('Spot already taken!')
                       continue
                  elif p2=='X':
                       X(squares[place2][0],squares[place2][1])
                       filled[coords[place2]]='X'
                  else:
                       O(squares[place2][0],squares[place2][1]-20)
                       filled[coords[place2]]='O'
                  turn = 1
              
     elif players==1:
        p1 = input("X or O? ").upper()
        if p1 != "X" and p1 != "O":
            print('Error')
            continue
	  
     else:
        print("Only 2 players allowed")
        continue
'''1   2   3
   4   5   6
   7   8   9'''
