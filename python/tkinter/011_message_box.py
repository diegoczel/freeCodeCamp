from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Message Box')

def popup():
    # conforme o tipo, tem um return especifico
    #messagebox.showinfo('Title', 'Content')
    #messagebox.showwarning('Title', 'Content')
    #messagebox.showerror('Title', 'Content')
    #messagebox.askquestion('Title', 'Content')
    #messagebox.askokcancel('Title', 'Content')
    res = messagebox.askyesno('Title', 'Content')
    if res == 1:
        label1['text'] = f'{res} is SIM'
    else:
        label1['text'] = f'{res} is NÃO'


Button(root, text='popup', command=popup).pack()
label1 = Label(root, text='')
label1.pack()
root.mainloop()