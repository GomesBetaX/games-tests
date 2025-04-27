from turtle import Turtle

class Writer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Guess the State", align="center", font=("Arial", 24, "normal"))

    def write_state(self, state, x, y):
        self.goto(x, y)
        self.write(state, align="center", font=("Arial", 10, "bold"))