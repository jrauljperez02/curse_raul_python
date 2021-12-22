from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Score_board
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

#create an object call Snake, Food
snake = Snake()
food = Food()
scoreboard = Score_board()


#lets code the methods to be able to move our snake
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect when happen a colision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        scoreboard.increse_score()
        snake.extend()
    #detect when happen a collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.gameOver()

    #detect when snake hit whit collision with his own tail
    #if head collides with any segments in the tail
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameOver()


screen.exitonclick()


