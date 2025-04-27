from turtle import Turtle
import pandas

AMERICAN_STATES = 50

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.corrected_states = 0
        self.score = self.corrected_states
        self.hideturtle()
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.corrected_states} / {AMERICAN_STATES}", align="center", font=("Arial", 12, "normal"))

    def get_highschore(self):
        with open("./us_game/highscores.txt", "r") as file:
            highscore = file.read()
        return int(highscore)
    
    def save_highscore(self, score):
        print(f"está mandando {score} para a funcao save_")
        if score > self.get_highschore():
            with open("./us_game/highscores.txt", "w") as file:
                file.write(str(score))

    def update_score(self):
        self.corrected_states += 1
        self.score = self.corrected_states
        self.save_highscore(score=self.score)
