import math
from turtle import *

def heartA(k):
    return 16 * math.sin(k) ** 3

def heartB(k):
    return 13 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)

speed(0)
bgcolor("black")

for i in range(10000):
    x = heartA(i) * 20
    y = heartB(i) * 20
    goto(x, y)
    for j in range(3):
        goto(x, 0)
        color("red")

done()
