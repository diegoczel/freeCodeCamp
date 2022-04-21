from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

# Select an location of a file, then open this using othres ways, like PIL, open().

root = Tk()
root.title('Files')
root.filename = ''

"""on exec, launch this dialog in screen
root.filename = filedialog.askopenfilename(
    initialdir='C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\', 
    title="Select a file", 
    filetypes=(
        ('jpg files', '*.jpg'), 
        ('all files', '*.*')
    )
)
"""
def open_file():
    global img1
    root.filename = filedialog.askopenfilename(
        # initial dir using an away for get the current path of file in exec
        initialdir='C:\\dev\\git\\freeCodeCamp\\python\\tkinter\\', 
        title="Select a file", 
        filetypes=(
            ('jpg files', '*.jpg'), 
            ('all files', '*.*')
        )
    )
    # need global using image
    img1 = ImageTk.PhotoImage(Image.open(root.filename))

    label1 = Label(root, text=root.filename).pack()
    label2 = Label(image=img1).pack()

but1 = Button(text='Open a file', command=open_file).pack()


root.mainloop()