from turtle import Turtle
score = 0
align = 'center'
font = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        # color should be before write
        self.penup()
        self.goto(0, 275)
        # goto should be before write
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=align, font=font)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=align, font=font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()