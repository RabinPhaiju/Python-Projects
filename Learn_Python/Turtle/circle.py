from turtle import Turtle, Screen
import random

t1 = Turtle()


t1.speed(20)
for i in range(200):
    t1.color((random.random(),random.random(),random.random(),))
    t1.circle(140)
    t1.right(5)
   



screeen = Screen()
screeen.exitonclick()