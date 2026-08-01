from turtle import Turtle
from turtle import Screen
import random

turtle = Turtle()
screen = Screen()
screen.colormode(255)

turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
for i in range(3):
    turtle.forward(100)
    turtle.right(120)

turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
for i in range(4):
    turtle.forward(100)
    turtle.right(90)

turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
for i in range(5):
    turtle.forward(100)
    turtle.right(72)

turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
for i in range(6):
    turtle.forward(100)
    turtle.right(60)

turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
for i in range(7):
    turtle.forward(100)
    turtle.right(51.42)

turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
for i in range(8):
    turtle.forward(100)
    turtle.right(45)

turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
for i in range(9):
    turtle.forward(100)
    turtle.right(40)

turtle.color(random.randint(0,255), random.randint(0,255), random.randint(0,255))
for i in range(10):
    turtle.forward(100)
    turtle.right(36)

screen.exitonclick()