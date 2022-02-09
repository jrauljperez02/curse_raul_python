from re import search
from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
from turtle import tilt, title
import pyperclip
import json


BLACK = "#000016"
YELLOW = "#f7f5dd"
RED = "#e7305b"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(6,8))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]

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


    new_data = {website:{
            'email': email,
            'password': password
        }
    }
    

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops',message='Please make sure you have not left any field empty')
    else:
        is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\n \n Is it okay to save?")
    
        if is_okay:
            try:
                
                with open('data.json','r') as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open('data.json','w') as data_file:
                    json.dump(new_data, data_file,indent=4)
            
            else:
                #Updating old data with the new data
                data.update(new_data)

                    
                with open('data.json','w') as data_file:
                    #Saving update data
                    json.dump(data,data_file,indent=4)
            
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)                
                
#----------------------------FIND PASSWORD----------------------------- #

def find_password():
    website = website_entry.get()

    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
            
    except FileNotFoundError:
        messagebox.showinfo(title='Error',message='No data file found')

    else:
        if website in data:
                email = data[website]['email']
                password = data[website]['password']

                messagebox.showinfo(title=website,message=f'Email: {email}\n Password: {password}')
        else:
            messagebox.showinfo(title='Error',message=f'No details for {website} exist')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=50,bg=BLACK)

#lets create canvas
canvas = Canvas(height=200,width=200,bg=BLACK,highlightthickness=0)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=2,row=1)

#website label
website_label =  Label(text='Website:',font=(FONT_NAME,12,'normal'),bg=BLACK,fg='#ffffff')
website_label.grid(column=1,row=2)

#email label
email_label = Label(text='Email:',font=(FONT_NAME,12,'normal'),bg=BLACK,fg='#ffffff')
email_label.grid(column=1,row=3)

#password label
password_label = Label(text='Password:',font=(FONT_NAME,12,'normal'),bg=BLACK,fg='#ffffff')
password_label.grid(column=1,row=4)

#website entry
website_entry = Entry(width=24,highlightthickness=0,bg=YELLOW)
website_entry.grid(column=2,row=2)
website_entry.focus()

#email entry
email_entry = Entry(width=35,highlightthickness=0,bg=YELLOW)
email_entry.insert(0,'raul_jimenez_71@outlook.es')
email_entry.grid(column=2,row=3,columnspan=2)
#password entry
password_entry = Entry(width=24,highlightthickness=0,bg=YELLOW)
password_entry.grid(column=2,row=4)

#button to generate password
generate_password_button = Button(text='Generate Password',highlightthickness=0,width=16,command=generate_password)
generate_password_button.grid(column=3,row=4)

#add button
add_button = Button(text='Add',highlightthickness=0,width=36,command=save)
add_button.grid(column=2,row=5,columnspan=2)

#search button
search_button = Button(text='Search',highlightthickness=0,width=16,command=find_password)
search_button.grid(column=3,row=2)

window.mainloop()