from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,x_pos,stretch_width = 5,stretch_length = 1,y_pos=0):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=stretch_width,stretch_len=stretch_length)
        self.color('white')
        self.penup()
        self.goto(x_pos,y_pos)

    def paddle_up(self):
        if self.ycor()<270:
            new_y = self.ycor()+30
            self.goto(self.xcor(),new_y)
        
    def paddle_down(self):
        if self.ycor()>-270:
            new_y = self.ycor()-30
            self.goto(self.xcor(),new_y)