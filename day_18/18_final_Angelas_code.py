# Find colors
# import colorgram

# rgb_colors = []
# colors = colorgram.extract("/Users/chaeyun/Documents/100_days_of_python/day_18/image.jpg", 110)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)


import turtle as t
import random

color_list =[
    (250, 246, 243), (248, 245, 246),
    (212, 154, 97), (242, 248, 245),
    (52, 107, 131), (235, 240, 244),
    (199, 142, 33), (178, 78, 33),
    (116, 155, 171), (124, 79, 98),
    (122, 175, 158), (227, 197, 128),
    (191, 87, 108), (55, 38, 19),
    (11, 49, 63), (42, 168, 128),
    (198, 123, 142), (51, 126, 121),
    (167, 21, 30), (225, 92, 77),
    (243, 163, 160), (38, 32, 34),
    (4, 26, 25), (79, 147, 169),
    (164, 25, 21), (19, 80, 92),
    (237, 165, 170), (177, 206, 185),
    (102, 127, 158), (164, 203, 211),
    (58, 60, 74), (15, 103, 99),
    (182, 190, 205), (78, 67, 39)
    ]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()



tim.penup()
tim.setheading(225)
tim.forward(325)
tim.setheading(0)


for i in range(1, 101):
    tim.dot(25, random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if i % 10 == 0:
        tim.penup()
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()

screen = t.Screen()
screen.exitonclick()