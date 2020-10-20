from tkinter import *


#def click():
#    name = enttxt.get()
#    name = str("Hello " + name)
#    output["text"] = name
#    output.focus()

#window = Tk()
#window.geometry("600x400")
#window.title("My Logo")
#window.wm_iconbitmap("IMG_1037.png")
#window.configure(background = "light green")

#logo = PhotoImage(file = "IMG_1037.png")
#logolbl = Label(image = logo)
#logolbl.place(x = 100, y = 50, width = 400, height = 200 )

#entlbl = Label(text = "Enter your name: ")
#entlbl.place(x = 20, y = 300, width = 150, height = 25)
#entlbl["bg"] = "light gray"

#enttxt = Entry(text = "")
#enttxt.place(x = 170, y = 300, width = 250, height = 25)
#enttxt["justify"] = "left"
#enttxt.focus()

#button = Button(text = "Press Me", command = click)
#button.place(x = 20, y = 350, width = 150, height = 25)
#button["bg"] = "light gray"
#button.focus()

#output = Message(text = "")
#output.place(x = 170, y = 350, width = 250, height = 100)

#window.mainloop()

import random

#def checkans():
#    theirans = ansbox.get()
#    theirans = int(theirans)
#    num1 = num1box["text"]
#    num1 = int(num1)
#    num2 = num2box["text"]
#    num2 = int(num2)
#    ans = num1 + num2
#    if theirans == ans:
#        img = PhotoImage(file = "tick.png")
#        imgbx.image = img
#    else:
#        img = PhotoImage(file = "cross.png")
#        imgbx.image = img
#    imgbx["image"] = img
#    imgbx.update()

#def nextquestion():
#    ansbox.delete(0, END)
#    num1 = random.randint(10, 50)
#    num1box["text"] = num1
#    num2 = random.randint(10, 50)
#    num2box["text"] = num2
#    img = PhotoImage(file = "")
#    imgbx.image = img
#    imgbx["image"] = img
#    imgbx.update()

#window = Tk()
#window.title("Addition")
#window.geometry("250x300")

#num1box = Label(text = "0")
#num1box.place(x = 50, y = 30, width = 25, height = 25)
#addsymbol = Message(text = "+")
#addsymbol.place(x = 75, y = 30, width = 25, height = 25)
#num2box = Label(text = "0")
#num2box.place(x = 100, y = 30, width = 25, height = 25)
#eqlsymbol = Message(text = "=")
#eqlsymbol.place(x = 125, y = 30, width = 25, height = 25)
#ansbox = Entry(text = "")
#ansbox.place(x = 150, y = 30, width = 25, height = 25)
#ansbox["justify"] = "center"
#ansbox.focus()
#checkbtn = Button(text = "Check", command = checkans)
#checkbtn.place(x = 50, y = 60, width = 75, height = 25)
#nextbtn = Button(text = "Next", command = nextquestion)
#nextbtn.place(x = 130, y = 60, width = 75, height = 25)
#img = PhotoImage(file = "")
#imgbx = Label(image = img)
#imgbx.image = img
#imgbx.place(x = 25, y = 100, width = 200, height = 150)

#nextquestion()

#window.mainloop()

#def col():
#    colour = selectCol.get()
#    window.configure(background = colour)
#    window.update()


#window = Tk()
#window.geometry("300x200")
#window.title("Background Colour")

#selectCol = StringVar(window)
#selectCol.set("Select Colour")
#colList = OptionMenu(window, selectCol, "red", "yellow", "green", "blue")
#colList.place(x = 10, y = 100)

#click = Button(text = "Click me", command = col)
#click.place(x = 150, y = 100, width = 100, height = 25)
#click.focus()

#window.mainloop()

#def add_to_list():
#    name = ent_txt.get()
#    gender = selGender.get()
#    entry = name + "," + gender + "\n"
#    list_box.insert(END, entry)
#    file = open("names.txt", "a")
#    file.write(entry)
#    file.close()

#def print_():
#    file = open("names.txt", "r")
#    print(file.read())
#    file.close()


#window = Tk()
#window.title("Name and gender list")
#window.geometry("600x450")

#ent_lbl = Message(text = "Enter name: ")
#ent_lbl.place(x = 5, y = 20, width = 150, height = 25)
#ent_lbl["bg"] = "light gray"
#ent_lbl["relief"] = "raised"

#ent_txt = Entry(text = "")
#ent_txt.place(x = 155, y = 20, width = 200, height = 25)
#ent_txt["justify"] = "left"
#ent_txt.focus()

#selGender = StringVar(window)
#selGender.set("Gender")
#genderLst = OptionMenu(window, selGender, "Female", "Male")
#genderLst.place(x = 155, y = 50, width = 200, height = 25)
#genderLst.focus()

#add_lst = Button(text = "Add to List", command = add_to_list)
#add_lst.place(x = 155, y = 90, width = 200, height = 25)
#add_lst["bg"] = "light gray"
#add_lst["relief"] = "raised"
#add_lst.focus()

#list_box = Listbox()
#list_box.place(x = 155, y = 120, width = 300, height = 300)
#list_box.focus()

#print_button = Button(text = "Print list", command = print_)
#print_button.place(x = 5, y = 90, width = 150, height = 25)
#print_button["bg"] = "light gray"
#print_button["relief"] = "raised"
#print_button.focus()

#window.mainloop()

def click():
    img = planet_ent.get()
    if int(img) == 1 or int(img) == 2 or int(img) == 3:
        planet = PhotoImage(file = str(img + ".png"))
        planetlbl.image = planet
        planetlbl["image"] = planet
        planetlbl.update()

window = Tk()
window.title("Planet Images")
window.geometry("800x800")
window.configure(background = "black")

planet = PhotoImage(file = "1.png")
planetlbl = Label(image = planet)
planetlbl.place(x = 200, y = 300, height = 400, width = 400)

optlbl = Label(text = "Choose 1,2 or 3:")
optlbl.place(x = 100, y = 150, width = 200, height = 50)
optlbl["bg"] = "light blue"
optlbl["relief"] = "raised"

planet_ent = Entry(text = "")
planet_ent.place(x = 300, y = 150, width = 100, height = 50)
t1planet_ent["justify"] = "left"
planet_ent.focus()

clck = Button(text = "Click me", command = click)
clck.place(x = 400, y = 150, width = 150, height = 50)
clck["bg"] = "light blue"
clck["relief"] = "raised"
clck.focus()

window.mainloop()
