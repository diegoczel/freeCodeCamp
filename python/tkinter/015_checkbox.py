from tkinter import *

root = Tk()
root.title('Checbox')

def check_value():
    label1['text'] = check1_v.get()

check1_v = IntVar()
# onvalue="On" when it's checked
# offvalue="Off" when it's is not checked
# check1.deselect() for default uncheckd check
check1 = Checkbutton(root, text="Check 1", variable=check1_v, command=check_value)
label1 = Label(root, text=check1_v.get())

check1.grid(row=0, column=0)
label1.grid(row=0, column=1)

root.mainloop()