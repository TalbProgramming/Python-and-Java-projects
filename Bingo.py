#bingo
#importing
import keyboard  # using module keyboard
import time

import turtle
t=turtle.Turtle()
import random
#the winning variables
win = False 
GameOver = False
#the function that checks if theres a bingo
def Player_Win(list1,list2):

    if (((list1[0] in list2) and (list1[1] in list2) and (list1[2] in list2) and (list1[3] in list2)) or ((list1[4] in list2) and (list1[5] in list2) and (list1[6] in list2) and (list1[7] in list2)) or ((list1[8] in list2) and (list1[9] in list2) and (list1[10] in list2) and (list1[11] in list2)) or ((list1[12] in list2) and (list1[13] in list2) and (list1[14] in list2) and (list1[15] in list2))):
        return True
    
    elif (((list1[0] in list2) and (list1[7] in list2) and (list1[8] in list2) and (list1[15] in list2)) or ((list1[1] in list2) and (list1[6] in list2) and (list1[9] in list2) and (list1[14] in list2)) or ((list1[2] in list2) and (list1[5] in list2) and (list1[10] in list2) and (list1[13] in list2)) or ((list1[3] in list2) and (list1[4] in list2) and (list1[11] in list2) and (list1[12] in list2))):
        return True
    
    elif ((list1[0] in list2) and (list1[6] in list2) and (list1[10] in list2) and (list1[12] in list2)) or ((list1[3] in list2) and (list1[5] in list2) and (list1[9] in list2) and (list1[15] in list2)):
        return True

#the function that check if u won
def Game_End(lst1,lst2):
    lst1,lst2 = set(lst1),set(lst2) 
    if lst1 == lst2:
        return True

#the bingo variable list
VarList = []
ChartList = []

for i in range(0,10):
    VarList.append("R" + str(i))
    VarList.append("T" + str(i))
    VarList.append("H" + str(i))
    VarList.append("E" + str(i))
    VarList.append("L" + str(i))
#the list i would roll from
VarFrom = tuple(VarList)       
#taking input for their chart
for j in range(1,17):
    RC = random.choice(VarList)
    VarList.remove(RC)
    ChartList.append(RC)  
 
############################################################################################

t.hideturtle()
t.speed(10)
#Making  a 4*4 chart
t.pensize(10)
t.penup()
t.goto(200,200)
t.pendown()
for i in range(4):
    t.right(90)
    t.forward(400)
#first lines
t.left(180)
t.forward(100)
t.left(90)
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.left(90)
t.forward(100)
t.left(90)
t.forward(400)
#second lines
t.left(90)
t.forward(300)
t.left(90)
t.forward(100)    
t.left(90)
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.left(90)
t.forward(100)
t.left(90)
t.forward(400)
#adding the words to the chart
style = ('ariel',20,'italic')
t.penup()
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.pendown()
t.write(ChartList[0],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[1],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[2],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[3],font = style,align='center')
#going down a line
t.penup()
t.right(90)
t.forward(100)
t.right(90)

t.pendown()
t.write(ChartList[4],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[5],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[6],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[7],font = style,align='center')

#going down a line again
t.penup()
t.left(90)
t.forward(100)
t.left(90)

t.pendown()
t.write(ChartList[8],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[9],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[10],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[11],font = style,align='center')
#going downa a line
t.penup()
t.right(90)
t.forward(100)
t.right(90)

t.pendown()
t.write(ChartList[12],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[13],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[14],font = style,align='center')

t.penup()
t.forward(100)
t.pendown()
t.write(ChartList[15],font = style,align='center')

t.penup()
t.forward(50)
t.left(90)
t.forward(50)
t.left(180)
#printing the instructions
t.goto(0,220)
t.write("Press 'l' to roll!",font = style, align = 'center')
#####################################################################################################
#making the roll hotkey
def Roll_Word(lst):
    while True:  # making a lool
            if keyboard.read_key() == 'L' or 'l':  # if key 'q' is pressed 
                var = random.choice(lst)
                return var
#red color for 'X's
t.color("red")
t.speed(5)


#win checking list
WinList = []
#instead of removing an item from a list lets just create another list and then put its index in there and then its easy to see who wins...    
VarFrom = list(VarFrom)#doing it so i can remove from it

while GameOver == False:
    #RandWord = random.choice(VarFrom)#a random item from the 50 item lists
    RandWord = Roll_Word(VarFrom)
    print(RandWord)
    if RandWord in ChartList: # if the item we rolled is in the chart...
        #printing 'is in' and 'isnt in'.
    
        
        
        #drawing a 'X' on the word statements
        #######################################################################
        
        pos = ChartList.index(RandWord)#the index of the item
        VarFrom.remove(RandWord)#remove it from the big list
        WinList.append(RandWord)#adding to the win checking list for later
            
        if pos == 0:
            t.goto(-200,100)#important goto point
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)            
            t.penup()        
        elif pos == 1:
            t.goto(-100,100)#important goto point
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 2:
            t.goto(0,100)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 3:
            t.goto(100,100)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 7:
            t.goto(-200,0)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 6:
            t.goto(-100,0)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 5:
            t.goto(0,0)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)                
            t.penup()
        elif pos == 4:
            t.goto(100,0)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 8:
            t.goto(-200,-100)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 9:
            t.goto(-100,-100)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421) 
            t.penup()               
        elif pos == 10:
            t.goto(0,-100)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 11:
            t.goto(100,-100)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 15:
            t.goto(-200,-200)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)                
            t.penup()
        elif pos == 14:
            t.goto(-100,-200)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()                
        elif pos == 13:
            t.goto(0,-200)  
            t.setheading(360)
            t.left (45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()
        elif pos == 12:
            t.goto(100,-200)
            t.setheading(360)
            t.left(45)
            t.pendown()
            t.forward(141.421)
            t.penup()
            t.right(135)
            t.forward(100)
            t.right(135)
            t.pendown()
            t.forward(141.421)
            t.penup()        
    if Player_Win(ChartList,WinList) == True:
        t.goto(-250,220)
        BingoFont = ('arial',30,'italic')
        t.write('Bingo!',font = BingoFont,align = 'center')
        win = True
    if Game_End(ChartList,WinList) == True:
        t.goto(0,-50)
        GOstyle = ('arial',80,'italic')
        t.color('blue')
        t.write('Game Over!',font = GOstyle,align='center')
        time.sleep(2)
        print("Game Over!")             
        GameOver = True        

#the actual loop of the game
#drawing a 'X' on the word statements
    #######################################################################
    #First line
    