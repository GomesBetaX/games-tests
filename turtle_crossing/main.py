from turtle import Screen
from time import sleep
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# player
player = Player()

# car manager
car_manager = CarManager()

# scoreboard
score = Scoreboard()

#commands
screen.onkeypress(player.move_up, "Up")

game_on = True
c = 0

while game_on:
    c += 1
    sleep(0.1)
    screen.update()
    score.update_score()

    # create car
    car_manager.move_cars()

    # cars according to level
    if c % 3 == 0:
        car_manager.create_car()

    # check for collision with the cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            player.reset()
            score.game_over()
            game_on = False

    # check for collision with the top wall
    if player.ycor() > 280:
        score.level_up()
        car_manager.speed += 10
        player.reset()
        # to add scores

screen.mainloop()