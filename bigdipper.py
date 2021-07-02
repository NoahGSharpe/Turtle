# Big Dipper 
 
from turtle import *
import random  


bgcolor("darkblue")  
speed(0)  
hideturtle()  
 
def ursamajor(i,j):  
	for k in range(7):  
		lst=["red","green","orange", "yellow","darkgray","brown","lightgreen"] 			 
		color(lst[random.randint(0,6)])  
		forward(i)  
		right(j)  
 
x=-350  
y=-50  
coordinates=((x,y),(x+135,y+1),(x+220,y-50),(x+330,y-105),(x+344,y-188), (x+470,y-209), (x+500,y-123))  
 
def starconnect():  
	for i in range(1):  
		ursamajor(12,144)  
 
for i in coordinates:  
	penup()  
	setpos(i)  
	pendown()  
	starconnect()  
 
hideturtle()  
penup()  
 
for i in coordinates:  
	goto(i)  
	color("yellow")  
	pendown()  
goto(coordinates[-4])  
 
exitonclick() 