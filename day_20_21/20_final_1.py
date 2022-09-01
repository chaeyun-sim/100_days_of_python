# snake game

# Create a snake body
# move snake
# control the snake
# detect collision with food
# create a score board
# detect collision with wall + show game over
# detect collision with tail

from turtle import Turtle, Screen
from snake import Snake
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

continue_game = True
while continue_game == True:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # snake.game_end()
    
screen.exitonclick()