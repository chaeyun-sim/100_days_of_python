from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.com_score = 0
        self.user_score = 0
        self.color('white')
        self.penup()
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.com_score, align='center', font=('Courier', 80, 'normal'))
        self.goto(100, 200)
        self.write(self.user_score, align='center', font=('Courier', 80, 'normal'))

    def increase_com_score(self):
        self.com_score += 1
        self.update_score()

    def increase_user_score(self):
        self.user_score += 1
        self.update_score()