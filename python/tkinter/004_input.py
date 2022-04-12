from tkinter import *

root = Tk()

label1 = Label(root, text="Label 1 :")
input1 = Entry(root)

label2 = Label(root, text="input width: ")
input2 = Entry(root, width=100)

label3 = Label(root, text="border width: ")
input3 = Entry(root, borderwidth=5)

input4 = Entry(root)
def changeContent():
    label5 = Label(root, text=input4.get())
    label5.grid(row=3, column=2)
but1 = Button(root, text="change content", command=changeContent)

label6 = Label(root, text="Entry.insert()")
input5 = Entry(root)
input5.insert(0, "default")

label1.grid(row=0, column=0)
input1.grid(row=0, column=1)

label2.grid(row=1, column=0)
input2.grid(row=1, column=1)

label3.grid(row=2, column=0)
input3.grid(row=2, column=1)

but1.grid(row=3, column=0)
input4.grid(row=3, column=1)

label6.grid(row=4, column=0)
input5.grid(row=4, column=1)



root.mainloop()