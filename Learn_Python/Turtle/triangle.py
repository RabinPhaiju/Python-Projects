from turtle import Turtle, Screen

t1 = Turtle()

angle = 360
sides = 3
color = ['red','blue','green','grey','brown','yellow','pink']
for i in range(7):
    t1.color(color[i])
    for _ in range(sides):
        t1.forward(100)
        t1.right(angle/sides)
    sides += 1



screeen = Screen()
screeen.exitonclick()