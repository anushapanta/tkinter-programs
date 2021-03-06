from turtle import *
import random


shape("classic")
speed(2)
pensize(3)
colours=["blue","purple","cyan","red","yellow","green","orange"]

Screen().bgcolor("dark orchid")

def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)

def snowflakeArm():
    for x in range(0,4):
        forward(30)
        vshape()
    backward(120)

def snowflake():
    for x in range(0,6):
        color(random.choice(colours))
        snowflakeArm()
        right(60)

snowflake()