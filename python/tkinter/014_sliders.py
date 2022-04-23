from tkinter import *

root = Tk()
root.title('Slider')
#root.geometry("1920x1080")

def rgb_to_hex(r, g, b):
    color_hex = '#'
    # hex() < 16 return one digit, then add 0 at left
    color_hex += '0' + hex(r)[2:] if r < 16 else hex(r)[2:]
    color_hex += '0' + hex(g)[2:] if g < 16 else hex(g)[2:]
    color_hex += '0' + hex(b)[2:] if b < 16 else hex(b)[2:]
    return color_hex

def scale_set(v):
    # Scale command need arg into funcion
    label1['bg'] = rgb_to_hex(scale_r.get(), scale_g.get(), scale_b.get())

def but_scale_set(l_or_r, scale):
    if l_or_r == 'l':
        if scale.get() > 0:
            scale.set(scale.get() - 1)
    elif l_or_r == 'r':
        if scale.get() < 255:
            scale.set(scale.get() + 1)
    label1['bg'] = rgb_to_hex(scale_r.get(), scale_g.get(), scale_b.get())

but_l_r = Button(root, text="<<", command=lambda : but_scale_set('l', scale_r))
scale_r = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=scale_set)
but_r_r = Button(root, text=">>", command=lambda : but_scale_set('r', scale_r))

but_l_g = Button(root, text="<<", command=lambda : but_scale_set('l', scale_g))
scale_g = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=scale_set)
but_r_g = Button(root, text=">>", command=lambda : but_scale_set('r', scale_g))

but_l_b = Button(root, text="<<", command=lambda : but_scale_set('l', scale_b))
scale_b = Scale(root, from_=0, to=255, orient=HORIZONTAL, command=scale_set)
but_r_b = Button(root, text=">>", command=lambda : but_scale_set('r', scale_b))

label1 = Label(root, text='', font="Times 10", width=40, height=3, bg="#000000")

but_l_r.grid(row=0, column=0)
scale_r.grid(row=0, column=1)
but_r_r.grid(row=0, column=2)

but_l_g.grid(row=1, column=0)
scale_g.grid(row=1, column=1)
but_r_g.grid(row=1, column=2)

but_l_b.grid(row=2, column=0)
scale_b.grid(row=2, column=1)
but_r_b.grid(row=2, column=2)

label1.grid(row=0, column=4, rowspan=3)

root.mainloop()