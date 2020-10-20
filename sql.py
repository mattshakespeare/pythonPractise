import sqlite3
#with sqlite3.connect("Phonebook.db") as db:
    #cursor = db.cursor()

#cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(
#id interger PRIMARY KEY,
#firstname text,
#surname text,
#phonenumber, text); """)

#cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
#VALUES("1", "Simon", "Howels", "01223 349752")""")
#db.commit()

#cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
#VALUES("2", "Karen", "Phillips", "01954 295773")""")
#db.commit()

#cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
#VALUES("3", "Darren", "Smith", "01583 749012")""")
#db.commit()

#cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
#VALUES("4", "Anne", "Jones", "01323 567322")""")
#db.commit()

#cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber)
#VALUES("5", "Mark", "Smith", "01223 855534")""")
#db.commit()

#db.close()

def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    print(cursor.fetchall())

def addtophonebook():
    newId = input("Enter ID number: ")
    newFirstname = input("Enter first name: ")
    newSurname = input("Enter surname: ")
    newPhonenumber = input("Enter new phone number: ")
    cursor.execute("""INSERT INTO Names(id,firstname,surname,phonenumber)
    VALUES (?,?,?,?)""", (newId,newFirstname,newSurname,newPhonenumber)
)
    db.commit()
def selectname():
    surname = input("Enter surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [surname])
    for i in cursor.fetchall():
        print(i)
    db.commit()
def deletename():
    deleteId = int(input("Enter the ID of the entry you would like to delete: ")
)
    cursor.execute("DELETE FROM Names WHERE id = ?", [deleteId])
    cursor.execute("SELECT * FROM Names")
    for i in cursor.fetchall():
        print(i)
    db.commit()

def main():
    x = True
    while x == True:
        print("Main Menu")
        print()
        print("1) View Phonebook")
        print("2) Add to phonebook")
        print("3) Search for surname")
        print("4) Delete Person from phonebook")
        print("5) Quit")
        print()
        selection = int(input("Enter your selection: "))

        if selection == 1:
            viewphonebook()
        elif selection == 2:
            addtophonebook()
        elif selection == 3:
            selectname()
        elif selection == 4:
           deletename()
        elif selection == 5:

            print("Thats all folks")
            x = False
        else:
            print("Incorrect Selection!")

#main()
#db.close()

#def main():
#    with sqlite3.connect("Bookinfo.db") as db:
#        cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Authors(
    Author text PRIMARY KEY,
    BirthPlace text);""")

    cursor.execute("""INSERT INTO Authors(Author, BirthPlace)
    VALUES("Agatha Christie","Torquay")""")
    db.commit()

    cursor.execute("""INSERT INTO Authors(Author, BirthPlace)
    VALUES("Cecilia Ahern","Dublin")""")
    db.commit()

    cursor.execute("""INSERT INTO Authors(Author, BirthPlace)
    VALUES("J.K. Rowling","Bristol")""")
    db.commit()

    cursor.execute("""INSERT INTO Authors(Author, BirthPlace)
    VALUES("Oscar Wilde","Dublin")""")
    db.commit()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Books(
    id interger PRIMARY KEY,
    Title text,
    Author text,
    DatePublished text );""")

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("1","De Profundis", "Oscar Wilde", "1905")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("2","Harry Potter and the chamber of secrets", "J.K. Rowling", "1998")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("3","Harry Potter and the prisoner of azkaban", "J.K. Rowling", "1999")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("4","Lyrebird", "Cecilia Ahern", "2017")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("5","Murder on the orient express", "Agatha Christie", "1934")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("6","Perfect", "Cecilia Ahern", "2017")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("7","The marble collector", "Cecilia Ahern", "2017")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("8","The murder on the links", "Agatha Christie", "1923")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("9","The picture of Dorian Gray", "Oscar Wilde", "1890")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("10","The secret adversary", "Agatha Christie", "1921")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("11","The seven dials mystery", "Agatha Christie", "1929")""")
    db.commit()

    cursor.execute("""INSERT INTO Books(id, Title, Author, DatePublished)
    VALUES("12","The year I met", "Cecilia Ahern", "2014")""")
    db.commit()

    db.close()

#main()





def saveAuthor(cursor):
    file = open("bookrecord.txt", "a")
    author = input("Choose an author: ")
    cursor.execute("SELECT * FROM Books WHERE Author = ?",[author])
    for i in cursor.fetchall():
        newRecord = str(i[0]) + "-" + str(i[1]) + "-" + str(i[2]) + "-" + str(i[3]) + "\n"
        file.write(newRecord)
    file.close

def year(cursor):
    year = input("Enter a year: ")
    cursor.execute("SELECT * FROM Books WHERE DatePublished > ? ORDER BY DatePublished",[year])
    print()
    print("These are the books published after that year: ")
    for i in cursor.fetchall():
        print(i)

def showAuthors(cursor):
    cursor.execute("SELECT * FROM Authors")
    for i in cursor.fetchall():
        print(i)

def placeOfBirth(cursor):
    x = input("Enter a place of birth: ")
    x = x.title()
    cursor.execute("""SELECT Books.Title, Books.Author, Books.DatePublished
    FROM Books,Authors WHERE Authors.Author = Books.Author AND Authors.BirthPlace = ?""", [x])
    for i in cursor.fetchall():
        print(i)

def main():
    y = ""
    while y != "x":
    
        with sqlite3.connect("Bookinfo.db") as db:
            cursor = db.cursor()

        showAuthors(cursor)
        print()
        placeOfBirth(cursor)
        print()
        year(cursor)
        print()
        saveAuthor(cursor)
        print()
        y = input("Enter x to exit, Press anything else to continue: ")
        print()

    db.close()


main()
