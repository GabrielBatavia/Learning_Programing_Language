from turtle import Turtle, Screen
import time
game_on = True

# setting the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# set the snake

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

# create the snake body
for position in starting_positions:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.up()
    snake.goto(position)
    segments.append(snake)

while game_on:
    for seg in segments:
        seg.forward(100)
        seg.left(90)
        screen.update()
        time.sleep(1)








 

























# set up the exit screen in bottom of our code
screen.exitonclick()