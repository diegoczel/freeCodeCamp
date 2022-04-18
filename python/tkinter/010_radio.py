from tkinter import *

root = Tk()
root.title('Radio')

r = IntVar()
r.set("1")

def clicked(v):
    label1['text'] = v

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda : clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda : clicked(r.get())).pack()

label1 = Label(root, text=r.get())
label1.pack()

root.mainloop()