import math
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
inSquare = (math.pow(b,2) - (4*a*c))
if (inSquare >= 0):
    inSquare = math.sqrt(inSquare)    
    tempB = -b
    x1 = (tempB + inSquare)/(2*a)
    x2 = (tempB - inSquare)/(2*a)
    print("x1 = " + str(x1) + "\n" + "x2 = " + str(x2))
else:
    print("the number below the square is negative.") 