from random import choice, randrange
from turtle import Turtle

from .constants import FOOD_RAND_FIELD
from .wall import Walls

FOOD_RADIUS = 5
HEADING = [45, 135, 225, 315]


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
        random_x = randrange(-FOOD_RAND_FIELD, FOOD_RAND_FIELD, 20)
        random_y = randrange(-FOOD_RAND_FIELD, FOOD_RAND_FIELD, 20)
        self.setheading(choice(HEADING))
        self.goto(random_x, random_y)

    def move(self):
        if Walls.collision(list(self.pos()), self.radius):
            self.setheading(self.heading() + 90)
        self.forward(self.radius)

    def collision(self, point, radius):
        if self.distance(point) < radius + self.radius:
            return True
