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
        self.highscore = self.get_highscore()

    def get_data(self):
        try:
            data = pandas.read_csv("./us_game/highscores.csv")
        except FileNotFoundError:
            highscores = {
                "highscore": [0],
                }
            pandas.DataFrame(highscores).to_csv("./us_game/highscores.csv", index=False)
            data = pandas.read_csv("./us_game/highscores.csv")
        return data

    def write_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.corrected_states} / {AMERICAN_STATES}", align="center", font=("Arial", 12, "normal"))

    def get_highscore(self):
        data = self.get_data()
        highscore = data["highscore"].values
        return int(highscore[0])
    
    def save_highscore(self, score):
        print(f"está mandando {score} para a funcao save_")
        if score > self.get_highscore():
            data = self.get_data()
            data["highscore"] = score
            data.to_csv("./us_game/highscores.csv", index=False)

    def update_score(self):
        self.corrected_states += 1
        self.score = self.corrected_states
        self.save_highscore(score=self.score)
