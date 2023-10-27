from turtle import Turtle, pos
import random
COLORS = ['red','orange','yellow','green','blue','purple']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 50

class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
    
    def create_car(self):
        for position in range(10):
            new_car = Turtle('square')
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1,stretch_len=3)
            new_car.setheading(180)
            new_car.goto(360+(random.randint(10,100)*10),-220+(position*MOVE_INCREMENT))
            self.cars.append(new_car)
    
