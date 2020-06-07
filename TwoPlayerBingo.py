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
SecondChartList = []
for i in range(0,10):
    VarList.append("B" + str(i))
    VarList.append("I" + str(i))
    VarList.append("N" + str(i))
    VarList.append("G" + str(i))
    VarList.append("O" + str(i))
#the list i would roll from
VarFrom = tuple(VarList)   
VarList2 = tuple(VarList) # the list for the second board     
#taking input for their chart
for j in range(1,17):
    RC = random.choice(VarList)
    VarList.remove(RC)
    ChartList.append(RC)

VarList2 = list(VarList2)
for d in range(1,17):
    RC = random.choice(VarList2)
    VarList2.remove(RC)
    SecondChartList.append(RC)  

############################################################################################
tempLst = ChartList
t.hideturtle()
t.speed(10)
#Making  a 4*4 chart
xx = -110
yyxx = 25
for x in range(2):
    xx+=100
    t.pensize(10)
    t.penup()
    t.goto(xx,100)
    t.pendown()
    for i in range(4):
        t.right(90)
        t.forward(200)
    #first lines
    t.left(180)
    t.forward(50)
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(200)
    #second lines
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(50)    
    t.left(90)
    t.forward(200)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(200)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(200)
    #adding the words to the chart
    style = ('ariel',15,'italic')
    t.penup()
    t.right(90)
    t.forward(20)
    t.right(90)
    t.penup()
    t.forward(yyxx)
    yyxx-=20
    t.pendown()
    c = 0
    t.write(tempLst[c],font = style,align='center')
    for c in range(1,4):
        t.penup()
        t.forward(50)
        t.pendown()
        t.write(tempLst[c],font = style,align='center')
        
    #going down a line
    t.penup()
    t.right(90)
    t.forward(50)
    t.right(90)

    t.pendown()
    t.write(tempLst[4],font = style,align='center')

    t.penup()
    t.forward(50)
    t.pendown()
    t.write(tempLst[5],font = style,align='center')

    t.penup()
    t.forward(50)
    t.pendown()
    t.write(tempLst[6],font = style,align='center')

    t.penup()
    t.forward(50)
    t.pendown()
    t.write(tempLst[7],font = style,align='center')

    #going down a line again
    t.penup()
    t.left(90)
    t.forward(50)
    t.left(90)

    t.pendown()
    t.write(tempLst[8],font = style,align='center')

    t.penup()
    t.forward(50)
    t.pendown()
    t.write(tempLst[9],font = style,align='center')

    t.penup()
    t.forward(50)
    t.pendown()
    t.write(tempLst[10],font = style,align='center')

    t.penup()
    t.forward(50)
    t.pendown()
    t.write(tempLst[11],font = style,align='center')
    #going downa a line
    t.penup()
    t.right(90)
    t.forward(50)
    t.right(90)

    t.pendown()
    t.write(tempLst[12],font = style,align='center')

    t.penup()
    t.forward(50)
    t.pendown()
    t.write(tempLst[13],font = style,align='center')

    t.penup()
    t.forward(50)
    t.pendown()
    t.write(tempLst[14],font = style,align='center')

    t.penup()
    t.forward(50)
    t.pendown()
    t.write(tempLst[15],font = style,align='center')

    t.penup()
    t.forward(50)
    t.left(90)
    t.forward(50)
    t.left(180)
    tempLst = SecondChartList
#printing the instructions
t.goto(0,220)
t.write("Press 'l' to roll!",font = style, align = 'center')
#####################################################################################################
#making the roll hotkey
def Roll_Word(lst):
    while True:  # making a lool
            if keyboard.read_key() == 'L' or keyboard.read_key() ==  'l':  # if key 'q' is pressed 
                var = random.choice(lst)
                return var
#red color for 'X's
t.color("red")
t.speed(5)


#win checking list
WinList = []
WinList2= []
#instead of removing an item from a list lets just create another list and then put its index in there and then its easy to see who wins...    
VarFrom = list(VarFrom)#doing it so i can remove from it

while GameOver == False:
    #RandWord = random.choice(VarFrom)#a random item from the 50 item lists
    RandWord = Roll_Word(VarFrom)
    print(RandWord)
    VarFrom.remove(RandWord)#remove it from the big list
    if RandWord in ChartList: # if the item we rolled is in the chart...
        #printing 'is in' and 'isnt in'.
    
        pos = ChartList.index(RandWord)#the index of the item
        WinList.append(RandWord)#adding to the win checking list for later
            
        if pos == 0:
            t.goto(-210,50)#important goto point
                    
        elif pos == 1:
            t.goto(-160,50)#important goto point
                            
        elif pos == 2:
            t.goto(-110,50)
                            
        elif pos == 3:
            t.goto(-60,50)
                           
        elif pos == 7:
            t.goto(-210,0)
                            
        elif pos == 6:
            t.goto(-160,0)
                           
        elif pos == 5:
            t.goto(-110,0)
            
        elif pos == 4:
            t.goto(-60,0)
                            
        elif pos == 8:
            t.goto(-210,-50)
                            
        elif pos == 9:
            t.goto(-160,-50)
                          
        elif pos == 10:
            t.goto(-110,-50)
                            
        elif pos == 11:
            t.goto(-60,-50)
                            
        elif pos == 15:
            t.goto(-210,-100)
            
        elif pos == 14:
            t.goto(-160,-100)
                            
        elif pos == 13:
            t.goto(-110,-100)  
            
        elif pos == 12:
            t.goto(-60,-100)

        #paint the X
        t.setheading(360)
        t.left(45)
        t.pendown()
        t.forward(141.421/2)
        t.penup()
        t.right(135)
        t.forward(100/2)
        t.right(135)
        t.pendown()
        t.forward(141.421/2)            
        t.penup()        

    if RandWord in SecondChartList:
        
        pos1 = SecondChartList.index(RandWord)
        WinList2.append(RandWord)

                
        if pos1 == 0:
            t.goto(90,-100)#important goto point
                    
        elif pos1 == 1:
            t.goto(90,-50)#important goto point
                            
        elif pos1 == 2:
            t.goto(90,0)
                            
        elif pos1 == 3:
            t.goto(90,50)
                           
        elif pos1 == 7:
            t.goto(140,-100)
                            
        elif pos1 == 6:
            t.goto(140,-50)
                           
        elif pos1 == 5:
            t.goto(140,0)
            
        elif pos1 == 4:
            t.goto(140,50)
                            
        elif pos1 == 8:
            t.goto(190,-100)
                            
        elif pos1 == 9:
            t.goto(190,-50)
                          
        elif pos1 == 10:
            t.goto(190,0)
                            
        elif pos1 == 11:
            t.goto(190,50)
                            
        elif pos1 == 15:
            t.goto(240,-100)
            
        elif pos1 == 14:
            t.goto(240,-50)
                            
        elif pos1 == 13:
            t.goto(240,0)  
            
        elif pos1 == 12:
            t.goto(240,50)

        #paint the X
        t.setheading(360)
        t.left(45)
        t.pendown()
        t.forward(141.421/2)
        t.penup()
        t.right(135)
        t.forward(100/2)
        t.right(135)
        t.pendown()
        t.forward(141.421/2)            
        t.penup()        
    
    if Player_Win(ChartList,WinList) == True:
        t.goto(-180,110)
        BingoFont = ('arial',20,'italic')
        t.write('Bingo!',font = BingoFont,align = 'center')
        win = True

    if Player_Win(SecondChartList,WinList2) == True:
        t.goto(250,110)
        BingoFont = ('arial',20,'italic')
        t.write('Bingo!',font = BingoFont,align = 'center')
        win = True

    if Game_End(ChartList,WinList) == True:
        t.goto(0,-50)
        GOstyle = ('arial',40,'italic')
        t.color('blue')
        t.write('Player 1 has won!',font = GOstyle,align='center')
        time.sleep(2)
        print("Player 1 has won!")             
        GameOver = True        

    if Game_End(SecondChartList,WinList2) == True:
        t.goto(0,-50)
        GOstyle = ('arial',40,'italic')
        t.color('blue')
        t.write('Player 2 has won!',font = GOstyle,align='center')
        time.sleep(2)
        print("Player 2 has won!")             
        GameOver = True        

#the actual loop of the game
#drawing a 'X' on the word statements
    #######################################################################
    #First line
    