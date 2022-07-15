from turtle import Screen
from snake_game.snake import Snake
from snake_game.food import Food
from snake_game.scoreboard import Scoreboard
from snake_game.constants import WORLD, WALL
from snake_game.wall import Walls
from snake_game.game import Game
from snake_game.screen import Field
import time


def main():

    screen = Field()
    snake = Snake()
    game = Game()
    food = Food()
    scoreboard = Scoreboard()
    walls = Walls()

    screen.control(snake, game)

    while game.on:

        if not game.over:
            game.delay()
            screen.update()
            snake.move()

        if food.collision(snake.head.pos(), snake.segment_radius):
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if (Walls.collision(snake.head.pos(), snake.segment_radius) or
                snake.self_collision()):
            game.over = True

        if game.resetter:
            screen.clear()
            snake.restart()
            food.restart()
            walls.restart()
            game.restart()
            screen.control(snake, game)
            scoreboard.restart()

        if game.over:
            scoreboard.game_over()


if __name__ == '__main__':
    main()
