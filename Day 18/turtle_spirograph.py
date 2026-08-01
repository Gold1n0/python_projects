from turtle import Turtle
from turtle import Screen
import random

angle_shift = int (input("Decide on angle shift "))

screen = Screen()
screen.colormode(255)
turtle = Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_col = (r,g,b)
    return random_col

turtle.speed("fastest")

angle = 0
rotation = int (360 / angle_shift)

for i in range (rotation):
    turtle.color(random_color())
    turtle.circle(100)
    turtle.setheading(angle)
    angle += angle_shift

screen.exitonclick()