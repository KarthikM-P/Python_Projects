from turtle import Turtle

POSITIONS=[(0, 0),(-20, 0),(-40, 0)]
MOVEMENT=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head=self.segments[0]
    
    def create_snake(self):
        for i in POSITIONS:
            self.add_segments(i)

    def extend(self):
        self.add_segments(self.segments[-1].position()) 

    def add_segments(self, i):
        new_segments=Turtle('square')
        new_segments.color("white")
        new_segments.penup()
        new_segments.goto(i)
        self.segments.append(new_segments)

    def move(self):
        for num in range(len(self.segments)-1, 0, -1):
            x_num=self.segments[num-1].xcor()
            y_num=self.segments[num-1].ycor()
            self.segments[num].goto(x_num,y_num)
        self.head.forward(MOVEMENT) 

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)     
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT) 
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT) 