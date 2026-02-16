import turtle as t
import random as rnd

timmy = t.Turtle()
t.colormode(255)
#timmy.shape("turtle")

def random_color():
    r = rnd.randint(0,255)
    g = rnd.randint(0, 255)
    b = rnd.randint(0, 255)
    rnd_color = (r, g, b)
    return rnd_color

def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)

def draw_dashed_line():
    for _ in range(15):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()

def draw_polygon(n_sides):
    angle = 360 / n_sides
    for _ in range(n_sides):
        timmy.forward(100)
        timmy.right(angle)

# for side_n in range(3,11):
#     draw_polygon(side_n)

def random_walk():
    angles = [0, 90, 180, 270]
    timmy.speed("fastest")
    timmy.pensize(10)

    for _ in range(200):
        angle = rnd.choice(angles)
        timmy.color(random_color())
        timmy.forward(30)
        timmy.right(angle)


timmy.speed("fastest")

def draw_spiral(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        timmy.color(random_color())
        timmy.circle(130)
        timmy.setheading(timmy.heading()+size_of_gap)

# draw_spiral(5)


screen = t.Screen()
screen.exitonclick()
