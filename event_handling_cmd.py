from tkinter import *

root = Tk()
r = 1
c = 0


def show():
    global r, c

    for r in range(1, 5):
        for c in range(0, 5):
            bt2 = Button(root, text="click me", font=("Arial", 15))
            bt2.grid(row=r, column=c)
            c += 1
        r += 1


root.geometry("500x500")
root.resizable(0, 0)
bt1 = Button(root, text="click", font=("Arial", 15), command=show)
bt1.grid(row=0, column=0)

root.mainloop()
