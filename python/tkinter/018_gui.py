from tkinter import *
import sqlite3

root = Tk()
root.title('Sqlite3')

# Databases

# Create a db or connect to one

def query():
    conn = sqlite3.connect('book.db')
    # create a cursor
    c = conn.cursor()

    c.execute("select oid,* from addresses")
    #c.fetchone()
    #c.fetchmany(50)
    #records = c.fetchall()
    record = ''
    for r in c.fetchall():
        record += str(r) + '\n  '
    records_label['text'] = record

    conn.commit()
    c.close()
    conn.close()

def submit():
    conn = sqlite3.connect('book.db')
    # create a cursor
    c = conn.cursor()

    # insert
    #c.execute("insert into addresses values(:f_name, :l_name, :address, :city, :state, :zipcode)",
    c.execute("insert into addresses values(:f_name, :l_name, :address, :state, :zipcode)", 
        {
            'f_name': f_name.get(),
            'l_name': l_name.get(),
            'address': address.get(),
            'state': state.get(),
            'zipcode': zipcode.get()
        }
    )

    # clear text
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    state.delete(0, END)
    #city.delete(0, END)
    zipcode.delete(0, END)
    conn.commit()
    c.close()
    conn.close()

# create input
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1)
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
#city = Entry(root, width=30)
#city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1)

# create labels
f_name_label = Label(root, text="f_name")
f_name_label.grid(row=0, column=0)
l_name_label = Label(root, text="l_name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="address")
address_label.grid(row=2, column=0)
#city_label = Label(root, text="city")
#city_label.grid(row=3, column=0)
state_label = Label(root, text="state")
state_label.grid(row=4, column=0)
zipcode_label = Label(root, text="zipcode")
zipcode_label.grid(row=5, column=0)

# submit button
submit_btn = Button(root, text="add.", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# qry button
query_btn = Button(root, text="show", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

records_label = Label(root, text="")
records_label.grid(row=8, column=0, columnspan=2)

root.mainloop()