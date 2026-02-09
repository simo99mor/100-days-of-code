from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

# ---- Screen setup ----
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - Simor")
screen.tracer(0)

# ---- Difficulty level choice ----
level_choice = screen.textinput(
    title= "Choose the difficulty level",
    prompt = "Type: \"e\" for easy, \"h\" for hard or \"v\" for veteran"
).lower()
if level_choice == "e":
    delay = 90
elif level_choice == "h":
    delay = 70
else: 
    delay = 50

# ---- Game objects ----
snake = Snake()
food = Food()
score = Score()

# ---- Keyboard listener ----
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# ---- Game loop ----
game_is_on = True

def game_loop():
    global game_is_on

    if not game_is_on:
        return 

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if (
        snake.head.xcor() > 290 or snake.head.xcor() < -290 or
        snake.head.ycor() > 290 or snake.head.ycor() < -290
    ):
        score.game_over()
        game_is_on = False
        return 

    # Detect collision with tail
    for segment in snake.segments:
        if snake.head != segment:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                score.game_over()
                return
    
    screen.update()
    screen.ontimer(game_loop, delay)

game_loop()

screen.exitonclick()
