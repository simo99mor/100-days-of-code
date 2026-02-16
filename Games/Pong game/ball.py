from turtle import Turtle
import random as rnd

LEFT_ANGLES = [150, 165, 195, 210]
RIGHT_ANGLES = [30, 45, 315, 330]
STARTING_ANGLES = [0, 180]
STARTING_SPEED = 0.028

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.move_speed = STARTING_SPEED

    def move(self):
        self.penup()
        self.forward(10)

    def paddle_collision(self):
        # case 1) the ball is approaching the left paddle
        if 90 < self.heading() < 270:
            new_heading = rnd.choice(RIGHT_ANGLES)
            self.setheading(new_heading)
        # case 2) the ball is approaching the right paddle
        else:
            new_heading = rnd.choice(LEFT_ANGLES)            
            self.setheading(new_heading)  
        self.move()
        self.move_speed *= 0.99

    def wall_collision(self):
        self.setheading(360 - self.heading())

    def reset_position(self):
        self.home()
        self.move_speed = 0.03
        self.setheading(self.heading() - rnd.choice(STARTING_ANGLES))
