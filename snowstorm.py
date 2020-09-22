from turtle import *
import random


shape("classic")
speed(2)
pensize(3)
colours=["blue","purple","cyan","red","yellow","green","orange"]

Screen().bgcolor("dark orchid")

def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)

def snowflakeArm(size):
    for x in range(0,4):
        forward(size)
        vshape(size)
    backward(size*4)

def snowflake(size):
    for x in range(0,6):
        color(random.choice(colours))
        snowflakeArm(size)
        right(60)

for i in range(0,10):
    size=random.randint(5,30)
    x=random.randint(-200,200)
    y=random.randint(-200,200)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)