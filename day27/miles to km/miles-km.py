from tkinter import *

window = Tk()
window.title('Miles to kilometers')
window.minsize(width=300,height=150)

#First label
first_label = Label(text='is equal to',font=('Arial',12,'normal'))
first_label.grid(column=0,row=1)

#Entry point
input = Entry(width=12)
input.insert(END,string=0)
input.grid(column=1,row=0)


#result
result = Label(text='0',font=('Arial',12,'normal'))
result.grid(column=1,row=1)

#button press
def button_calculate():
    result_ = int(input.get())
    result_ *= 1.60934
    result.config(text=result_)

button = Button(text='Calculate',command=button_calculate)
button.grid(column=1,row=2)

#label miles
text_miles = Label(text='Miles',font=('Arial',12,'normal'))
text_miles.grid(column=2,row=0)

#label kilometers
text_km = Label(text='Km',font=('Arial',12,'normal'))
text_km.grid(column=2,row=1)


window.mainloop()