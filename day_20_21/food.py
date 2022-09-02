from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        self.goto(randint(-270, 270), randint(-270, 270))
        self.refresh()

    def refresh(self):
        self.goto(randint(-270, 270), randint(-270, 270))