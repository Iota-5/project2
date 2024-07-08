from turtle import Turtle


class Snake:

    def __init__(self):
        self.start_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segment = []

    def start(self):
        for _ in self.start_position:
            self.add_seg(_)

    def add_seg(self, _):
        snake = Turtle("square")
        snake.color("green")
        snake.penup()
        snake.goto(_)
        self.segment.append(snake)

    def new_segment(self):
        self.add_seg(self.segment[-1].position())

    def clear_seg(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.start()

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(20)

    def down(self):
        if self.segment[0].heading() != 90:
            self.segment[0].setheading(270)

    def right(self):
        if self.segment[0].heading() != 180:
            self.segment[0].setheading(0)

    def left(self):
        if self.segment[0].heading() != 0:
            self.segment[0].setheading(180)

    def up(self):
        if self.segment[0].heading() != 270:
            self.segment[0].setheading(90)
