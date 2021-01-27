from turtle import Turtle
import random as r


class Food(Turtle): #class Food mewarisi class Turtle
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()

    def refresh(self):
        x = r.randint(-280, 280)
        y = r.randint(-280, 280)
        self.goto(x, y)

