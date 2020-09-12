from tkinter import *
from tkinter import messagebox


root = Tk()
root.geometry("500x500")
root.resizable(0, 0)

# defining command on login button


def do():
    messagebox.showinfo("login", "You are logged in")


lab1 = Label(root, text="Enter name", font=("Arial", 15))
lab1.grid(row=0, column=0, pady=50, sticky=W)

en1 = Entry(root, font=("Arial", 15))
en1.grid(row=0, column=1, pady=25)

lab2 = Label(root, text="Enter Password", font=("Arial", 15))
lab2.grid(row=1, column=0)

en2 = Entry(root, show="*", font=("Arial", 15))
en2.grid(row=1, column=1)

b1 = Button(root, text="Login", font=("Arial", 15), command=do)
b1.grid(row=2, column=0, pady=25, columnspan=2)

root.mainloop()
