from tkinter import *

window = Tk()
window.title('my first app')
window.minsize(width = 500,height = 500)

#label
my_label = Label(text = 'I am a label',font=('Arial',16,'bold'))
my_label.config(text='New text')
my_label.grid(column=0,row=0)

#Entry
input = Entry(width=12)
input.grid(column=2,row=2)


#Button
def button_clicked():
    print('I got a clicked')
    label = input.get()
    my_label.config(text=label)

button = Button(text='click me',command=button_clicked)
button.grid(column=0,row=1)



window.mainloop()