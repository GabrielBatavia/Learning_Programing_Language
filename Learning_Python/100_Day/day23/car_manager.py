COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random

class CarManager:
    
    def __init__(self, scoreboard):
        self.all_cars = []
        self.scoreboard = scoreboard  # Reference to the scoreboard to access the score

    
    def make_car(self):
        level = self.get_level_based_on_score()
        random_chance = random.randint(1, level)
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
    
    
    def get_level_based_on_score(self):
        score = self.scoreboard.score
        if score < 5:
            return 8  # Easy level
        elif score < 7:
            return 7
        elif score < 10:
            return 6
        elif score < 15:
            return 5  # Normal level
        elif score < 20:
            return 4
        elif score < 30:
            return 3  # Hard level
        else:
            return 2  # Extreme level
