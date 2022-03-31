from cProfile import label
from re import S
import tkinter as tk
from time import strftime

window = tk.Tk()

window.geometry("450x70")
label = tk.Label(window, font=("terminal", 48), bg='darkblue', fg='yellow')
label.pack()
def counter():
    tijd = strftime('%H:%M:%S')
    var = tk.StringVar(value=tijd)
    label.config(textvariable=var)

    window.after(1000, counter)

counter()

window.mainloop()