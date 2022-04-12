from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("IMAGE")

# icon is a .ico file
root.iconbitmap('C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\006_py.ico') 

# using images
# need use module Pillow
# and need use a Label with a img
img1 = ImageTk.PhotoImage(Image.open('C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\006_py.ico'))
label1 = Label(image=img1)

# quit button
but_quit = Button(root, text="Exit", command=root.quit)

label1.grid(row=0, column=0)
but_quit.grid(row=0, column=1)

root.mainloop()