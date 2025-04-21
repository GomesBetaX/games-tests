from turtle import Turtle

UP = 90

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset()

    def move_up(self):
        self.fd(20)

    def reset(self):
        self.goto(0, -280)
        self.setheading(UP)