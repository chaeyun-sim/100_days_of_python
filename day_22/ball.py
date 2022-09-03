from turtle import Turtle
import random
move_distance = random.randint(0, 18)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.shapesize(1, 1)
        self.penup()
        self.x_move = 10
        self.y_move = move_distance - 7
        self.move_speed = 0.1

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.hideturtle()
        self.goto(0, 0)
        self.move_speed = 0.1
        self.showturtle()
        self.bounce_x()