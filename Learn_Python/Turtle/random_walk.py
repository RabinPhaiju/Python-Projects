from turtle import Turtle, Screen
import random

t1 = Turtle()


direction = [0,90,270]
t1.pensize(4)
t1.speed(3)
for i in range(2000):
    t1.color((random.random(),random.random(),random.random(),))
    t1.forward(40)
    t1.right(random.choice(direction))
   



screeen = Screen()
screeen.exitonclick()