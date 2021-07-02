from turtle import *
bgcolor('black') 
shape("turtle")

colors = ["red", "green", "blue", "yellow", "orange", "purple"]
pensize(5)

for x in range(0, 150):
    color(colors[x % len(colors)])

    forward(x * 2)
    left(59)



exitonclick()


