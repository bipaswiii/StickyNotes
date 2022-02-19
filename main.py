# Pin Your Note -Bipaswi Poudyal
# Import Necessary modules
import sqlite3 as sql
from tkinter import *
from tkinter import messagebox



# Invoke call to class to view a window
window = Tk()
# Set dimensions of window and title
window.geometry("500x300")
window.title("Pin Your Note -Bipaswi Poudyal")

title_label = Label(window, text="Pin Your Note -Bipaswi Poudyal").pack()
# Read inputs
# Date input
date_label = Label(window, text="Date:").place(x=10, y=20)
date_entry = Entry(window, width=20)
date_entry.place(x=50, y=20)
# Notes Title input
notes_title_label = Label(window, text="Notes title:").place(x=10, y=50)
notes_title_entry = Entry(window, width=30)
notes_title_entry.place(x=80, y=50)
# Notes input
notes_label = Label(window, text="Notes:").place(x=10, y=90)
notes_entry = Text(window, width=50, height=5)
notes_entry.place(x=60, y=90)

# Perform notes functions
button1 = Button(window, text='Add Notes', bg='Turquoise', fg='Red', command=add_notes).place(x=10, y=190)
button2 = Button(window, text='View Notes', bg='Turquoise', fg='Red', command=view_notes).place(x=110, y=190)
button3 = Button(window, text='Delete Notes', bg='Turquoise', fg='Red', command=delete_notes).place(x=210, y=190)
button4 = Button(window, text='Update Notes', bg='Turquoise', fg='Red', command=update_notes).place(x=320, y=190)

# close the app
window.mainloop()