from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-340,260)
        self.write('Level '+str(self.level),align='center',font=('Courier',20))
    
    def set_score(self):
        self.level +=1

    def show(self):
        self.clear()
        self.goto(-340,260)
        self.write('Level '+str(self.level),align='center',font=('Courier',20))

    def finish(self):
        self.clear()
        self.goto(-20,0)
        self.write('Game Over!',align='center',font=('Courier',20))