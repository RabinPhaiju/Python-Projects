from turtle import Turtle, Screen
import random

screen = Screen()

border = Turtle()
border.pensize(20)
border.speed(1500)
border.setheading(220)
border.penup()
border.forward(580)
border.pendown()
border.setheading(0)
border.color('blue')
for _ in range(4):
    for i in range(20):
        border.forward(38)
    border.left(90)

   


turtles = [Turtle(),Turtle(),Turtle(),Turtle(),Turtle(),Turtle()]
colors = ['pink','blue','green','yellow','brown','red','grey']
tu = [0,0,0,0,0,0]

for i,tur in enumerate(turtles):
    tur.color('white')
    tur.penup()
    tur.heading()
    tur.setheading(200)
    tur.speed(500)
    tur.forward(350)
    tur.setheading(0)

    tur.color(colors[i])
    tur.shape("turtle")
    tur.left(90)
    tur.forward(i*50)
    tur.right(90)

user_bet = screen.textinput(title='Make your bet',
prompt=' Which turtle wins')

for _ in range(24):
    for i,tur in enumerate(turtles):
        go = random.random()*50
        tu[i] += go
        tur.speed(10)
        tur.forward(go)
    
win = tu.index(max(tu))
print('Turtle ',win+1,' wins')
print(user_bet)
if win+1 == user_bet:
    print('You win the bet')
else:
    print('Your loose the bet')

screen.exitonclick()