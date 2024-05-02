COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager:
    
    def __init__(self):
        self.all_cars = []  
    
    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=0.5, stretch_len=1)
            new_car.goto(300, random.randint(-200,200))
            new_car.setheading(180)
            self.all_cars.append(new_car)
        
        
    def drive(self):
        for cars in self.all_cars:
            cars.forward(MOVE_INCREMENT)
