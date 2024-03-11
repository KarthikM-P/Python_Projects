from turtle import Turtle, Screen

# To SetUp The Screen And Change Color
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
x_coordinate=[(0, 0),(-20, 0),(-40, 0)]
segment=[]
for i in x_coordinate:
    obj=Turtle('square')
    obj.color("white")
    obj.goto(i)
    segment.append(obj)

is_game_on=True
while is_game_on:
    for s in segment:
        obj.forward(20)









screen.exitonclick()