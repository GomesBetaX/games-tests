from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-210, 250)
        self.nivel = 1

    def update_score(self):
        self.clear()
        print(f"Level: {self.nivel}")
        self.write(f"Level: {self.nivel}", align="center", font=("Arial", 20, "normal"))

    def level_up(self):
        self.nivel += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=("Arial", 20, "normal"))