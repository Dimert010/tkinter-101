import tkinter

window = tkinter.Tk()
size = 0
Counter = 0
kleur = ['red', 'blue', 'pink', 'violet', 'black', 'orange']

window.title('achtergornd en grote veranderd')
window.config(bg = 'red')
def color():
    global size, Counter
    index = int(size/50)
    if index == len(kleur):
        print('biieeeem!')
        window.destroy()
    else:
        Counter += 1
        size += 50
        window.config(bg=kleur[index])
        window.geometry(f'{size}x{size}')
        window.after(2000, color)
        print(f'{Counter}')

color()
window.mainloop()