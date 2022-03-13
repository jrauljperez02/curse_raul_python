import turtle
import pandas
from pandas import core

screen = turtle.Screen()
screen.title('U.S. States Game')


image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#this is use to know the position in the map of each state
'''
def get_mouse_click_coor(x,y):
    print(x,y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

'''
#read information from states list
data = pandas.read_csv('50_states.csv')

game_on = True

while game_on:
    correct_answers_list = []
    answer_state = screen.textinput(title='Guess the State',prompt="What's another state's name?")
    
    if answer_state == 'exit':
        game_on = False
    
    #create a turtle
    t = turtle.Turtle()
    for state in data['state']:
        if state.lower() == answer_state:
            x_coord = int(data[data.state == state]['x'])
            y_coord = int(data[data.state == state]['y']) 
            list_position = (x_coord,y_coord)
            #print(list_position)
        
            t.penup()
            t.goto(list_position)
            t.hideturtle()
            t.write(f'{answer_state}')

    correct_answers_list.append(answer_state)
    
    print(correct_answers_list)


screen.exitonclick()
        


