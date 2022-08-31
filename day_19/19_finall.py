from turtle import Turtle, Screen
import random

# initail settings
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# turtles' colors
colors = ['red', 'yellow', 'green', 'blue', 'purple']

# set turtles' position and color
turtles = []
for turtle_index in range(len(colors)):
    ttt = Turtle(shape='turtle')
    ttt.penup()
    ttt.color(colors[turtle_index])
    ttt.goto(-235, -60 + (turtle_index * 30))
# make a list of created turtles
    turtles.append(ttt)

# if user bets, game starts
if user_bet:
    game_continues = True

# if a turtle reaches the end of the window, the game ends.
while game_continues == True:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_continues = False
            the_color = turtle.pencolor()
            if the_color == user_bet:
                print(f"Congradulations! You win! The winner is {the_color}.")
            else:
                print(f"You lose. The winner is {the_color}.")
# the length the turtle goes at one time should be random. 
        turtle.forward(random.randint(0, 10))

# exit the screen when clicked
screen.exitonclick()