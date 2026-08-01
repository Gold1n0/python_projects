from turtle import Turtle
from turtle import Screen

turtle = Turtle()
screen = Screen()

def draw_forward():
    turtle.forward(10)

def draw_backward():
    turtle.back(10)

def turn_counter_clockwise():
    new_heading = turtle.heading() + 10
    turtle.setheading(new_heading)

def turn_clockwise():
    new_heading = turtle.heading() - 10
    turtle.setheading(new_heading)

def clear():
    turtle.clear()
    turtle.setheading(90)
    turtle.penup()
    turtle.goto(0,0)
    turtle.pendown()

screen.listen()
screen.onkeypress(key = "w", fun = draw_forward)
screen.onkeypress(key = "s", fun = draw_backward)
screen.onkeypress(key = "a", fun= turn_counter_clockwise)
screen.onkeypress(key = "d", fun = turn_clockwise)
screen.onkeypress(key = "c", fun = clear)
screen.exitonclick()