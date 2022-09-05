from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 25, 'normal')

class Levelboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.goto(-210, 250)
        self.hideturtle()
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)

    def next_level(self):
        self.level += 1
        self.update_level()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
