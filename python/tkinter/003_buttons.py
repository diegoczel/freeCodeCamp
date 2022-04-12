from tkinter import *

def myClick():
    label1 = Label(root, text="Look! I click a Button!!")
    label1.grid(row=1, column=0)

root = Tk()

but1 = Button(root, text="button disabled", state=DISABLED)
but2 = Button(root, text="button active")
but3 = Button(root, text="change size", padx=50, pady=50) # change size
but4 = Button(root, text="call function", command=myClick)
but5 = Button(root, text="colorized", fg="blue", bg="#ffff00")

#but1.pack()
but1.grid(row=0, column=0)
but2.grid(row=0, column=1)
but3.grid(row=0, column=2)
but4.grid(row=0, column=3)
but5.grid(row=0, column=4)

root.mainloop()