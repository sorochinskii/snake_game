from turtle import Turtle
import random
from .constants import WALL

FOOD_RADIUS = 5


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.restart()

    def restart(self):
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        self.radius = FOOD_RADIUS

    def refresh(self):
        random_x = random.randint(-WALL, WALL)
        random_y = random.randint(-WALL, WALL)
        self.goto(random_x, random_y)

    def collision(self, point, radius):
        if self.distance(point) < radius + self.radius:
            return True
