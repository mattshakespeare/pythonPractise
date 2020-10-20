#read first name, surname, output length
#join both names together with a space between
fname = input("Enter your first name: ")
print("There are", len(fname), "characters in your firstname.")
sname = input("Enter your surname: ")
print("There are", len(sname),"characters in your surname.")
name = fname + " " + sname
print("There are", len(name), "characters in your full name including the space inbetween.")

print()
#reads favourite school subject, outputs list sep= "-"
sub = input("What is your favourite subject: ")
for ch in sub:
    print(ch, end="-")

print()
#outputs string, reads slice indices
lyrics = "Sort your shit then roll, sex drugs and on the doll, some men rise, some men fall"
print(lyrics)
print("The length of the string is", len(lyrics))
x = int(input("Enter the first indices: "))
y = int(input("Enter the final indices: "))
print(lyrics[x:y])

print()
#reads a string, repeat while string is not uppercase
word = input("Enter a word in uppercase: ")
while word != word.upper():
    word = input("Word must be uppercase, try again: ")

print()
#reads string and displays first two characters in uppercase
pst = input("Enter your postcode: ")
print("First two characters of your postcade in uppercase", pst[0:2].upper())

print()
#reads string and outputs count of vowels in string
name = input("Enter your name: ")
name = name.lower()
count = 0
for ch in name:
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        count += 1
print("There are", count, "vowels in", name)

print()
#reads string twice, if string == string "correct"
#if strings are unequal due to case "Must be the same case"
#else "incorrect"
pword = input("Enter a password: ")
pword1 = input("Enter password again: ")
x = True
while x == True:
    if pword == pword1:
        print("Correct!")
        x = False
    elif pword.lower() == pword1.lower():
        pword1 = input("Passwords are case sensitive, try again: ")
    else:
        pword1 = input("Incorrect, try again: ")
        

print()
#reads string, outputs each character in descending order
word = input("Enter a word: ")
num = 1
leng = len(word)
for i in word:
    x = leng - num
    letter = word[x]
    num = num + 1
    print(letter)

print("Thats all for today folks.")



