from turtle import Screen, Turtle

from .constants import WALL


class Walls(Turtle):

    def __init__(self):
        super().__init__()
        self.restart()

    def restart(self):
        corner1 = (WALL, WALL)
        corner2 = (WALL, -WALL)
        corner3 = (-WALL, -WALL)
        corner4 = (-WALL, WALL)
        self.pensize(5)
        self.color("red")
        self.penup()
        self.goto(corner1)
        self.pendown()
        self.goto(corner2)
        self.goto(corner3)
        self.goto(corner4)
        self.goto(corner1)
        self.hideturtle()

    @staticmethod
    def collision(point, radius):
        if max(map(int, map(abs, list(point)))) > 280:
            return True
