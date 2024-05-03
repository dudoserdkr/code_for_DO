from tkinter import *


def click():
    print("Hello")


window = Tk()
window.geometry("800x800")
window.resizable(width=False, height=False)

window.config(bg='#123456')

btn = Button(window,
             text="Кнопка",
             command=click,
             font="Arial 20",
             bg="pink",
             activebackground='pink',
             fg="crimson"
             )
btn.pack()

window.mainloop()
