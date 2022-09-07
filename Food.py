import random

from turtle import Turtle

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color('purple')
        self.speed('fastest')
        self.spawn()

    def spawn(self):
        self.goto(random.randint(a= -280, b= 280), random.randint(-280, 280))

    