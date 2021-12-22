import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
screen = Screen()
t.colormode(255)
tim.pensize(2)
tim.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r,g,b)
    return random_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)

draw_spirograph(3)
screen.exitonclick()