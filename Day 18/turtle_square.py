from turtle import Turtle
from turtle import Screen

turtle = Turtle()

for i in range(0,4):
    turtle.forward(100)
    turtle.left(90)

screen = Screen()
screen.exitonclick()