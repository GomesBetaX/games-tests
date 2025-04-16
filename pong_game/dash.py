from turtle import Turtle

class Dash(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 290)
        self.setheading(270)
        self.speed("fastest")

    def draw_dash(self):
        keep_dash = True
        while keep_dash:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

            if self.ycor() <= -290:
                keep_dash = False
        self.hideturtle()