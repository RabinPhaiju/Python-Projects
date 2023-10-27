from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title('Ping Pong')
screen.listen()
screen.tracer(0)

l_paddle = Paddle(-360)
r_paddle = Paddle(360)
m_paddle = Paddle(0,5,1,80)
m_paddle = Paddle(0,5,1,-80)
m_paddle = Paddle(0,5,1,220)
m_paddle = Paddle(0,5,1,-220)

ball = Ball()

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(.08)
    screen.update()
    screen.onkey(l_paddle.paddle_up,'w')
    screen.onkey(l_paddle.paddle_down,'s')
    screen.onkey(r_paddle.paddle_up,'Up')
    screen.onkey(r_paddle.paddle_down,'Down')

    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
    
    if ball.distance(r_paddle)< 50 and ball.xcor() > 340:
        ball.p_bounce()
    
    if ball.distance(l_paddle)< 50 and ball.xcor() < -340:
        ball.p_bounce()
    
    if ball.xcor()<-350:
        scoreboard.score_left()
        scoreboard.show()
        ball.goto(0,0)
    
    if ball.xcor()>350:
        scoreboard.score_right()
        scoreboard.show()
        ball.goto(0,0)
    
    if(scoreboard.l_score > 10 or scoreboard.r_score > 10 ):
        game_is_on = False


screen.exitonclick()