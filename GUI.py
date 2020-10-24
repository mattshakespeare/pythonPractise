from tkinter import *
# just to practise changes
#def click():
#    name = textbox1.get()
#    message = str("Hello " + name)
#    textbox2["bg"] = "yellow"
#    textbox2["fg"] = "blue"
#    textbox2["text"] = message

#window = Tk()
#window.geometry("500x200")

#label1 = Label(text = "Enter your name: ")
#label1.place(x = 30, y = 20)

#textbox1 = Entry(text = "")
#textbox1.place(x = 150, y = 20, width = 200, height = 25)
#textbox1["justify"] = "center"
#textbox1.focus()

#button1 = Button(text = "Press Me", command = click)
#button1.place(x = 30, y = 50, width = 120, height = 25)

#textbox2 = Message(text = "")
#textbox2.place(x = 150, y = 50, width = 200, height = 75)
#textbox2["bg"] = "white"
#textbox2["fg"] = "black"

#window.mainloop()

# output window, button
# press a button that rolls a dice and outputs the number the dice lands on

import random

#def click():
#    num = random.randint(1,6)
#    answer["text"] = num

#window = Tk()
#window.title("Roll a dice")
#window.geometry("100x120")

#button1 = Button(text = "Roll", command = click)
#button1.place(x = 150, y = 20, width = 200, height = 25)

#answer = Message(text = "")
#answer.place(x = 40, y = 70, width = 30, height = 25)

#window.mainloop()


#def add_on():
#    num = enter_txt.get()
#    num = int(num)
#    answer = output_txt["text"]
#    answer = int(answer)
#    total = num + answer
#    output_txt["text"] = total

#def reset():
#    total = 0
#    output_txt["text"] = 0
#    enter_txt.delete(0, END)
#    enter_txt.focus()

#total = 0
#num = 0

#window = Tk()
#window.title("Adding together")
#window.geometry("450x100")

#enter_lbl = Label(text = "Enter a number: ")
#enter_lbl.place(x = 50, y = 20, width = 100, height = 25)

#enter_txt = Entry(text = 0)
#enter_txt.place(x = 150, y = 20, width = 100, height = 25)
#enter_txt["justify"] = "center"
#enter_txt.focus()

#add_btn = Button(text = "Add", command = add_on)
#add_btn.place(x = 300, y = 20, width = 50, height = 25)

#output_lbl = Label(text = "Answer = ")
#output_lbl.place(x = 50, y = 50, width = 100, height = 25)

#output_txt = Message(text = 0)
#output_txt.place(x = 50, y = 50, width = 100, height = 25)
#output_txt["bg"] = "white"
#output_txt["relief"] = "sunken"

#clear_btn = Button(text = "Clear", command = reset)
#clear_btn.place(x = 300, y = 50, width = 50, height = 25)

#window.mainloop()

#def add_name():
#    name = enter_txt.get()
#    lst.insert(END, name)
#    lst.focus()

#def clear():
#    lst.delete(0,END)
#    lst.focus()



#window = Tk()
#window.title("Name list")
#window.geometry("600x400")
#window["bg"] = "light blue"

#enter_lbl = Label(text = "Enter a name: " )
#enter_lbl.place(x = 5, y = 20, width = 100, height = 25)
#enter_lbl["bg"] = "light blue"

#enter_txt = Entry(text = 0)
#enter_txt.place(x = 100, y = 20, width = 200, height = 25)
#enter_txt["justify"] = "left"
#enter_txt["bg"] = "light blue"
#enter_txt.focus()

#add_btn = Button(text = "Add Name", command = add_name)
#add_btn.place(x = 300, y = 20, width = 100, height = 25)

#lst = Listbox()
#lst.place(x = 100, y = 50, width = 200, height = 300)
#lst["bg"] = "silver"
#lst["relief"] = "raised"

#clear_btn = Button(text = "Clear List", command = clear)
#clear_btn.place(x = 300, y = 50, width = 100, height = 25)

#window.mainloop()

#def convert_to_miles():
#    km = enter_txt.get()
#    km = int(km)
#    miles = km * 0.6214
#    output_txt["text"] = str(miles) + " miles"
#    output_txt.focus()

#def convert_to_km():
#    miles = enter_txt.get()
#    miles = int(miles)
#    km = miles * 1.6093
#    output_txt["text"] = str(km) + " Km"
#    output_txt.focus()

#window = Tk()
#window.geometry("800x200")
#window.title("Coversion interface")

#enter_lbl = Label(text = "Enter distance: ")
#enter_lbl.place(x = 5, y = 20, width = 200, height = 25)

#enter_txt = Entry(text = 0)
#enter_txt.place(x = 200, y = 20, width = 200, height = 25)
#enter_txt["justify"] = "left"
#enter_txt.focus()

#km_button = Button(text = "Convert to Km", command = convert_to_km)
#km_button.place(x = 400, y = 20, width = 125, height =  25)

#m_button = Button(text = "Convert to miles", command = convert_to_miles)
#m_button.place(x =  550, y = 20, width = 125, height = 25)

#output_txt = Message(text = 0)
#output_txt.place(x = 100, y = 50, width = 200, height = 25)

#window.mainloop()

#def add():
#    num = ent_txt.get()
#    x = num.isdigit()
#    if x == True:
#        num = int(num)
#        lst.insert(END, num)
#        output_box["text"] = ""
#        ent_txt["text"] = ""
#        lst.focus()
#    else:
#        ent_txt["text"] = ""
#        output_box["text"] = "Must be a whole number"
#        output_box.focus()

#def save():
#    tmp_lst = lst.get(0,END)
#    for i in tmp_lst:
#        n = str(i) + ","
#        file = open("numlst.csv","a" )
#        file.write(n)
#        file.close()

#window = Tk()
#window.geometry("800x600")
#window.title("Number List")

#ent_label = Label(text = "Enter a whole number: ")
#ent_label.place(x = 5, y = 20, width = 200, height = 25)

#ent_txt = Entry(text = 0)
#ent_txt.place(x = 220, y = 20, width = 100, height = 25)
#ent_txt["justify"] = "left"
#ent_txt.focus()

#add_but = Button(text = "Add to list", command = add)
#add_but.place(x = 330, y = 20, width = 100, height = 25)

#output_box = Message(text = "")
#output_box.place(x = 201, y = 50, width = 200, height = 100)


#lst = Listbox()
#lst.place(x = 5, y = 50, width = 200, height = 200)

#save_button = Button(text = "Save List", command = save)
#save_button.place(x = 430, y = 20, width = 100, height = 25)

#window.mainloop()

import csv

def add():
    name1 = name1_ent.get()
    name1 = name1 + ","
    name2 = name2_ent.get()
    name2 = name2 + ","
    age = age_ent.get()
    age = str(age) + ","
    data = name1 + name2 + age + "\n"
    file = open("personel.csv", "a")
    file.write(data)
    file.close()

def display_file():
    disp_file.delete(0, END)
    file = open("personel.csv", "r")
    read = csv.reader(file)
    row = list(read)
    for i in row:
        disp_file.insert(END, i)
    disp_file.focus()
    file.close()
    
window = Tk()
window.geometry("600x400")
window.title("Names csv")

name1_lbl = Label(text = "Enter First name: ")
name1_lbl.place(x = 5, y = 20, width = 200, height = 25)
name1_lbl["bg"] = "light gray"

name2_lbl = Label(text = "Enter Last name: ")
name2_lbl.place(x = 5, y = 50, width = 200, height = 25)
name2_lbl["bg"] = "light gray"

age_lbl = Label(text = "Enter age: ")
age_lbl.place(x = 5, y = 85, width = 200, height = 25)
age_lbl["bg"] = "light gray"

name1_ent = Entry(text = "")
name1_ent.place(x = 210, y = 20, width = 200, height = 25)
name1_ent["justify"] = "center"
name1_ent.focus()

name2_ent = Entry(text = "")
name2_ent.place(x = 210, y = 50, width = 200, height = 25)
name2_ent["justify"] = "center"
name2_ent.focus()

age_ent = Entry(text = "")
age_ent.place(x = 210, y = 85, width = 200, height = 25)
age_ent["justify"] = "center"
age_ent.focus()

ent_button = Button(text = "Add to file" , command = add)
ent_button.place(x = 420, y = 20, width = 100, height = 25)
ent_button["bg"] = "light gray"
ent_button.focus()

disp_file = Listbox()
disp_file.place(x = 5, y = 115, width = 400, height = 300)

disp_button = Button(text = "Display file", command = display_file)
disp_button.place(x = 420, y = 50, width = 150, height = 25)
disp_button["bg"] = "light gray"
disp_button.focus()

window.mainloop()

