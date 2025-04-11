from turtle import Turtle

ALIGNMENT = "center"
FONT_SIZE = 15
FONT = ("Courier", FONT_SIZE, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.penup()
        self.sety(280)
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER.", False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()