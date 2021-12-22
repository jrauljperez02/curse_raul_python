from turtle import Screen, Turtle, left
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

#lets create both paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#lets define what is going to do both paddles
screen.listen()
screen.onkey(r_paddle.go_up,'Up')
screen.onkey(r_paddle.go_down,'Down')


#second player 
screen.onkey(l_paddle.go_up,'w')
screen.onkey(l_paddle.go_down,'s')

ball = Ball()

#lets create both scoreboard
scoreboard = ScoreBoard()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #need to bounce 
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        #need to bounce
        ball.bounce_x()

    #detect R paddle misses
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    
    
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()
        
screen.exitonclick()