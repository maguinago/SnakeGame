from turtle import *
import time

INITIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
PACE = 20
# Solid walls? "Yes" or "No"?
WALL_DEATH = "No"

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for coordinate in INITIAL_POSITIONS:
            self.add_segment(coordinate)

    def add_segment(self, coordinate):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.shapesize(0.9, 0.9)
        new_segment.penup()
        new_segment.goto(coordinate)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(PACE)
        self.last_heading = self.head.heading()

    def up(self):
        if self.last_heading != 270:
            self.head.setheading(90)

    def down(self):
        if self.last_heading != 90:
            self.head.setheading(270)

    def left(self):
        if self.last_heading != 0:
            self.head.setheading(180)

    def right(self):
        if self.last_heading != 180:
            self.head.setheading(0)

    def reset(self):
        for seg in self.segments:
            seg.ht()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]