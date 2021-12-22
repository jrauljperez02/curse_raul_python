import turtle as  t

tim =  t.Turtle()
scren = t.Screen()

for _ in range (12):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


scren.exitonclick()

