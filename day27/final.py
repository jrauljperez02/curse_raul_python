from tkinter import *

#create all the objects we are gonna use
window = Tk()
entry_miles = Entry()

#creating a new window and configuration
window.title('Miles to kilometers')
window.minsize(width=500,height=500)


#label1
label1 = Label(text='Introduce miles: ')
label1.pack()

#Entry
input = Entry(width=20)


def button_clicked():
    miles = input.get()






label2 = Label(text='hello')
label2.pack()








window.mainloop()