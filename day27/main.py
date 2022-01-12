
from tkinter import *



window = Tk()
window.title('my first app')
window.minsize(width = 500,height = 500)


#label
my_label = Label(text = 'I am a label',font=('Arial',16,'bold'))
#my_label.pack()

#to change the label
my_label['text'] = 'new text'
my_label.config(text=my_label['text'])
my_label.pack()
#my_label.place(x=100,y=0)
#my_label.grid(column=0,row=0)

#Entry - to ask for a value
input = Entry(width=20)
input.insert(END,string='insert smt')
input.pack()



#to create a button
def button_clicked():
    print('I got a clicked')
    label = input.get()
    my_label.config(text=label)
button = Button(text='click me',command=button_clicked)
button.pack()







window.mainloop()