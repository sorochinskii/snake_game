from turtle import Screen

from .constants import WORLD


class Field:
    def __init__(self):
        self.screen = Screen()

    def setup(self, window_x = None, window_y = None):
        self.screen.tracer(0)
        self.screen.setup(width=WORLD, height=WORLD, 
                          startx = window_x, starty = window_y)
        self.screen.bgcolor("black")
        self.screen.title("Super Duper Snake Game")
        self.screen.listen()

    def clear(self):
        self.screen.clear()

    def control(self, snake, game):
        self.screen.onkey(snake.up, "Up")
        self.screen.onkey(snake.down, "Down")
        self.screen.onkey(snake.left, "Left")
        self.screen.onkey(snake.right, "Right")
        self.screen.onkey(game.resetter_on, "r")
        self.screen.onkey(game.quit, "q")
        self.screen.onkeypress(game.dec_tempo, "space")
        self.screen.onkeyrelease(game.inc_tempo, "space")

    def update(self):
        self.screen.update()

    def turtles(self):
        return self.screen.turtles()

    def get_canvas(self):
        return self.screen.getcanvas()
