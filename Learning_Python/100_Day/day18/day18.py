from turtle import Turtle, Screen

tono = Turtle()
tono.shape("turtle")
tono.color("green", "yellow")

# challenge 1 ## make a square
def make_square():
    for i in range(0, 4):
        tono.forward(100)
        tono.left(90)

# challenge 2
def make_dash_line():
    for i in range(10):
        tono.forward(10)
        tono.pd()
        tono.forward(10)
        tono.pu()
    
make_dash_line()

screen = Screen()
screen.exitonclick()


# try to use package that doesn't exist before installing
import heroes
print(heroes.gen())

