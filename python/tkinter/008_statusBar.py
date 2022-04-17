from cProfile import label
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image Viewer")

#root.iconbitmap('C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\006_py.ico') 
root.iconbitmap('C:\\Users\\diego\\OneDrive\\dev\\git\\freeCodeCamp\\python\\tkinter\\') 

"""
imgs = [
    ImageTk.PhotoImage(Image.open("C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img1.jpg")),
    ImageTk.PhotoImage(Image.open("C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img2.jpg")),
    ImageTk.PhotoImage(Image.open("C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img3.jpg"))
]
"""
imgs = [
    ImageTk.PhotoImage(Image.open("C:\\Users\\diego\\OneDrive\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img1.jpg")),
    ImageTk.PhotoImage(Image.open("C:\\Users\\diego\\OneDrive\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img2.jpg")),
    ImageTk.PhotoImage(Image.open("C:\\Users\\diego\\OneDrive\\dev\\git\\freeCodeCamp\\python\\tkinter\\007_img3.jpg"))
]
index = 0
def status_bar_msg(index, len_imgs):
    return f'Image {index+1} of {len_imgs}'

def change_img_r():
    global index
    if index == len(imgs) - 1:
        index = 0
        #label1['image'] = imgs[index]
    else:
        index += 1
        #label1['image'] = imgs[index]
    label1['image'] = imgs[index]
    status_bar['text'] = status_bar_msg(index, len(imgs))

def change_img_l():
    global index
    if index == 0:
        index = len(imgs) - 1
        #label1['image'] = imgs[index]
    else:
        index -= 1
        #label1['image'] = imgs[index]
    label1['image'] = imgs[index]
    status_bar['text'] = status_bar_msg(index, len(imgs))
    #status_bar.config(text = status_bar_msg)
    

label1 = Label(image=imgs[0])
# state=DISABLED for disabled an widget
but_left = Button(root, text="<<", command=change_img_l)
but_right = Button(root, text=">>", command=change_img_r)
status_bar = Label(root, text=status_bar_msg(index, len(imgs)), bd=1, relief=SUNKEN, anchor=E)

""" change image
label['image'] = img

# or

label.config(image=img)
"""

# .grid_forget() is a function for limpar an widget
label1.grid(row=0, column=0, columnspan=2)
but_left.grid(row=1, column=0)
but_right.grid(row=1, column=1, pady=10)
# W esquerda | E direita
# para add line superior, usa bd=1, relief=SUNKEN, anchor=E no widget
status_bar.grid(row=2, column=0, columnspan=2, sticky=W+E)

root.mainloop()