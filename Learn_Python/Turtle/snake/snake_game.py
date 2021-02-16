from turtle import Turtle,Screen
import time
import math
import random
from snake import Snake

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

FOOD_EATEN = 0
food = Turtle()
food.goto(random.randint(-14,14)*20,random.randint(-14,14)*20)
food.dot(20,'green')
food.hideturtle()
food.penup()

display = Turtle('square')
display.goto(-290,285)
display.hideturtle()
display.color('white')
display.fillcolor("white")

with open('./Learn_Python/Turtle/snake/score.txt', 'r') as file_handler:
    display.write('Score: '+ str(FOOD_EATEN) + ' High Score: '+file_handler.read())
screen.update()


game_is_on = True
snake = Snake()
while game_is_on:
    screen.update()
    if(FOOD_EATEN>20):
        time.sleep(0.05)
    elif(FOOD_EATEN>10):
        time.sleep(0.08)
    else:
        time.sleep(0.1)
    
    screen.listen()
    screen.onkeypress(key="w", fun=snake.move_up)
    screen.onkeypress(key="a", fun=snake.move_left)
    screen.onkeypress(key="s", fun=snake.move_down)
    screen.onkeypress(key="d", fun=snake.move_right)
    
    snake.move()
    x_square = math.pow((snake.get_pos()[0]-food.xcor()),2)
    y_square = math.pow((snake.get_pos()[1]-food.ycor()),2)
    d = math.sqrt(int(x_square) + int(y_square))

    # Score
    if(d < 2 and d > -2):
        FOOD_EATEN += 1
        with open('./Learn_Python/Turtle/snake/score.txt', 'r') as file_handler:
            if int(file_handler.read())<FOOD_EATEN:
                file_handler = open('./Learn_Python/Turtle/snake/score.txt', 'w')
                file_handler.write(str(FOOD_EATEN))
                file_handler.close()
        print('Point : ',FOOD_EATEN)
        food.clear()
        food.goto(random.randint(-14,14)*20,random.randint(-14,14)*20)
        food.dot(20,'green')
        food.write(FOOD_EATEN)
        display.clear()
        with open('./Learn_Python/Turtle/snake/score.txt', 'r') as file_handler:
            display.write('Score: '+ str(FOOD_EATEN) + ' High Score: '+file_handler.read())
        snake.move()
        snake.add_snake()
    
    # wall colision
    if(snake.get_pos()[0]< -290 or
     snake.get_pos()[0]> 290 or 
     snake.get_pos()[1]< -290 or
      snake.get_pos()[1]> 290):
        print('Game Over')
        game_is_on = False
        display.clear()
        display.goto(-40,0)
        display.write('Score: '+ str(FOOD_EATEN) + ' Game Over!')
    
    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            display.clear()
            display.goto(-40,0)
            display.write('Score: '+ str(FOOD_EATEN) + ' Game Over!')
    
        
screen.exitonclick()