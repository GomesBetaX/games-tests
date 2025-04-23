from turtle import Turtle

ALIGNMENT = "center"
FONT_SIZE = 15
FONT = ("Courier", FONT_SIZE, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.highscore = self.get_highscore()
        self.score = 0
        self.penup()
        self.sety(280)
        self.update_score()

    def game_over(self):     
        if self.score > self.highscore:
            self.save_highscore()
            # self.highscore = self.score
        self.score = 0
        # self.goto(0,0)
        self.update_score()

    def update_score(self):
        self.clear()
        self.get_highscore()
        self.write(f"Score = {self.score} | High score: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.update_score()

    def get_highscore(self):
        with open("data.txt") as file:
            self.highscore = int(file.read())

    def save_highscore(self):
        with open("data.txt", "w") as file:
            file.write(str(self.score))