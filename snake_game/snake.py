from turtle import Turtle
import time

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():
    def __init__(self):
        # self.screen = 
        self.segments = []
        self.create_snake()
        self.heading = 0

    # movements
    def up(self):
        if self.heading != DOWN:
            self.heading = 90

    def down(self):
        if self.heading !=  UP:
            self.heading = 270

    def left(self):
        if self.heading != RIGHT:
            self.heading = 180

    def right(self):
        if self.heading != LEFT:
            self.heading = 0

    def add_segment(self):

        last_segment_x = self.segments[-1].xcor()
        last_segment_y = self.segments[-1].ycor()

        new_square = Turtle()
        new_square.penup()
        new_square.shape("square")
        new_square.color("white")
        new_square.pen()
        new_square.goto(-20 * last_segment_x, last_segment_y)
        self.segments.append(new_square)

    # create the snake itself
    def create_snake(self):
        for i in range(3):
            new_square = Turtle()
            new_square.shape("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(-20 * i, 0)
            self.segments.append(new_square)
        # screen.update()

    # moves the snake continously
    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            next_pos = self.segments[i - 1].pos()
            head_heading = self.segments[i - 1].heading()
            self.segments[i].goto(next_pos)


        # moves snake forward
        self.segments[0].setheading(self.heading)
        self.segments[0].fd(20)
    
    # resets snake
    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        
        self.segments.clear()
        self.create_snake()