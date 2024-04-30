from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import Score
game_on = True
scors = 0


# setting the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# set the snake
snake = Snake()
food = Food()
scoreboard = Score()

screen.listen() 
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    # detect cllision witg food
    if snake.head.distance(food) < 15:
        scoreboard.scoring()
        food.refresh()
        







 




















# set up the exit screen in bottom of our code
screen.exitonclick()