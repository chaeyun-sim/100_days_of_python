from re import T
import turtle as t

# Challenge 2
# Draw a dotted line

pen = t.Turtle()

def draw_dots(pen):
    pen.forward(10)
    pen.penup()
    pen.forward(10)
    pen.pendown()

for i in range(15):
    draw_dots(pen)