from tkinter import *


root = Tk()
root.title('Titulo')


# control when open new window
def open_window():
    top = Toplevel()
    top.title("top Window")
    label1 = Label(top, text="text in window top").grid(row=0, column=0)
    button2 = Button(top, text="close window using destroy", command=top.destroy)

button1 = Button(root, text="open new window", command=open_window).grid(row=0, column=0)


root.mainloop()