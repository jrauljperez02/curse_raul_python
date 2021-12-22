from turtle import Screen,Turtle, pos
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake game')
screen.tracer(0)
starting_position = ((0,0),(-20,0),(-40,0))

segments = []
#code to creake our snake
for position in starting_position:
    new_squre = Turtle('square')
    new_squre.color('white')
    new_squre.penup()
    new_squre.goto(position)
    segments.append(new_squre)

#code to go forward
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
   #for seg_num in range(start=2,stop=0,step=-1):
    for seg_num in range(len(segments) -1,0,-1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    
    segments[0].forward(20)

screen.exitonclick()