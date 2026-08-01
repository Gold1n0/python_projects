from turtle import Turtle
from turtle import Screen

turtle = Turtle()

for i in range(10):
    turtle.forward(10)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

screen = Screen()
screen.exitonclick()