from turtle import Screen
import time
from Snake import Snake
game_on = True

# setting the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# set the snake
snake = Snake()


while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()







 

























# set up the exit screen in bottom of our code
screen.exitonclick()