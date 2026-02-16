from turtle import Turtle

WIDTH = 20
HEIGHT  = 100

class  Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        
    def go_up(self,step=50):
        if self.ycor() < 250:
            new_y = self.ycor() + step
            self.goto(self.xcor(), new_y)

    def go_down(self,step=50):
        if self.ycor() > -250:
            new_y = self.ycor() - step
            self.goto(self.xcor(), new_y)

        
