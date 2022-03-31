from cProfile import label
from curses import window
from turtle import width


number = 0

def plus():
    global number
    number += 1
    color()

def minus():
    global number
    number -= 1
    color()

def color():
    global number
    label.configure(text=number)
    if number == 0:
        label.configure(bg='green')
    elif number < 0:
        label.configure(bg='red')
    else:
        label.configure(bg='blue')


import tkinter

window = tkinter.Tk()
window.geometry('200x200')

label = tkinter.Label(text=f"{number}", bg= 'violet', fg='white', font=('danger', 20))
label.place(relx=0.5, rely=0.5, anchor='center')

button = tkinter.Button(text='+', bg='green', fg='white', width=20, height=5)
button.configure(command=plus)
button.pack(side=tkinter.TOP)

button1 = tkinter.Button(text='-', bg='red', fg='white', width=20, height=5)
button1.configure(command=minus)
button1.pack(side=tkinter.BOTTOM)

window.mainloop()