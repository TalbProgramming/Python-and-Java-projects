import turtle

a=float(input("a: "))
b=float(input("b: "))
c=float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
hezka1 = float(input("exsponent 1: "))
hezka2 = float(input("exsponent 2: "))
hezka3 = float(input("exsponent 3: "))
hezka4 = float(input("exsponent 4: "))
#מערכת צירים
t=turtle.Turtle()
t.penup()
t.goto(-600,0)
t.pensize(10)
t.pendown()
t.forward(1200)
t.penup()
t.goto(0,600)
t.pendown()
t.right(90)
t.forward(1200)

t.pencolor("red")
if hezka1 == 3:
    x=-20.0
if hezka1 == 2:
    x=-50    
if hezka1 == 4:
    x=-10    
t.speed(100)
t.penup()
y = (x**hezka1)*a + (x**hezka2)*b + (x**hezka3)*c + d
t.goto(x*10,y)
t.pendown()    
while x <= 400.0:
    y = (x**hezka1)*a + (x**hezka2)*b + (x**hezka3)*c + (x**hezka4)*d + e
    t.goto(x*10,y)
    x+=0.2
