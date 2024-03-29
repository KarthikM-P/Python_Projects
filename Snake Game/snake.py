from turtle import Screen
from snakeclass import Snake
from food import Food
from ScoreBoard import Score
import time
# To SetUp The Screen And Change Color
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Score()

# react based on user input 
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move() 

    # detects the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_update()
    # detects the collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # detects collision with head
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                is_game_on = False
                scoreboard.game_over()
screen.exitonclick()