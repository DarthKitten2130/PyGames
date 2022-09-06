import random
import turtle

# Board
screen = turtle.getscreen()
t = turtle.Turtle()
screen.bgcolor("black")
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
 

turn  = 1
win = False
winner = ''
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


# Win conditions

def Hcheck(filled):
     global win
     global winner
     global turn
     for row in filled:
               
               if row.count('X')== 3:
                    win,winner,turn = True,'X',0
                    
               elif row.count('O')== 3:
                    win,winner,turn = True,'O',0
     return [win,winner,turn]


def Vcheck(filled):
     global win
     global winner
     global turn
     vxcount = vocount = 0
     for x in range(3):
          for row in filled:
               if row[x] == 'X':
                    vxcount+=1
               elif row[x] == 'O':
                    vocount+=1
          if vxcount == 3:
               win,winner,turn = True,'X',0
          elif vocount == 3:
               win,winner,turn = True,'O',0
          vxcount = vocount = 0

     return [win,winner,turn,vxcount,vocount]     


def Dcheck(filled):
     global win
     global winner
     global turn
     dxcount = docount = 0

     # Negative Diagonal
     x = 0
     for row in filled:
          if row[x] == 'X':
               dxcount+=1
          elif row[x] == 'O':
               docount +=1
          x+=1
               
     if dxcount == 3:
          win,winner,turn = True,'X',0
     elif docount == 3:
          win,winner,turn = True,'O',0
             
     dxcount = docount = 0

     # Positive Diagonal 
     x = 2 
     for row in filled:
          if row[x] == 'X':
               dxcount+= 1
          elif row[x] == 'O':
               docount += 1
          x -= 1

     if dxcount == 3:
          win,winner,turn = True,'X',0
     elif docount == 3:
          win,winner,turn = True,'O',0
               

     return [win,winner,turn,dxcount,docount]


def Fcheck (filled):
     global win
     global winner
     global turn
     if filled[0].count('n') == 0 and filled[1].count('n') == 0 and filled[2].count('n') == 0:
          win = True
          winner = 'None'
          turn = 0
     return [win,winner,turn]

squares = {"1" : [-100,75], "2" : [0,75], "3" : [100,75],
           "4" : [-100,-25], "5" : [0,-25], "6" : [100,-25],
           "7" : [-100,-125], "8" : [0,-125], "9" : [100,-125]}

coords = {'1':(0,0),'2':(0,1),'3':(0,2),
          '4':(1,0),'5':(1,1),'6':(1,2),
          '7':(2,0),'8':(2,1),'9':(2,2)}

filled = [['n','n','n'],
          ['n','n','n'],
          ['n','n','n']]

game = True

while game == True:

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
          
             # Player 1
             while turn == 1:

                  place1 = input(f"Player 1, where will you place your {p1} ? (Choose a number). ")

                  if place1.isnumeric()==False:
                      print("Try again")
                      continue
                  elif int(place1)>9 or int(place1)<1:
                      print('Try again')

                  elif filled[coords[place1][0]][coords[place1][1]] != 'n':
                       print('Spot already taken!')
                       continue
                  elif p1=='X':
                       X(squares[place1][0],squares[place1][1])
                       filled[coords[place1][0]][coords[place1][1]]='X'
                  else:
                       O(squares[place1][0],squares[place1][1]-20)
                       filled[coords[place1][0]][coords[place1][1]]='O'
                  turn = 2


             Hcheck(filled)
             Dcheck(filled)
             Vcheck(filled)
             if win == True:
               break
             Fcheck(filled)
             if win == True:
               break  
               
             # Player 2     
             while turn == 2:

                  place2 = input(f"Player 2, where will you place your {p2} ? (Choose a number). ")
                  if place2.isnumeric()==False:
                       print("Try again")
                       continue
                  elif int(place2)>9 or int(place1)<1:
                       print('Try again')
                       continue
                 
                  elif filled[coords[place2][0]][coords[place2][1]] != 'n':
                       print('Spot already taken!')
                       continue
                  elif p2=='X':
                       X(squares[place2][0],squares[place2][1])
                       filled[coords[place2][0]][coords[place2][1]]='X'
                  else:
                       O(squares[place2][0],squares[place2][1]-20)
                       filled[coords[place2][0]][coords[place2][1]]='O'
                  turn = 1
                  
             Hcheck(filled)
             Dcheck(filled)
             Vcheck(filled)
             if win == True:
               break 
             Fcheck(filled)
             if win == True:
               break 
                  
                  
     
     elif players==1:
        p1 = input("X or O? ").upper()
        if p1 == 'X':
            cpu = 'O'
        elif p1 == 'O':
          cpu = 'X'
        else:
          print("Error")
          continue
        while win==False: 
          
             # Player 1
             while turn == 1:

                  place1 = input(f"Player 1, where will you place your {p1} ? (Choose a number). ")

                  if place1.isnumeric()==False:
                      print("Try again")
                      continue
                  elif int(place1)>9 or int(place1)<1:
                      print('Try again')

                  elif filled[coords[place1][0]][coords[place1][1]] != 'n':
                       print('Spot already taken!')
                       continue
                  elif p1=='X':
                       X(squares[place1][0],squares[place1][1])
                       filled[coords[place1][0]][coords[place1][1]]='X'
                  else:
                       O(squares[place1][0],squares[place1][1]-20)
                       filled[coords[place1][0]][coords[place1][1]]='O'
                  turn = 2


                           
             Hcheck(filled)
             Dcheck(filled)
             Vcheck(filled)


             if win == True:
               break  
               
             # Player 2     
             while turn == 2:

                  place2 = str(random.randint(1,9))

                  if filled[coords[place2][0]][coords[place2][1]] != 'n':
                       continue
                  elif cpu =='X':
                       X(squares[place2][0],squares[place2][1])
                       filled[coords[place2][0]][coords[place2][1]]='X'
                  else:
                       O(squares[place2][0],squares[place2][1]-20)
                       filled[coords[place2][0]][coords[place2][1]]='O'
                  turn = 1
                  
             Hcheck(filled)
             Dcheck(filled)
             Vcheck(filled)

             if win == True:
               break 
	  
     else:
        print("Only 2 players allowed")
        continue

     if winner == 'X' or winner == 'O':
          print(f"Congratulations! {winner} is the winner!\n\n\n\n\n")
     elif winner == 'None':
          print("It's a tie")
     game = False