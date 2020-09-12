from tkinter import *

root = Tk()

root.geometry("500x500")
root.resizable(0, 0)


def show(e):
    root.configure(background="blue")


bt1 = Button(root, text="click", font=("Arial", 15))
bt1.grid(row=0, column=0)
bt1.bind("<Button>", show)

root.mainloop()
