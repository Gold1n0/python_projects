from turtle import Turtle
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

turtle = Turtle()
screen = Screen()
screen.setup(width = 600, height = 600)
turtle.speed("fastest")
screen.bgcolor("black")
screen.title("snek")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

game_state = True

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while game_state == True:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        turtle.color("white")
        turtle.write("Game Over", align="center", font=("Arial",24,"normal"))
        game_state = False

    for segments in snake.segments:
        if segments == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segments) < 10:
            turtle.color("white")
            turtle.write("Game Over", align="center", font=("Arial",24,"normal"))
            game_state = False
            

screen.exitonclick()