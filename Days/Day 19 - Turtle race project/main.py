from turtle import Turtle, Screen
import random as rnd

tim = Turtle()
screen = Screen()

width = 800
height = 600
finish_line = width//2 - 30

def draw_vertical_line(n_turtles):
    x = finish_line
    y = -height//2 + height//8
    tim.penup()
    tim.goto(x = x, y = y)
    tim.left(90)
    tim.pendown()
    tim.pensize(4)
    tim.pencolor("red")
    tim.forward((n_turtles-1)*(height//7))
    tim.hideturtle()



screen.setup(width = width, height=height)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color: ")
turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

draw_vertical_line(len(turtle_colors))

for i,color in enumerate(turtle_colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    x_axis = - width//2 + 30
    y_axis = - height//2 + height//8
    new_turtle.goto(x = x_axis, y=y_axis +i*(height//7))
    turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > finish_line:
            is_race_on=False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost.. The {winning_color} turtle is the winner!")

        rnd_distance = rnd.randint(0,10)
        turtle.forward(rnd_distance)


screen.exitonclick()
