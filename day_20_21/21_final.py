# snake game

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Create a snake body
snake = Snake()
food = Food()
# create a score board
scoreboard = Scoreboard()

# control the snake
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


continue_game = True
while continue_game == True:
    screen.update()
    time.sleep(0.1)

    # move snake
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_tail()
        scoreboard.increase_score()

    # detect collision with wall + show game over
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 299 or snake.head.ycor() < -290:
        continue_game = False
        scoreboard.game_over()

    # detect collision with tail
    # for tt in snake.turtles:
    #     if tt == snake.head:
    #         pass
    #     elif snake.head.distance(tt) < 10:
    #         continue_game = False
    #         scoreboard.game_over()

    # use slicing to change shorter
    for tt in snake.turtles[-1]:
        if snake.head.distance(tt) < 10:
            continue_game = False
            scoreboard.game_over()
    
screen.exitonclick()