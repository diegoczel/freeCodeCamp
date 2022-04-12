from tkinter import *

root = Tk()

# grid has row and col

label1 = Label(root, text="label1")
label2 = Label(root, text="label2")
label3 = Label(root, text="label3").grid(row=2, column=1)

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

root.mainloop()