import random
from turtle import Turtle

import random
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1


    def move(self):
        random_x = self.xcor() + self.x_move
        random_y = self.ycor() + self.y_move
        self.goto(random_x,random_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()