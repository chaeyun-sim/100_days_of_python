import turtle as t

# Challenge 3
# Draw shapes
pen = t.Turtle()

def move(pen, angle):
    pen.forward(100)
    pen.right(angle)

for i in range(2, 11):
    angle = 360 / (i + 1)
    the = i + 1
    for i in range(0, the):
        move(pen, angle)


# Angela's code

pen = t.Turtle()

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        pen.forward(100)
        pen.right(angle)

for shape_side_n in range(3, 11):
    draw_shape(shape_side_n)