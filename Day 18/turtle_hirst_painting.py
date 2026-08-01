from turtle import Turtle
from turtle import Screen
import random

screen = Screen()
screen.colormode(255)
screen.setup(width= 500, height = 500)
turtle = Turtle()

width = screen.window_width()
height = screen.window_height()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_col = (r,g,b)
    return random_col
turtle.speed("fastest")
turtle.hideturtle()

turtle.penup()
turtle.goto(-width/2 + 20, -height/2 + 20)
turtle.pendown()

for i in range(110):
    turtle.dot(20, random_color())
    turtle.penup()
    
    if turtle.xcor() > width/2 - 20:
        turtle.goto(-width/2 + 20, turtle.ycor() + 50)
    else:
        turtle.forward(50)

    turtle.pendown()
    

screen.exitonclick()