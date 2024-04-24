# oop
import another_module
print(another_module.another_variable)

from turtle import Turtle, Screen
# make object
tono = Turtle()
print(tono)
tono.shape("turtle")
tono.color("green", "blue")
tono.forward(200)

# screen is object
my_screen = Screen()
print(my_screen.canvheight) # canvheight is atribut

my_screen.exitonclick() # exitonclick is method
