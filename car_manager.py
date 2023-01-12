from turtle import Turtle
import random,time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
class CarManager(Turtle):
    def __init__(self):
        self.allcars=[]

        
    def create_car(self):
        reduce_car_num=random.randint(1,6)
        if reduce_car_num==1:   
            car=Turtle("square")
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.setheading(180)
            car.color(random.choice(COLORS))
            car.penup()
            new_x=280
            new_y=random.randint(-250,250)
            car.goto(new_x,new_y)
            self.allcars.append(car)

    def move_car(self):
        for i in self.allcars:
            i.forward(STARTING_MOVE_DISTANCE)
