from tkinter import *
import sqlite3

root = Tk()
root.title('Sqlite3')

# Databases

# Create a db or connect to one
conn = sqlite3.connect('book.db')

# create a cursor
c = conn.cursor()
c.execute("""create table addresses (
    first_name text,
    last_name text,
    address text,
    state text,
    zipcode integer
)""")


conn.commit()

conn.close()

root.mainloop()