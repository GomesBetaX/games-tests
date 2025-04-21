from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)

        #start going to a random direction
        self.setheading(random.randint(0, 360))

    def bounce(self):
        new_angle = 360 - self.heading()
        self.setheading(new_angle)

    def bounce_pad(self):
        new_angle = (180 - self.heading()) % 360
        self.setheading(new_angle)

    def reset(self):
        self.goto(0, 0)
        new_angle = (180 - self.heading())
        self.setheading(new_angle)


    def move(self):
        self.fd(17)