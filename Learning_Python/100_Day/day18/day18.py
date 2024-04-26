from turtle import Turtle, Screen
import turtle
import random

tono = Turtle()
tono.shape("turtle")
tono.color("green", "yellow")
turtle.colormode(255)

# challenge 1 ## make a square
def make_square():
    for i in range(0, 4):
        tono.pencolor("pink")
        tono.forward(100)
        tono.left(90)

# challenge 2
def make_dash_line():
    for i in range(10):
        tono.forward(10)
        tono.pd()
        tono.forward(10)
        tono.pu()
#make_dash_line()

# challenge 3
# draw a triangle, square, pentagon, hexagon, heptagon, octagon
# nonagon, and decagon
# each shapes have random color and each side is 100 len

def make_triangle():
    for i in range(3):
        tono.pencolor("red")
        tono.forward(100)
        tono.left(120)
        
def make_pentagon():
    for i in range(5):
        tono.pencolor("green")
        tono.forward(100)
        tono.left(72)

def make_hexagon():
    for i in range(6):
        tono.pencolor("blue")
        tono.forward(100)
        tono.left(60)

def make_heptagon():
    for i in range(7):
        tono.pencolor("purple")
        tono.forward(100)
        tono.left(51.43)

def make_octagon():
    for i in range(8):
        tono.pencolor("yellow")
        tono.forward(100)
        tono.left(45)
        
def make_nonagon():
    for i in range(9):
        tono.pencolor("brown")
        tono.forward(100)
        tono.left(40)

def make_decagon():
    for i in range(10):
        tono.pencolor("grey")
        tono.forward(100)
        tono.left(36)

def wipe():
    tono.pencolor("white")
    tono.forward(100)

def make_the_shapes():
    make_triangle()
    make_square()
    make_pentagon()
    make_hexagon()
    make_heptagon()
    make_octagon()
    make_nonagon()
    make_decagon()

#make_the_shapes()
#wipe()


# Challenge 4
# Draw a random walk
moving = ["forward", "backward"]
corner = ["left", "right"]
colours = ["red", "green", "yellow", "blue", "purple", "brown", "black"]

def random_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_rgb = (r, g, b)
    return random_rgb

def random_walk():
    for i in range(1000):
        random_rgb()
        tono.pensize(15)
        tono.speed(150)
        tono.pencolor(random_rgb())
        random_move = random.choice(moving)
        random_corner = random.choice(corner)
        if random_move == "forward" and random_corner == "left":
            tono.forward(random.randint(10, 50))
            tono.left(90)
        elif random_move == "forward" and random_corner == "right":
            tono.forward(random.randint(10, 50))
            tono.right(90)
        elif random_move == "backward" and random_corner == "left":
            tono.backward(random.randint(10, 50))
            tono.left(90)
        elif random_move == "backward" and random_corner == "right":
            tono.backward(random.randint(10, 50))
            tono.right(90)
    
random_walk()

screen = Screen()
screen.exitonclick()


# try to use package that doesn't exist before installing
import heroes
#print(heroes.gen())

