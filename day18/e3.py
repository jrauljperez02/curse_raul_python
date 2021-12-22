from turtle import Screen, Turtle
import random

line = Turtle()
screen = Screen()

num_sides = 3
colours = ["dark blue","dark green","chocolate","blue violet"]

def draw(num_sides):
    angle = 360 / num_sides
    for _ in range (num_sides):
        line.forward(100)
        line.right(angle)


for side in range(3,11):
    draw(side)
    line.color(random.choice(colours))

screen.exitonclick()