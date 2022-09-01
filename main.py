from turtle import *
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Cobra Spiel")
screen.tracer(0)

wall_death = "yes"

scoreboard = Score()

snake = Snake()
food = Food()
screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    if scoreboard.score < 5:
        game_speed = time.sleep(0.1)
    elif scoreboard.score < 11:
        game_speed = time.sleep(0.08)
    elif scoreboard.score < 16:
        game_speed = time.sleep(0.06)
    else:
        game_speed = time.sleep(0.04)
    snake.move()

# Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase()

    dist = 280
    if wall_death.lower() == "yes":

        # With wall collision
        if snake.head.xcor() > dist or snake.head.xcor() < -dist or snake.head.ycor() > dist \
                or snake.head.ycor() < -dist:
            # game_is_on = False
            scoreboard.reset()
            snake.reset()

    # Without wall collision
    else:
        if snake.head.xcor() > dist:
            snake.head.setx(-dist)
        if snake.head.xcor() < -dist:
            snake.head.setx(dist)
        if snake.head.ycor() > dist:
            snake.head.sety(-dist)
        if snake.head.ycor() < -dist:
            snake.head.sety(dist)

    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # scoreboard.game_over()
            scoreboard.reset()
            snake.reset()

screen.exitonclick()