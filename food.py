from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")

    def relocate(self):
        rand_x = random.randint(-480, 480)
        rand_y = random.randint(-480, 460)
        self.goto(rand_x, rand_y)
