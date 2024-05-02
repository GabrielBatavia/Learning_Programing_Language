import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



#set up player
player = Player()

#set up the car
for i in range(0, 10):
    car = CarManager()
    for i in range(0, 30):
        car.drive()


#set up gameplay moving
screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    


# exit
screen.exitonclick()
