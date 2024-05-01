from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
game_is_on = True

# set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

# set up the paddle
l_paddle = Paddle()
r_paddle = Paddle()

l_paddle.goto(-350, 0)
r_paddle.goto(350, 0)

# set up the ball
ball = Ball()


# make a move
screen.listen()
screen.onkey(l_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "Down")


# set up main 
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()
    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()










# set up the exit screen in bottom of our code
screen.exitonclick()