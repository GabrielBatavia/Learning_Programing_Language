from turtle import Turtle, Screen

tono = Turtle()
screen = Screen()

def move_forwards():
    tono.forward(10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.exitonclick()