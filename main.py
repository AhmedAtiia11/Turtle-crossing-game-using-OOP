import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def move():
    timmy.forward(10)

#screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(move,"Up")

#Variables decleration
speed=.1
timmy=Player()
obstacle=CarManager()
score=Scoreboard()
game_is_on = True

while game_is_on:
    obstacle.create_car()
    obstacle.move_car()
    screen.update()
    time.sleep(speed)
    if timmy.ycor() > 250:
        print("Level Up")
        score.update()
        timmy.starting_position()
        speed*=.9
        print(speed)
    for car in obstacle.allcars:    
        if timmy.distance(car) < 20:
            score.game_over()
            game_is_on=False
    
screen.exitonclick()    