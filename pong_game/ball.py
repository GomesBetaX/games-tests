from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(0, 360))
        self.goto(0, 0)
        self.dx = 10
        self.dy = 10

    def reset_heading(self, direction):
        if direction == "horizontal":
            self.dx *= -1

        elif direction == "vertical":
            self.dy *= -1

        # self.setheading(self.heading() - self.heading()) 


    def reset_ball (self):
        self.goto(0, 0)
        self.setheading(random.randint(0, 360))
        self.reset_heading("horizontal")
        self.reset_heading("vertical")

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)