from turtle import Turtle, Screen
from paddle import Paddle
from dash import Dash
from ball import Ball
from score_board import Scoreboard
import time

# Screen settings
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.bgcolor("black")

# refresh rate
screen.tracer(0)
screen.listen()

# create Paddle
pad_pc = Paddle("PC")
pad_user = Paddle("USER")

# create score
score = Scoreboard()

# create ball
b = Ball()

# create line
d = Dash()
d.draw_dash()

# movements
screen.onkeypress(pad_user.up, "Up")
screen.onkeypress(pad_user.down, "Down")


# game settings
while True:
    screen.update()
    time.sleep(0.05)  # 10 FPS  

    # write score
    score.update_score()

    # pc_pc_moving
    pad_pc.move() 
    b.move()
    

    # detect pc_paddle collision with wall
    for pad in pad_pc.paddle:
        if pad.ycor() >= 270 or pad.ycor() <= -270:
            if pad.ycor() >= 250:
                pad.setheading(270)
            elif pad.ycor() <= -250:
                pad.setheading(90)

    # detect ball collision with wall
    bxcor = b.xcor()
    bycor = b.ycor()
    
    if bxcor >= 390 or bxcor <= -390:
        if bxcor > 0:
            score.add_score("USER")
            b.reset_ball()
            time.sleep(0.5)
        else:
            score.add_score("PC")
            b.reset_ball()
            time.sleep(0.5)
        # b.reset_heading("horizontal")
    
    if bycor >= 290 or bycor <= -290:
        b.reset_heading("vertical")

    # detect ball collision with paddle_PC
    for pad in pad_pc.paddle:
        if pad.distance(b) <= 10:
            b.reset_heading("horizontal")
    
    # detect ball collision with user_paddle
    for pad in pad_user.paddle:
        if pad.distance(b) <= 10:
            b.reset_heading("horizontal")

screen.mainloop()