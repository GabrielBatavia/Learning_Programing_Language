from turtle import Turtle, Screen

tono = Turtle()
screen = Screen()

def move_forwards():
    tono.forward(10)

def move_backwards():
    tono.backward(10)

def move_left():
    tono.left(10)

def move_right():
    tono.right(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.exitonclick()