import time
from score_board import Scoreboard
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from dash import Dash

SCREEN_SIZE = (800, 600)
UP = 90
DOWN = 270

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(SCREEN_SIZE[0], SCREEN_SIZE[1])
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

# players
c1 = Paddle("LEFT")
c2 = Paddle("RIGHT")

# ball
b = Ball()

#score
score = Scoreboard()

#dash line
d = Dash()
d.draw_dash()

# commands player_left
screen.onkeypress(c2.up, "Up")
screen.onkeypress(c2.down, "Down")

# commands player_right
screen.onkeypress(c1.up, "w")
screen.onkeypress(c1.down, "s")

# game working
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)

    score.update_score()

    #moving ball
    b.move()

    #collision with wall
    if b.ycor() >= 280 or b.ycor() <= -280:
        b.bounce()

    #collision with vertical walls
    if b.xcor() > 380 or b.xcor() < -380:
        if b.xcor() > 0:
            score.add_score("USER")
        else:
            score.add_score("PC")
        b.reset()

    #collision with paddle
    collision_c1 = -350 < b.xcor() < -330 and c1.ycor() + 50 > b.ycor() > c1.ycor() - 50
    collision_c2 = 330 < b.xcor() < 350 and c2.ycor() + 50 > b.ycor() > c2.ycor() - 50
    if collision_c1 or collision_c2:
        b.bounce_pad()



screen.mainloop()