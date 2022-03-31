from cgitb import text
from operator import index
import tkinter as tk
import random
from turtle import window_height

window = tk.Tk()

lst = ["money", "food", "cars", "clothes", "pets", "other"]

window.geometry("300x300")
button = tk.Button(text="click me", bg="red", fg="white")
button.pack()
def answer():
    if len(lst) == 0:
        window2 = tk.Tk()
        window2.geometry("300x300")
        label1 = tk.Label(text="you are out of options", font=("helvetica", 30))
        label1.config(bg='violet', fg='orange')
        label1.place(relx=0.5, rely=0.5, anchor='center')
    else:
        windowAnswer = tk.Tk()
        windowAnswer.geometry("300x300")
        var = random.choice(lst)
        label = tk.Label(windowAnswer, text=var)
        label.config(bg='brown', fg='green', font=32)
        label.pack()
        lst.remove(var)



button.config(command=answer)


window.mainloop()
