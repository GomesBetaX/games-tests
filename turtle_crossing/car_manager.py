from turtle import Turtle
from random import choice, randint
from time import sleep

COLORS = [
    "white", "black", "gray", "lightgray", "darkgray",
    "red", "darkred", "firebrick", "salmon", "tomato",
    "orange", "darkorange", "coral", "gold", "yellow",
    "lightyellow", "khaki", "green", "darkgreen", "lime",
    "forestgreen", "olive", "chartreuse", "cyan", "turquoise",
    "lightblue", "skyblue", "deepskyblue", "dodgerblue", "blue",
    "darkblue", "navy", "purple", "indigo", "violet",
    "plum", "magenta", "fuchsia", "pink", "hotpink",
    "deeppink", "brown", "maroon", "beige", "tan",
    "wheat", "sienna", "chocolate", "peru", "slategray"
]

LEVEL = [2, 5, 7, 10, 12, 15]
CAR_SPEED = [10, 20, 30, 40, 50, 60]

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed = 10
        self.cars = []

    def create_car(self):
        #standard creation            
        car = Turtle("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(choice(COLORS))
        car.penup()
        car.goto(300, randint(-240, 240))
        car.setheading(180)
        self.cars.append(car)
        sleep(0.1)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.speed)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars.remove(car)