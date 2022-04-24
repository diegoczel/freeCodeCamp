from tkinter import *

root = Tk()
root.title('Dropdown menu')
root.geometry('800x600')

drop_var = StringVar()
drop_var.set("Seg")
#drop = OptionMenu(root, drop_var, lista_itens)
drop = OptionMenu(root, drop_var, "Seg", "Ter", "Qua")
print(dir(drop_var))
drop.pack()

root.mainloop()