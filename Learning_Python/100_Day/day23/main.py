import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

CAR_LIST = ["car1", "car2", "car3", "car4", "car5", "car6", "car7"]

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#set up player
player = Player()


#set up the car
car = CarManager()

# Set up scoreboard
scoreboard = Scoreboard()

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
    


# exit
screen.exitonclick()
