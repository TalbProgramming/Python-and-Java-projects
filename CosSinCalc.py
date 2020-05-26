#add to all the functions a self parameer 
#make a function that draws the triangle 
import math
import turtle

class eli():
    def __init__(self):
        self.nearSide = 0
        self.farSide = 0
        self.angle = 0
        self.hypotenuse = 0
        self.farSidelength = 0
        self.nearSidelength = 0
        self.functionType = ""
        self.ans = 0
        self.hypotenuselength = 0
        self.x = 0#temporary variables
        self.y = 0
        self.z = 0 
        
    def chooseFunc(self):
        self.functionType = input("(cos,sin or tan) \nwhats the function you want to use:")
        if self.functionType == "cos":
            self.functionType = "cos"
            self.ans = self.calcCos()
        elif self.functionType == "sin":
            self.functionType = "sin"
            self.ans = self.calcSin()
        elif self.functionType == "tan":
            self.functionType = "tan"
            self.ans = self.calcTan()
        print(self.ans)            
    def calcCos(self):
        inp = input("what do you want to find out?(Y = רתי,S = עלצ,A =תיווז):")

        if inp == "Y":#hypotenuse
            #getting inputs
            self.angle = float(input("Enter the angle: "))
            self.angle = math.cos(self.angle)
            #self.angle = math.degrees(self.angle)
            self.nearSide = float(input("Enter the side length: "))
            self.hypotenuse = self.nearSide/self.angle
            self.farSide = math.sqrt((math.pow(self.hypotenuse,2) - math.pow(self.nearSide,2)))
            return self.hypotenuse
        elif inp == "S":#side
            self.angle = float(input("Enter the angle: "))
            self.angle = math.cos(self.angle)
            self.angle = math.degrees(self.angle)
            self.hypotenuse = float(input("Enter the big side length: "))
            self.nearSide = self.hypotenuse*self.angle
            self.farSide = math.sqrt((math.pow(self.hypotenuse,2) - math.pow(self.nearSide,2)))
            return self.nearSide
        elif inp == "A":#angle
            self.nearSide = float(input("Enter the side length: "))
            self.hypotenuse = float(input("Enter the big side length: " ))
            self.angle = math.acos(self.nearSide/self.hypotenuse)
            self.angle = math.degrees(self.angle)
            self.farSide = math.sqrt((math.pow(self.hypotenuse,2) - math.pow(self.nearSide,2)))
            return self.angle

    def calcSin(self):
        inp = input("what do you want to find out?(Y = רתי,S = עלצ,A =תיווז):")

        if inp == "Y":#hypotenuse
            self.angle = float(input("Enter the angle: "))
            self.angle = math.sin(self.angle)
            self.angle = math.degrees(self.angle)
            self.farSide = float(input("Enter the side length: "))
            self.hypotenuse = self.farSide/self.angle
            self.nearSide = math.sqrt((math.pow(self.hypotenuse,2) - math.pow(self.farSide,2)))
            return self.hypotenuse
        elif inp == "S":#side
            self.angle = float(input("Enter the angle: "))
            self.angle = math.sin(self.angle)
            self.angle = math.degrees(self.angle)
            self.hypotenuse = float(input("Enter the hypotenuse: " ))
            self.farSide = self.angle*self.hypotenuse
            self.nearSide = math.sqrt((math.pow(self.hypotenuse,2) - math.pow(self.farSide,2)))
            return self.farSide
        elif inp == "A":#angle
            self.farSide = float(input("Enter the side length: "))
            self.hypotenuse = float(input("Enter the hypotenuse length"))
            self.angle = math.asin(self.farSide/self.hypotenuse)
            self.angle = math.degrees(self.angle)
            self.nearSide = math.sqrt((math.pow(self.hypotenuse,2) - math.pow(self.farSide,2)))
            return self.angle

    def calcTan(self):
        inp = input("what do you want to find out?(F = far side, N = near side, A= angle): ")

        if inp == "F":#Far side
            self.nearSide = float(input("Enter the near side length: "))
            self.angle = float(input("Enter the angle: "))
            self.angle = math.tan(self.angle)
            #self.angle = math.degrees(self.angle)
            self.farSide = self.nearSide*self.angle
            self.hypotenuse = math.sqrt((math.pow(self.farSide,2) + math.pow(self.nearSide,2)))
            return self.farSide
        elif inp == "N":#near side
            self.farSide = float(input("Enter the far side length: "))
            self.angle = float(input("Enter the angle: "))
            self.angle = math.tan(self.angle)
            #self.angle = math.degrees(self.angle)
            self.nearSide = self.farSide/self.angle
            self.hypotenuse = math.sqrt((math.pow(self.farSide,2) + math.pow(self.nearSide,2)))
            return self.nearSide
        elif inp == "A":#angle
            self.farSide = float(input("Enter the far side length: "))
            self.nearSide = float(input("Enter the near side length: "))
            self.angle = math.atan(self.farSide/self.nearSide)
            self.angle = math.degrees(self.angle)
            self.hypotenuse = math.sqrt((math.pow(self.farSide,2) + math.pow(self.nearSide,2)))
            self.x = self.nearSide
            self.nearSide = self.farSide
            self.farSide = self.x
            return self.angle        

    def drawTriangle(self):
        t = turtle.Turtle()
        t.pensize(10)
        t.speed(1)
        t.penup()
        t.goto(-25,-100)
        t.pendown()
        t.forward(self.nearSide*10)
        t.left(90)
        t.forward(self.farSide*10)
        t.left(90)
        t.left(90-self.angle)
        t.forward(self.hypotenuse*10)
            

            
            




e1=eli()
e1.chooseFunc()
print(e1.nearSide,e1.farSide,e1.hypotenuse,e1.angle)
e1.drawTriangle()



