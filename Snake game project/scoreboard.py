from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 15, 'normal')

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(x=0, y=280)
        self.current_score = 0
        self.show_scoreboard()

    def show_scoreboard(self):
        self.write(f"score = {self.current_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.show_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGN, font = FONT)
