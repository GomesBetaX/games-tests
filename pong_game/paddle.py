from turtle import Turtle

PLAYER_PADDLE = [(-350, 0), (-350, 20), (-350, 40), (-350, 60)]
PC_PADDLE = [(350, 0), (350, 20), (350, 40), (350, 60)]

class Paddle():
    def __init__(self, user):
        self.paddle = []
        self.create_paddle(user)
    
    def create_paddle(self, user):
        if user == "USER":
            for i in range(len(PLAYER_PADDLE)):
                new_pad = Turtle("square")
                new_pad.color("white")
                new_pad.penup()
                new_pad.goto(PLAYER_PADDLE[i])
                new_pad.setheading(90)
                self.paddle.append(new_pad)

        elif user == "PC":
            for i in range(len(PC_PADDLE)):
                new_pad = Turtle("square")
                new_pad.speed("fastest")
                new_pad.color("white")
                new_pad.penup()
                new_pad.goto(PC_PADDLE[i])
                new_pad.setheading(270)
                self.paddle.append(new_pad)

    def up(self):
        for pad in self.paddle:
            pad.setheading(90)
            pad.forward(20)
            
    def down(self):
        for pad in self.paddle:
            pad.setheading(270)
            pad.forward(20)

    def move(self):
        for i in range(len(self.paddle) - 1, 0, -1):
            next_pos = self.paddle[i - 1].pos()
            self.paddle[i].goto(next_pos)
        self.paddle[0].forward(20)
