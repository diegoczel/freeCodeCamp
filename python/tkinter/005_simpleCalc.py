from tkinter import *

root = Tk()
root.title("Calculadora")

entrada = Entry(root, width=35, borderwidth=5)
entrada.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def but_click(number):
    current = entrada.get()
    entrada.delete(0, END)
    entrada.insert(0, current +  str(number))

def but_clear_screen():
    entrada.delete(0, END)

def but_fun_add():
    first_number = entrada.get()
    global f_num
    global op
    op = "+"
    f_num = int(first_number)
    entrada.delete(0, END)

def but_fun_sub():
    first_number = entrada.get()
    global f_num
    global op
    op = "-"
    f_num = int(first_number)
    entrada.delete(0, END)

def but_fun_mul():
    first_number = entrada.get()
    global f_num
    global op
    op = "*"
    f_num = int(first_number)
    entrada.delete(0, END)

def but_fun_div():
    first_number = entrada.get()
    global f_num
    global op
    op = "/"
    f_num = int(first_number)
    entrada.delete(0, END)
    
def but_fun_equal():
    second_number = entrada.get()
    entrada.delete(0, END)

    if op == '+':
        entrada.insert(0, f_num + int(second_number))
    if op == '-':
        entrada.insert(0, f_num - int(second_number))
    if op == '*':
        entrada.insert(0, f_num * int(second_number))
    if op == '/':
        entrada.insert(0, f_num / int(second_number))

but_1 = Button(root, text="1", padx=40, pady=20, command=lambda: but_click(1))
but_2 = Button(root, text="2", padx=40, pady=20, command=lambda: but_click(2))
but_3 = Button(root, text="3", padx=40, pady=20, command=lambda: but_click(3))
but_4 = Button(root, text="4", padx=40, pady=20, command=lambda: but_click(4))
but_5 = Button(root, text="5", padx=40, pady=20, command=lambda: but_click(5))
but_6 = Button(root, text="6", padx=40, pady=20, command=lambda: but_click(6))
but_7 = Button(root, text="7", padx=40, pady=20, command=lambda: but_click(7))
but_8 = Button(root, text="8", padx=40, pady=20, command=lambda: but_click(8))
but_9 = Button(root, text="9", padx=40, pady=20, command=lambda: but_click(9))
but_0 = Button(root, text="0", padx=40, pady=20, command=lambda: but_click(0))
but_add = Button(root, text="+", padx=40, pady=20, command=lambda: but_fun_add())
but_equal = Button(root, text="=", padx=90, pady=20, command=lambda: but_fun_equal())
but_clear = Button(root, text="Clear", padx=80, pady=20, command=but_clear_screen)

but_sub = Button(root, text="-", padx=40, pady=20, command=lambda: but_fun_sub())
but_mul = Button(root, text="*", padx=40, pady=20, command=lambda: but_fun_mul())
but_div = Button(root, text="/", padx=40, pady=20, command=lambda: but_fun_div())

but_7.grid(row=1, column=0)
but_8.grid(row=1, column=1)
but_9.grid(row=1, column=2)

but_4.grid(row=2, column=0)
but_5.grid(row=2, column=1)
but_6.grid(row=2, column=2)

but_1.grid(row=3, column=0)
but_2.grid(row=3, column=1)
but_3.grid(row=3, column=2)

but_0.grid(row=4, column=0)
but_clear.grid(row=4, column=1, columnspan=2)

but_add.grid(row=5, column=0)
but_equal.grid(row=5, column=1, columnspan=2)

but_sub.grid(row=6, column=0)
but_mul.grid(row=6, column=1)
but_div.grid(row=6, column=2)

root.mainloop()