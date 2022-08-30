from turtle import Turtle, Screen


# Challenge 1
# Draw a square

turtle = Turtle()

def right_then_move(turtle):
    turtle.right(90)
    turtle.forward(100)

for i in range(4):
    right_then_move(turtle)



