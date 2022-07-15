from turtle import Screen

from .constants import WORLD


class Field:
    def __init__(self):
        self.screen = Screen()
        self.restart()

    def restart(self):
        self.screen.tracer(0)
        self.screen.setup(width=WORLD, height=WORLD)
        self.screen.bgcolor("black")
        self.screen.title("Super Duper Snake Game")
        self.screen.listen()

    def clear(self):
        self.screen.reset()

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

    def get_screen(self, turtle):
        return turtle.getscreen()

    def turtles(self):
        return self.screen.turtles()
