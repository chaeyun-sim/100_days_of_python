from turtle import Turtle

starting_position = (0, -280)
move_distance = 10
finish_line_y = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.setheading(90)
        # self.refresh()
    
    def move(self):
        self.forward(10)

    def go_to_start(self):
        self.goto(starting_position)
