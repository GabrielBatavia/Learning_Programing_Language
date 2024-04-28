from turtle import Turtle, Screen

# setting the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")


# create the snake body
snake = Turtle(shape="square")
snake.shapesize(stretch_len=3)
snake.color("white")





 

























# set up the exit screen in bottom of our code
screen.exitonclick()