from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100,190)
        self.write(self.l_score,align='center',font=('Courier',80))
        self.goto(100,190)
        self.write(self.r_score,align='center',font=('Courier',80))
    
    def score_left(self):
        self.l_score +=1

    def score_right(self):
        self.r_score +=1

    def show(self):
        self.clear()
        self.goto(-100,190)
        self.write(self.l_score,align='center',font=('Courier',80))
        self.goto(100,190)
        self.write(self.r_score,align='center',font=('Courier',80))