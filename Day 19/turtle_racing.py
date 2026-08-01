from turtle import Turtle
from turtle import Screen
import random

red = Turtle()
green = Turtle()
yellow = Turtle()
blue = Turtle()
purple = Turtle()
orange = Turtle()
screen = Screen()

screen.setup(width=500, height=400)

width = screen.window_width()
height = screen.window_height()

start_x = (-width / 2) + 20
finish_x = (width / 2) - 20

turtles = [red, green, yellow, blue, purple, orange]
colors = ["red", "green", "yellow", "blue", "purple", "orange"]
y_positions = [100, 50, 0, -50, -100, -150]

for turtle, color, y in zip(turtles, colors, y_positions):
    turtle.penup()
    turtle.goto(x=start_x, y=y)
    turtle.shape("turtle")
    turtle.color(color)

user_guess = screen.textinput(
    title="Make your bet!",
    prompt="Which turtle will win the race? Pick between Red, Green, Yellow, Blue, Purple, Orange!"
)
user_guess = user_guess.lower()

is_race_on = True

while is_race_on:
    for t in turtles:
        speed = random.randint(1, 10)
        t.forward(speed)

        if t.xcor() > finish_x:
            is_race_on = False
            winner_color = t.pencolor()
            break
print(f"The {winner_color} turtle wins!")

if user_guess == winner_color:
    print(f"You guessed {user_guess} and you were correct! You win!")
else:
    print(f"You guessed {user_guess}, but the winner was {winner_color}. You lose!")

screen.exitonclick()