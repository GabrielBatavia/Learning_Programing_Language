import os
import colorgram
from turtle import Turtle, Screen
import turtle
import random

# Print the current working directory
# print("Current Working Directory: ", os.getcwd())

# extraxt color
#rgb_colors = []
#colors = colorgram.extract('image.jpg', 30)
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r, g, b)
#    rgb_colors.append(new_color)
    
#print(rgb_colors)

color_list = [(229, 162, 72), (234, 238, 244), (47, 111, 154), (229, 243, 238), (208, 126, 166), (21, 129, 97), (110, 158, 206), (229, 200, 98), (148, 21, 60), (9, 175, 144), (173, 163, 35), (170, 48, 88), (218, 78, 115), (127, 110, 163), (27, 35, 83), (121, 174, 125), (226, 86, 46), (41, 165, 
204), (205, 67, 37), (33, 53, 110), (154, 9, 6), (163, 207, 192), (70, 23, 56), (224, 171, 190), (19, 100, 78), (219, 181, 172), (180, 185, 215), (154, 208, 220)]


tono = Turtle()
tono.shape("turtle")
tono.color("green")
turtle.colormode(255)
tono.pensize(20)
tono.speed("fast")
tono.hideturtle()

number_of_dots = 100

def make_the_dots():
    start_position()
    for i in range(1, number_of_dots + 1):
        tono.pencolor(random.choice(color_list))
        tono.pd()
        tono.forward(1)
        tono.pu()
        tono.forward(49)
        
        if i % 10 == 0:
            next_positions()

def start_position():
    tono.pu()
    tono.setheading(255)
    tono.forward(300)
    tono.setheading(0)

def next_positions():
    tono.setheading(90)
    tono.forward(50)
    tono.setheading(180)
    tono.forward(500)
    tono.setheading(0)
    
    

make_the_dots()





screen = Screen()
screen.exitonclick()


