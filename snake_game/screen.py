from turtle import Screen

from .constants import WORLD


class Field:
    def __init__(self):
        self.screen = Screen()

    def setup(self):

        self.screen.tracer(0)

        window = self.screen.getcanvas().winfo_toplevel()
        temp_x = window.winfo_x() - 5
        window_x = temp_x if temp_x else None
        temp_y = window.winfo_y() - 29
        window_y = temp_y if temp_y else None

        self.screen.setup(width=WORLD, height=WORLD,
                          startx=window_x, starty=window_y)

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
