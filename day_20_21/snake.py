from turtle import Turtle 
move_distance = 20
position = [0, 90, 180, 270]
continue_game = False


class Snake:

    def __init__(self):     
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for i in range(3):
            t = Turtle('square')
            t.color("white")
            t.penup()
            t.goto(0 - (i * 20), 0)
            self.turtles.append(t)

    def move(self):
        for n in range(2, 0, -1):
            x = self.turtles[n - 1].xcor()
            y = self.turtles[n - 1].ycor()
            self.turtles[n].goto(x, y)
        
        self.turtles[0].forward(move_distance)

    def up(self):
        if self.head.heading() != position[3]:
            self.turtles[0].setheading(90)

    def down(self):
        if self.head.heading() != position[1]:
            self.turtles[0].setheading(270)

    def left(self):
        if self.head.heading() != position[2]:
            self.turtles[0].setheading(180)

    def right(self):
        if self.head.heading() != position[0]:
            self.turtles[0].setheading(0)

    # def game_end(self):
    #     if self.turtles[0].xcor() == 300:
    #         continue_game = False
    #         print("You bumped into a wall! You lose.")