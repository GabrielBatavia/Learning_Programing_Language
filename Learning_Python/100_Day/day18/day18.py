from turtle import Turtle, Screen

tono_the_turtle = Turtle()
tono_the_turtle.shape("turtle")
tono_the_turtle.color("green", "yellow")

# challenge 1 ## make a square
tono_the_turtle.forward(100)
tono_the_turtle.left(90)
tono_the_turtle.forward(100)
tono_the_turtle.left(90)
tono_the_turtle.forward(100)
tono_the_turtle.left(90)
tono_the_turtle.forward(100)
tono_the_turtle.left(90)

screen = Screen()
screen.exitonclick()