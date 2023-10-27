from turtle import Turtle
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
    

    def add_snake(self):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)
    
        
    def move(self):
        for snake_b in range(len(self.segments)-1,0,-1):
            new_x = self.segments[snake_b-1].xcor()
            new_y = self.segments[snake_b-1].ycor()
            self.segments[snake_b].goto(new_x,new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def move_left(self):
        if(self.segments[0].heading() != 0):
            self.segments[0].setheading(180)
        
    def move_right(self):
        if(self.segments[0].heading() != 180):
            self.segments[0].setheading(0)
        
    def move_up(self):
        if(self.segments[0].heading() != 270):
            self.segments[0].setheading(90)
        
    def move_down(self):
        if(self.segments[0].heading() != 90):
            self.segments[0].setheading(270)
    
    def get_pos(self):
        return (self.segments[0].xcor(),self.segments[0].ycor())