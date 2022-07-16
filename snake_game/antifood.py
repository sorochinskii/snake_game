from random import choice, randint, randrange
from turtle import Turtle

from .constants import WALL, FOOD_RAND_FIELD
from .wall import Walls

HEADING = [45, 135, 225, 315]
FOOD_RADIUS = 5


class AntifoodItem(Turtle):

    def __init__(self):
        super().__init__()
        self.restart()

    def restart(self):
        self._radius = FOOD_RADIUS
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        self._move_count = 0

    def refresh(self):
        random_x = randrange(-FOOD_RAND_FIELD, FOOD_RAND_FIELD, 20)
        random_y = randrange(-FOOD_RAND_FIELD, FOOD_RAND_FIELD, 20)
        self.setheading(choice(HEADING))
        self.goto(random_x, random_y)

    def item_move(self):
        if not self._move_count:
            self._move_count = randint(5, 10)
            self.setheading(choice(HEADING))
        if Walls.collision(list(self.pos()), self.radius):
            self.setheading(self.heading() + 90)
        self.forward(self._radius)
        self._move_count -= 1

    @property
    def radius(self):
        return self._radius


class Antifood:
    def __init__(self):
        self.restart()

    def restart(self):
        self._items = []

    def move(self):
        for item in self._items:
            item.item_move()

    def add_item(self):
        self._items.append(AntifoodItem())

    def collision(self, point, other_radius):
        items_temp = []
        for item in self._items:
            if int(item.distance(point)) <= item.radius + other_radius:
                items_temp.append(item)
        return items_temp

    def remove_items(self, items):
        if items:
            for item in items:
                self._items.remove(item)
                item.hideturtle()
