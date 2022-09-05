from turtle import Screen
from player import Player
from levelboard import Levelboard
from car_controll import CarController
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
cars = CarController()
level = Levelboard()

screen.listen()
screen.onkey(user.move, "Up")

continue_game = True
while continue_game == True:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()

    for c in cars.cars_list:
        if c.distance(user) < 20:
            continue_game = False
            level.game_over()

    if user.ycor() > 280:
        user.go_to_start()
        cars.next_level()
        level.next_level()


screen.exitonclick()