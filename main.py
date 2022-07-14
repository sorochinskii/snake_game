from turtle import Screen
from snake_game.snake import Snake
from snake_game.food import Food
from snake_game.scoreboard import Scoreboard
from snake_game.constants import WORLD, WALL
from snake_game.wall import Walls
import time

screen = Screen()
screen.setup(width=WORLD, height=WORLD)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
walls = Walls()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if Walls.collision(snake.head.pos(), snake.segment_radius):
        game_is_on = False
        scoreboard.game_over()

    if snake.self_collision():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
