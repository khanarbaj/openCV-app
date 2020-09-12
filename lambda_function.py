from tkinter import *

window = Tk()

window.geometry("500x500")
window.resizable(0, 0)

# Making lambda fuctions


def show1(e): return window.configure(background="red")


def show2(e): return window.configure(background="green")


def show3(e): return window.configure(background="blue")


bt1 = Button(window, text="click", font=("Arial", 20))
bt1.pack()

# Binding the button to perform the cammnd

bt1.bind("<Button-1>", show1)  # for left click
bt1.bind("<Button-2>", show2)  # for middle click
bt1.bind("<Button-3>", show3)  # for right click

window.mainloop()
