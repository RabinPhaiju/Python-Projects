from turtle import Turtle,Screen, onkeypress

t1 = Turtle()
t1.right(270)



screen = Screen()

def move_up():
    # t1.setheading(90)
    t1.forward(10)

def move_down():
    # t1.setheading(270)
    t1.backward(10)

def move_left():
    # t1.setheading(180)
    t1.left(20)
    # t1.forward(10)

def move_right():
    # t1.setheading(0)
    t1.right(20)
    # t1.forward(10)

def clear():
    t1.penup()
    t1.clear()
    t1.home()
    t1.pendown()

 
screen.listen()
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="s", fun=move_down)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="w", fun=move_up)
screen.onkeypress(key="c", fun=clear)



screen.exitonclick()