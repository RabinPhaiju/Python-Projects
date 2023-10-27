import turtle as turtle_module
from os import close
import colorgram
import random

rgb_colors = []
colors = colorgram.extract('./Learn_Python/Turtle/image.jpg', 20)
for color in colors:
    rgb_colors.append((color.rgb.r,color.rgb.g,color.rgb.b))

print(rgb_colors[0])

t1 = turtle_module.Turtle()
turtle_module.colormode(255)
t1.color('white')
t1.hideturtle()
t1.setheading(220)
t1.speed(300)
t1.forward(530)
t1.setheading(0)
t1.penup()

for i in range(15):
    t1.speed(8)
    for _ in range(16):
        t1.dot(40,random.choice(rgb_colors))
        t1.forward(50)
    
    t1.dot(40,random.choice(rgb_colors))
    t1.speed(200)
    t1.setheading(90)
    t1.forward(50)
    t1.setheading(180)
    t1.forward(800)
    t1.setheading(0)



screeen = turtle_module.Screen()
screeen.exitonclick()