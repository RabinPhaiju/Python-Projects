import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800,height=600)
screen.title('Turtle Race')
screen.tracer()
screen.bgcolor('black')
screen.listen()
screen.tracer(0)

player = Player()
speed = 0
car = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.onkey(player.move,' ')

    for i in range(10):
        car.cars[i].forward(random.randint(1,50)+speed)
        if car.cars[i].xcor()<-300:
            car.cars[i].goto(360,car.cars[i].ycor())
        if player.ycor()>290:
            player.down()
            print('win')
            scoreboard.set_score()
            scoreboard.show()
            speed +=5
        if player.distance(car.cars[i])<20:
            print('loose')
            scoreboard.finish()
            game_is_on = False


screen.exitonclick()