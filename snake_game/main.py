# Goal: make a snake game
from food import Food
from score import Scoreboard
import time
from snake import Snake
from turtle import Turtle, Screen

# Settings
    # screen
s = Screen()
 # sets screen to listen for user input
s.tracer(0)  # turns off the screen updates
s.setup(width=600, height=600) # sets screen height and width
s.bgcolor("black") #sets background color
s.title("Snake Game") #sets window title

    # objects
cobra = Snake(s)
food = Food()
score = Scoreboard()

# ---------------------- START THE CODE ------------------------#

# commands
s.onkey(cobra.up, "Up")
s.onkey(cobra.down, "Down")
s.onkey(cobra.left, "Left")
s.onkey(cobra.right, "Right")

s.listen()

should_continue_game = True
while should_continue_game:
    # screen updates
    s.update()
    time.sleep(0.1)


    # snake moves
    cobra.move()

    # detect collision with food
    if cobra.segments[0].distance(food) <= 15:
        food.new_position()

        # add new segment
        cobra.add_segment()

        # add new score
        score.add_score()

    # detects collision with self
    for segment in cobra.segments[1:]:
        if cobra.segments[0].distance(segment) <= 10:
            score.game_over()
            should_continue_game = False

    # detect collision with wall
    x = cobra.segments[0].xcor()
    y = cobra.segments[0].ycor()
    if ((x <= -300.05) or (x >= 298)) or ((y <= -290) or (y >= 300.001)):
        score.game_over()
        print("You hit a wall, therefore you lost.")
        should_continue_game = False

# exit when window is closed
s.mainloop()

