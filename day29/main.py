import imp
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(3,6))]
    password_symbols = [choice(symbols) for _ in range(randint(3,6))]

    password_list = password_symbols + password_numbers + password_letters
    shuffle(password_list)

    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops',message='Please make sure you have not left any field empty')
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\n \n Is it okay to save?")

        if is_okay:
            with open('data.txt','a') as data_file:
                data_file.write(f'{website} // {email} // {password}\n' )
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

#lets create canvas
canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=2,row=1)

#website label
website_label =  Label(text='Website:',font=('Arial',12,'normal'))
website_label.grid(column=1,row=2)

#email label
email_label = Label(text='Email:',font=('Arial',12,'normal'))
email_label.grid(column=1,row=3)

#password label
password_label = Label(text='Password:',font=('Arial',12,'normal'))
password_label.grid(column=1,row=4)

#website entry
website_entry = Entry(width=35)
website_entry.grid(column=2,row=2,columnspan=2)
website_entry.focus()

#email entry
email_entry = Entry(width=35)
email_entry.insert(0,'@gmail.com')
email_entry.grid(column=2,row=3,columnspan=2)
#password entry
password_entry = Entry(width=21)
password_entry.grid(column=2,row=4)

#button to generate password
generate_password_button = Button(text='Generate Password',highlightthickness=0,width=12,command=generate_password)
generate_password_button.grid(column=3,row=4)

#add button
add_button = Button(text='Add',highlightthickness=0,width=36,command=save)
add_button.grid(column=2,row=5,columnspan=2)

window.mainloop()