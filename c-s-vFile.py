import csv

#creates a csv file
file = open("Books.csv", "w")
newRecord = ("""To Kill A Mockingbird,Harper Lee,1960
A Brief History of Time,Stephen Hawking,1988
The Great Gatsby,F.Scott Fitzgerald,1922
The Man Who Mistook His Wife For A Hat,Oliver Sacks,1985
Pride And Prejudice,Jane Austen,1813""")
file.write(str(newRecord))
file.close
file = open("Books.csv", "r")
print(file.read())
file.close()

print()
#apped new record to books.csv
title = input("Enter the title of a book you would like to add to the record: ")
author = input("Enter the author of the book: ")
year = input("Enter the year the book was published: ")
book = "\n" + title + "," + author + "," + year
file = open("Books.csv", "a")
file.write(str(book))
file.close()
file = open("Books.csv", "r")
print(file.read())

print()
#asks how many records they would like to append to the list, append record.
#ask user for an author, display all books by that author from the list
num = int(input("How many records would you like to add to the list: "))
count = 0 
while count < num:
    file = open("Books.csv", "a")
    title = input("Enter the title of a book you would like to add to the record: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the year the book was published: ")
    book = "\n" + title + "," + author + "," + year
    file.write(str(book))
    file.close()
    count += 1
aut = input("Select an author: ")
aut = aut.title()
file = open("Books.csv", "r")
read = csv.reader(file)
count = 0
for row in file:
    if aut in row:
        count += 1
        print(row)
if count == 0:
    print("This author as not been recorded in the file.")
file.close()

print()
#reads a start year and an end year, outputs books published during that year
start = int(input("Enter a start year: "))
end = int(input("Enter a end year: "))
print("These are the books published in the Books.csv file, between", start, "and", end)
file = list(csv.reader(open("Books.csv", "r")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    if int(file[x][2]) >= start and int(file[x][2]) <= end:
        print(tmp[x])
    x += 1

print()
#display the index for each row of data
file = open("Books.csv", "r")
x = 0
for row in file:
    print("Row: " + str(x) + "-" + row)
    x += 1
file.close()

print()
#import Books.csv into a list, output list. read row to delete.
#read which data to alter, alter data and overwirte existing file
file = list(csv.reader(open("Books.csv")))
lst = []
for row in file:
    lst.append(row)
delete = int(input("Enter the number of the row you would like to remove from the file: "))
del lst[delete]
file = open("Books.csv", "r")
x = 0
for row in lst:
    print("Row: " + str(x) + "-" + str(row))
    x += 1
file.close()
row = int(input("Enter the number of the row you would like to alter: "))
print(lst[row])
col = int(input("Enter column you would like to alter: "))
print(lst[row][col])
newData = input("Enter the new Data: ")
lst[row][col] = newData
x = 0
file = open("Books.csv", "w")
for row in lst:
    newData = str(lst[x][0]) + "," + str(lst[x][1]) + "," + str(lst[x][2]) + "\n"
    file.write(newData)
    x += 1
file.close()
file = open("Books.csv", "r")
print(file.read())
file.close()

print()
#A math quiz, stores and reads name, stores and asks to questions and sorts and reads answers
#stores final score
import random
print("This is a maths quiz.")
name = input("Enter your name: ")
score = 0
val1 = random.randint(1, 100)
val2 = random.randint(1, 100)
val3 = random.randint(1, 100)
val4 = random.randint(1, 100)
ans1 = val1 + val2
ans2 = val3 + val4
q1 = "Question 1: " + str(val1) + "+" + str(val2)
print(q1)
userans1 = int(input(" = "))
if userans1 == ans1:
    score += 1
q2 ="Question 2: " + str(val3) + "+" + str(val4)
print(q2)
userans2 = int(input(" = "))
if userans2 == ans2:
    score += 1
record = name + "," + q2 + "," + str(userans1) + "," + q2 + "," + str(userans2) + "," + str(score) + "\n"
file = open("mathquiz.csv", "a")
file.write(record)
file.close()
file = open("mathquiz.csv", "r")
print(file.read())
file.close()
       
