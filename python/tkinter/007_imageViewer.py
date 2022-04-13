from cProfile import label
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")

root.iconbitmap('C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\006_py.ico') 

imgs = [
    ImageTk.PhotoImage(Image.open("C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img1.jpg")),
    ImageTk.PhotoImage(Image.open("C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img2.jpg")),
    ImageTk.PhotoImage(Image.open("C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img3.jpg"))
]
index = 0

#img1 = ImageTk.PhotoImage(Image.open("C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img1.jpg"))
#img2 = ImageTk.PhotoImage(Image.open("C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img2.jpg"))
#img3 = ImageTk.PhotoImage(Image.open("C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img3.jpg"))

def change_img_r():
    global index
    if index == len(imgs) - 1:
        index = 0
        label1['image'] = imgs[index]
    else:
        index += 1
        label1['image'] = imgs[index]

def change_img_l():
    global index
    if index == 0:
        index = len(imgs) - 1
        label1['image'] = imgs[index]
    else:
        index -= 1
        label1['image'] = imgs[index]

label1 = Label(image=imgs[0])
but_left = Button(root, text="<<", command=change_img_l)
but_right = Button(root, text=">>", command=change_img_r)

""" change image
label['image'] = img

# or

label.config(image=img)
"""

label1.grid(row=0, column=0)
but_left.grid(row=1, column=0)
but_right.grid(row=1, column=1)

root.mainloop()