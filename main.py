from turtle import *
import random

shape("turtle")
speed(0)
bgcolor("black")  


def tree(size=100, levels=4, angle=30):

    color("brown")

    if levels == 0:
        color("green")
        dot(size)
        color("brown")
        return

    forward(size)
    right(angle)
    

    tree(size * 0.8, levels - 1, angle)

    left(angle * 2)

    tree(size * 0.8, levels - 1, angle)

    right(angle)
    backward(size)

def tree_spiral(num_trees=5, size=100, levels=4, angle=30):
    for x in range(0, num_trees):
        tree(size, levels, angle)
        left(360 / num_trees)

def grass():
    color("green")
    right(45)
    for x in range(0, 3):
        forward(20)
        right(90)
        forward(20)
        left(90)
    right(45)
    forward(20)
    left(90)


def forest(num_trees=5, size=100, levels=5, angle=30):
    grass()
    for x in range(0, num_trees):
        tree(size * random.randrange(5, 12)/10, levels, angle)
        grass()


def snowflake_side(length=300, levels=3):
    if levels == 0:
        forward(length)
        return

    length /= 3.0
    snowflake_side(length, levels-1)
    left(60)
    snowflake_side(length, levels-1)
    right(120)
    snowflake_side(length, levels-1)
    left(60)
    snowflake_side(length, levels-1)

def create_snowflake(sides=3, length=300):
    color("blue")
    begin_fill()
    for _ in range(sides):
        snowflake_side(length, sides)
        right(360 / sides)
    end_fill()

def spiky(size):
    color('red', 'yellow')
    begin_fill()
    while True:
        forward(size)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()

goto(0, 0)
spiky(400)
right(90)
create_snowflake(4, 200)
left(90)
goto(-400,100)
left(90)
forest()
goto(-300,-200)
tree_spiral()



exitonclick()