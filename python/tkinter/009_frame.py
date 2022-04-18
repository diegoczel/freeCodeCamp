from cProfile import label
from tkinter import *

root = Tk()
root.title('Frames')

# frame is similar to div

# del text for a frame within text
frame = LabelFrame(root, text="This is my frame...", padx=5, pady=5)

label1 = Label(root, text="root - Label1")
label2 = Label(frame, text="frame - Label2")
label3 = Label(frame, text="frame - Label3")
label4 = Label(root, text="root - Label4")

label1.grid(row=0, column=0)
frame.grid(row=1, column=0)
# this position is relative to frame
label2.grid(row=0, column=0)
label3.grid(row=1, column=0)

label4.grid(row=2, column=0)

root.mainloop()