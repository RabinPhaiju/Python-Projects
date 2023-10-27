import turtle
from numpy.core.fromnumeric import sort
import pandas

screen = turtle.Screen()
screen.title("US State Game")

image = 'Learn_Python/File/Tutle_us_state/blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

states = pandas.read_csv('Learn_Python/File/Tutle_us_state/50_states.csv')
state_name = states.state.to_list()
state_pos_x = states.x.to_list()
state_pos_y = states.y.to_list()

count = 0
correct = []

for i in range(50):
    answer_state = screen.textinput(f"{count}/50 correct",prompt='What"s another state name?').title()
    if(answer_state in state_name):
        correct.append(answer_state)
        count  = count+1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_pos_x[i],state_pos_y[i])
        t.write(answer_state)
    else:
        remainning_state = sorted(list(set(state_name)-set(correct)))
        print(remainning_state)
        exit()

turtle.mainloop()

screen.exitonclick()