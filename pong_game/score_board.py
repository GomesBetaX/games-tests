from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.scores = [0, 0]
        self.penup()
        self.sety(230)
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"{self.scores[0]} : {self.scores[1]}", False, align="center", font=("Courier", 32, "bold"))

    def add_score(self, player):
        if player == "USER":
            self.scores[0] += 1
        elif player == "PC":
            self.scores[1] += 1
        self.update_score()