from tkinter import *

window = Tk()
window.title('Challenge')
window.minsize(width = 500,height = 500)

#label
my_label = Label(text = 'Label',font=('Arial',16,'bold'))
my_label.grid(column =0,row =0)

#first button
def button_clicked():
    my_label.config('Hello 1 ')

button1 = Button(text = 'Button1',command=button_clicked)
button1.grid(column =1,row =1)


#second button
button2 =  Button(text = 'Button2',command=button_clicked)
button2.grid(column =3,row =0)

#Entry point
input = Entry(width =10)
input.grid(column=4,row =2)



window.mainloop()