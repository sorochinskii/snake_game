import time
from turtle import Screen

from snake_game.constants import WALL, WORLD
from snake_game.food import Food
from snake_game.game import Game
from snake_game.scoreboard import Scoreboard
from snake_game.screen import Field
from snake_game.snake import Snake
from snake_game.wall import Walls
from snake_game.antifood import Antifood
import tkinter  


def main():

    game = Game()
    field = Field()


    while game.on:

        if game.resetter:

            game.setup()

            window = field.get_canvas().winfo_toplevel()
            window_x = window.winfo_x()
            window_y = window.winfo_y()

            field.clear()
            field.setup(window_x, window_y)

            snake = Snake()
            food = Food()
            scoreboard = Scoreboard()
            walls = Walls()
            antifood = Antifood()

            field.control(snake, game)

        if not game.over:
            game.delay()
            field.update()
            antifood.move()
            food.move()
            snake.move()

        if food.collision(snake.head.pos(), snake.segment_radius):
            antifood.add_item()
            food.refresh()
            snake.extend()
            scoreboard.change_score(+1)

        antifood_collisions = antifood.collision(snake.head.pos(),
                                                 snake.segment_radius)
        if antifood_collisions:
            antifood.remove_items(antifood_collisions)
            snake.segment_destroy()
            scoreboard.change_score(-1)
            
        if (Walls.collision(snake.head.pos(), snake.segment_radius) or
                snake.self_collision()):
            game.over = True


        if game.over: 
            scoreboard.game_over()

if __name__ == '__main__':
    main()
