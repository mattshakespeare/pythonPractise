#creates a txt file
file = open("Numbers.txt", "w")
file.write("1, ")
file.write("2, ")
file.write("3, ")
file.write("4, ")
file.write("5, ")
file.close()

print()
#creates a txt file
file1 = open("Names.txt", "w")
file1.write("Matt\n")
file1.write("Katie\n")
file1.write("Ben\n")
file1.write("Tom\n")
file1.write("Elle\n")
file1.close()

print()
#reads txt file
file1 = open("Names.txt", "r")
print(file1.read())
file1.close()

print()
#reads new str entity, appends entity to file
file1 = open("Names.txt", "a")
name = input("Enter a name to add to names file: ")
name += "\n"
file1.write(name)
file1.close()

print()
#output menu,  user picks a menu option 1, 2 or 3
#if 1 user enters a school subject
#if 2 display contents of file
#if 3 add a new item to file and display contents of fie
sel = 0
while sel != 4:
    sel = int(input("1) Create a new file\n2) Display the file\n3) Add a new item to the file\n4) Close program\nSelect 1, 2, 3 or 4: "))
    if sel == 1:
        file = open("Subject.txt", "w")
        sub = input("Enter a subject you want to add to a file: ")
        sub += "\n"
        file.write(sub)
        file.close()
    elif sel == 2:
        file = open("Subject.txt", "r")
        print(file.read())
        file.close()
    elif sel == 3:
        file = open("Subject.txt", "a")
        sub = input("Enter a subject you want to add to the file: ")
        sub += "\n"
        file.write(sub)
        file.close()
        file = open("Subject.txt", "r")
        print(file.read())
        file.close()

print()
#display names from Names.txt, program reads one of the names and stores name in a new file
file = open("Names.txt", "r")
print(file.read())
file.close()
name = input("Enter a name to remove from the file: ")
name = name + "\n"
file = open("Names.txt", "r")
for row in file:
    if row != name:
        file1 = open("Names2.txt", "a")
        newName = row
        file1.write(newName)
        file1.close()
file1 = open("Names2.txt", "r")
print(file1.read())
file1.close()
file = open("Names.txt", "r")
print(file.read())
file.close()
