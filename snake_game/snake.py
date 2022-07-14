from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
SEGMENT_RADIUS = 10


class Snake:

    def __init__(self):
        self._segments = []
        self._create_snake()
        self.segment_radius = SEGMENT_RADIUS

    def _create_snake(self):
        for position in STARTING_POSITIONS:
            self._add_segment(position)
        self.head.color("green")

    def _add_segment(self, position):
        new_segment = Turtle("circle")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self._segments.append(new_segment)

    def extend(self):
        self._add_segment(self._segments[-1].position())

    def move(self):
        for seg_num in range(len(self._segments) - 1, 0, -1):
            new_x = self._segments[seg_num - 1].xcor()
            new_y = self._segments[seg_num - 1].ycor()
            self._segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    @property
    def head(self):
        return self._segments[0]

    def self_collision(self):
        for segment in self._segments[1:]:
            if self.head.distance(segment) < SEGMENT_RADIUS:
                return True
        else:
            return False
