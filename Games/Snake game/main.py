from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

def initialize_game():
    global snake, food, score, screen, delay, game_is_on

    # ---- Screen setup ----
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game - Simor")
    screen.tracer(0)

    game_is_on = True

    level_choice = screen.textinput(
        title="Choose the difficulty level",
        prompt='Type: "e" for easy, "h" for hard or "v" for veteran'
    )

    if level_choice and level_choice.lower() == "h":
        delay = 70
    elif level_choice and level_choice.lower() == "v":
        delay = 50
    else:
        delay = 90

    snake = Snake()
    food = Food()
    score = Score()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


def game_loop():
    if not game_is_on:
        return

    snake.move()

    # Collision with foodR
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Collision with wall
    if (
        snake.head.xcor() > 290 or snake.head.xcor() < -300 or
        snake.head.ycor() > 300 or snake.head.ycor() < -290
    ):
        end_game()
        return

    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            end_game()
            return

    screen.update()
    screen.ontimer(game_loop, delay)


def end_game():
    global game_is_on

    game_is_on = False
    score.game_over()
    screen.update()
    time.sleep(1)
    answer = ""
    answer = screen.textinput(
        title="Play again?",
        prompt='Type "y" or "n")'
    )

    if answer.lower() == "y":
        screen.clear()
        initialize_game()
        game_loop() 


# ---- Start game  ----
initialize_game()
game_loop()

screen.exitonclick()
