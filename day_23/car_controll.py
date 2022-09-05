from turtle import Turtle
from random import randint, choice

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
starting_move_distance = 5
move_increment = 3

class CarController():
    
    def __init__(self):     
        self.cars_list = []
        self.game_speed = starting_move_distance

    def create_cars(self):
        how_many_cars = randint(0, 5)
        if how_many_cars == 0:
            c = Turtle('square')
            c.shapesize(1, 2)
            c.penup()
            c.color(choice(colors))
            c.goto(300, randint(-250, 250))
            self.cars_list.append(c)

    def move(self):
        for car in self.cars_list:
            car.backward(self.game_speed)

    def next_level(self):
        self.game_speed += move_increment