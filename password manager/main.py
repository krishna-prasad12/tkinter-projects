from tkinter import *
from tkinter import messagebox
from random import random,randint,shuffle,choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols =randint(2, 4)
    nr_numbers =randint(2, 4)


    letter_list=[choice(letters) for _ in range(randint(8, 10))]
    number_list=[choice(letters) for _ in range(randint(2, 4))]
    symbols_list=[choice(letters) for _ in range(randint(2, 4))]
    password_list=letter_list+number_list+symbols_list

    shuffle(password_list)

    password="".join(password_list)
    inp3.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website=inp1.get()
    email=inp2.get()
    password=inp3.get()
    if len(website)==0 or len(password)==0:
            messagebox.showinfo(message='Check if password or website details are empty')
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"these are the detailes entered:\n"
                                                         f"email:{email} password={password}")
        if is_ok:
            with open('data.txt','a') as file:
                file.write(f"{website} | {email} | {password}\n")
        inp1.delete(0,END)
        inp2.delete(0, END)
        inp3.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title('Password Manager')
window.config(padx=20,pady=20)
canvas=Canvas(width=200,height=200)
img=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)
lable1=Label(text='Website')
lable1.grid(row=1,column=0)
inp1=Entry(width=35)
inp1.focus()
inp1.grid(row=1,column=1,columnspan=2)
lable2=Label(text='Email/Username')
lable2.grid(row=2,column=0)
inp2=Entry(width=35)
inp2.insert(0,'example.gmail.com')
inp2.grid(row=2,column=1,columnspan=2)
lable3=Label(text='Password')
lable3.grid(row=3,column=0)
inp3=Entry(width=35)
inp3.grid(row=3,column=1,columnspan=2)
but1=Button(text='Generate password',command=gen_pass)
but1.grid(row=3,column=2)
but2=Button(text='Add',width=36,command=save_data)
but2.grid(row=4,column=1,columnspan=2)









window.mainloop()