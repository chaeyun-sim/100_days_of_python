# pingpong game


from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


# create the screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('pong game')
screen.tracer(0)

# create another paddle for computer
user = Paddle((370, 0))
com = Paddle((-370, 0))

# create the ball and make it move
ball = Ball()
scoreboard = Scoreboard()

# create and move a paddle
screen.listen()
screen.onkey(user.up, "Up")
screen.onkey(com.up, "w")
screen.onkey(user.down, "Down")
screen.onkey(com.down, "s")

continue_game = True 
while continue_game == True:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # detect collision with paddle
    if ball.distance(user) < 50 and ball.xcor() > 340 or ball.distance(com) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # detect when paddle misses and keep score
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_user_score()
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_com_score()


screen.exitonclick()