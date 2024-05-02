import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random


CAR_LIST = ["car1", "car2", "car3", "car4", "car5", "car6", "car7"]
easy1_level = 8
easy2_level = 7
easy3_level = 6
normal1_level = 5
normal2_level = 4
hard_level = 3
extrime_level = 2

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#set up player
player = Player()


# Set up scoreboard
scoreboard = Scoreboard()

#set up the car
car = CarManager(scoreboard)

#set up gameplay moving
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.make_car()
    car.drive()
    
    #Detect when our cars is hit the player
    for cars in car.all_cars:
        if player.distance(cars) < 20:
            scoreboard.game_over()
            game_is_on = False 
    
    if player.ycor() > 250:
        scoreboard.scoring()
        player.restart()
        
    


# exit
screen.exitonclick()
