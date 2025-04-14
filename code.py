#Zadacha
import math

pi = math.pi
x = -2*pi
Q = 0

while x < 2*pi:
    if x < pi/4:
        Q = math.cos(x)
        print("----------")
    else:
        Q = math.sin(x)
        print("----------")
    print("Q= ", round(Q,2))
    print("x= ", round(x,2))
    x += pi/12
print("==============================")
