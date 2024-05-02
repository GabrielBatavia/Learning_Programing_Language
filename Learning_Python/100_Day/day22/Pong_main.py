from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Score
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

# set up score
score = Score()


# make a move
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



# set up main 
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    
    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Detect whena paddle misses and add score
    if ball.xcor() > 360:
        score.l_point()
        ball.reset_positions()
    elif ball.xcor() < -360:
        score.r_point()
        ball.reset_positions()
    








# set up the exit screen in bottom of our code
screen.exitonclick()