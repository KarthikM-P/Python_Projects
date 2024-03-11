# To Import Turtle Module 
from turtle import Turtle, Screen

# Turtle Object created 
turtle1=Turtle()
# Screen Object Created To Control The Window
screen=Screen()
# Used To Listen The Events
screen.listen()

# These Functions Are Used As An Input To Onkey Event  
def move_forward():
    turtle1.forward(10)

def move_backward():
    turtle1.backward(10)

def move_left():
    # Insted of Heading Method We Can Also Use turtle.left(10)
    new=turtle1.heading() + 10
    turtle1.setheading(new)
    
def move_right():
    # Insted of Heading Method We Can Also Use turtle.right(10)
    new=turtle1.heading() - 10
    turtle1.setheading(new)

# Clear The Drawings 
def clear():
    turtle1.clear()
    turtle1.penup()
    turtle1.home()
    turtle1.pendown()
# The Onkey Function Is Used To Trigger The Key On Keyboard 
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='d', fun=move_right)
screen.onkey(key='a', fun=move_left)
screen.onkey(key='c', fun=clear)
screen.exitonclick()