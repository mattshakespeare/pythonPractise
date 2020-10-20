import random
from tkinter import *

def clear():
    table.delete(0,END)
    table.focus

def view_table():
    num = ent_bx.get()
    num = int(num)
    x = 1
    ans = 0
    for i in range(12):
        ans = x * num
        table.insert(END,(x, "x", num, "=", ans))
        x += 1
    table.focus()


window = Tk()
window.geometry("700x300")
window.title("Times Table")

ent_lbl = Label(text = "Enter a number: ")
ent_lbl.place(x = 10, y = 10, width = 200, height = 25)

ent_bx = Entry(text = 0)
ent_bx.place(x = 220, y = 10, width = 200, height = 25)
ent_bx["justify"] = "left"
ent_bx.focus()

view_btn = Button(text = "View Times Table", command = view_table)
view_btn.place(x = 430, y = 10, width = 200, height = 25)
view_btn.focus()

table = Listbox()
table.place(x = 220, y = 50, width = 200, height = 250)

clear_btn = Button(text = "Clear", command = clear)
clear_btn.place(x = 430, y = 50, width = 200, height = 25)

window.mainloop()


