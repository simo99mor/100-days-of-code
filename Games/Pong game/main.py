from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random as rnd

COMPUTER_STEP = 10

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height=600)
screen.title("Pong game - Simor")
screen.tracer(0)  # to turn off the animation

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down,"Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down,"s")

def computer_paddle_l():
    # if the ball is approaching the left paddle:
    if ball.xcor() < 0:

        error = rnd.randint(-15,15)

        if ball.ycor() > paddle_l.ycor() + 10:
            paddle_l.go_up(step=COMPUTER_STEP + error)

        elif ball.ycor() < paddle_l.ycor() - 10:
            paddle_l.go_down(step=COMPUTER_STEP + error)

def computer_paddle_r():
    # if the ball is approaching the left paddle:
    if ball.xcor() > 0:

        error = rnd.randint(-15,15)

        if ball.ycor() > paddle_r.ycor() + 10:
            paddle_r.go_up(step=COMPUTER_STEP + error)

        elif ball.ycor() < paddle_r.ycor() - 10:
            paddle_r.go_down(step=COMPUTER_STEP + error)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    computer_paddle_l()
    #computer_paddle_r()

    # TODO Detect collision between the ball and the paddles
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.paddle_collision()

    # TODO Detect collision with the wall
    if ball.position()[1] > 290 or ball.position()[1] < -290:
        ball.wall_collision()

    # TODO Detect Right paddle misses
    if ball.xcor() > 390:
        scoreboard.increase_l_score()
        ball.reset_position()

    if ball.xcor() < -390:
        scoreboard.increase_r_score()
        ball.reset_position()

screen.exitonclick()
