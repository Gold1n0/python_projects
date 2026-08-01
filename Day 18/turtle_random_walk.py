from turtle import Turtle
from turtle import Screen
import random

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.speed(3)

for i in range(100):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    angles = [90,180,270,0]
    angle = random.choice(angles)

    turtle.color(r,g,b)
    turtle.pensize(10)
    turtle.forward(30)
    turtle.setheading(angle)

screen.exitonclick()