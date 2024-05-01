from turtle import Screen
from paddle import Paddle
game_is_on = True

# set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

# set up the paddle
paddle = Paddle()


# make a move
screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")


# set up main 
while game_is_on:
    screen.update()










# set up the exit screen in bottom of our code
screen.exitonclick()