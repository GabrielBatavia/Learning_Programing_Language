from turtle import Turtle, Screen
game_is_on = True

# set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

# set up the paddle
paddle = Turtle("square")
paddle.color("white")
paddle.penup()
paddle.shapesize(stretch_wid=3, stretch_len=0.5)
paddle.goto(350, 0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

# make a move
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")


# set up main 
while game_is_on:
    screen.update()










# set up the exit screen in bottom of our code
screen.exitonclick()