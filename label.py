from tkinter import *

root = Tk()
root.geometry("500x500")
root.resizable(0, 0)
lab = Label(root, text="Welcome", font=("Algerian", 30),
            bg="red", fg="white", width="15", height="1")
lab.pack()

root.mainloop()
