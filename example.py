from turtle import *
speed(0)
bgcolor('black') 
color('red', 'yellow')
for _ in range(0, 4):
    begin_fill()
    while True:
        forward(300)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()
    left(90)

exitonclick()