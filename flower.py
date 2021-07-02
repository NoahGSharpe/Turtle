from turtle import *
import math 
import colorsys 

bgcolor("black")

phi = 180 * (3 - math.sqrt(5)) 

speed(0) 
 
def square(size): 
    for tmp in range(0,4): 
        forward(size) 
        right(90) 
 
 
num = 200 
 
for x in reversed(range(0, num)): 
    fillcolor(colorsys.hsv_to_rgb(x/num, 1.0, 1.0)) 
    begin_fill() 
    circle(5 + x, None, 11) 
    square(5 + x) 
    end_fill() 
    right(phi) 
    right(.8) 
 
turtle.mainloop() 