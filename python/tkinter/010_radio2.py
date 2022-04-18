from tkinter import *

root = Tk()

sex = StringVar()
sex.set("I")

def clicked(v):
    label1['text'] = f"Sexo Selecionado: {v} : "

frame_sex = LabelFrame(root, text="")
label1 = Label(frame_sex, text="Sexo Selecionado: I : ")
label1.grid(row=0, column=0)
Radiobutton(frame_sex, text="I", variable=sex, value="I", command= lambda : clicked(sex.get())).grid(row=0, column=1)
Radiobutton(frame_sex, text="M", variable=sex, value="M", command= lambda : clicked(sex.get())).grid(row=0, column=2)
Radiobutton(frame_sex, text="F", variable=sex, value="F", command= lambda : clicked(sex.get())).grid(row=0, column=3)

frame_sex.grid(row=0, column=0)

root.mainloop()