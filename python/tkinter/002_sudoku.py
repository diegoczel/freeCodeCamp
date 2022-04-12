from tkinter import *

root = Tk()

labels = []
r = 0
c = 0
for x in range(0, 9):
    if x % 3 == 0:
        r += 1
        c = 0
    
    labels.append(Label(root, text=f"{x+1}").grid(row=r, column=c))
    c += 1

root.mainloop()