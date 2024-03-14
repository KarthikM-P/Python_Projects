from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed('fastest')
        self.color('blue')
        

    def refresh(self):
        pos_x=random.randint(-280, 280)
        pos_y=random.randint(-280, 280)
        self.goto(pos_x, pos_y)