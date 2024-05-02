COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.make_car()
        
    
    def make_car(self):
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=1)
        self.goto(300, random.randint(-200,200))
        self.setheading(180)
        
        
    def drive(self):
        self.forward(MOVE_INCREMENT)
