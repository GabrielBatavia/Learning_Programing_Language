from turtle import Turtle, Screen
import time
game_on = True

# setting the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

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
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num -1].ycor()
        segments[seg_num].goto(new_x, new_y)
    
    segments[0].forward(20)







 

























# set up the exit screen in bottom of our code
screen.exitonclick()