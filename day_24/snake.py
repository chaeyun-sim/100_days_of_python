from turtle import Turtle 
move_distance = 20
directs = [0, 90, 180, 270]
positions = [(0, 0), (-20, 0), (-40, 0)]
continue_game = False

class Snake:

    def __init__(self):     
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for position in positions:
            self.add_snake(position)

    def add_snake(self, position):
        t = Turtle('square')
        t.color("white")
        t.penup()
        t.goto(position)
        self.turtles.append(t)

    def reset(self):
        for turt in self.turtles:
            turt.goto(1000, 1000)
        self.turtles.clear()
        self.create_snake()
        self.head = self.turtles[0]

    def extend_tail(self):
        self.add_snake(self.turtles[-1].position())

    def move(self):
        for n in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[n - 1].xcor()
            y = self.turtles[n - 1].ycor()
            self.turtles[n].goto(x, y)
        self.turtles[0].forward(move_distance)

    def up(self):
        if self.head.heading() != directs[3]:
            self.turtles[0].setheading(90)

    def down(self):
        if self.head.heading() != directs[1]:
            self.turtles[0].setheading(270)

    def left(self):
        if self.head.heading() != directs[2]:
            self.turtles[0].setheading(180)

    def right(self):
        if self.head.heading() != directs[0]:
            self.turtles[0].setheading(0)