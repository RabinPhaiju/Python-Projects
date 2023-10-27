from turtle import Turtle, Screen

t1 = Turtle()
t1.shape("turtle")
t1.color('blue')
for _ in range(10):
    t1.forward(10)
    t1.pendown()
    t1.forward(10)
    t1.penup()


screeen = Screen()
screeen.exitonclick()