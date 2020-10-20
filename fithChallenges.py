#reads users name and displays name three times
name = input("Enter your name: ")
for i in range(4):
    print(name)

print()
#takes users name and outputs name as many times as the user inputs

x = int(input("Enter the number of times i should print your name: "))
for i in range(x):
    print(name)

print()
#reads users name and outputs every letter on a new line
name = input("Enter your name and i will spell it out for you: ")
for i in name:
    print(i)

print()
#reads a numbers of times to output every letter of users name
x = int(input("How many times should I spell your name?: "))
for i in range(x):
    for i in name:
        print(i)
    print("\n")

print()
#read int and outputs times table for that number
num = int(input("Lets do some maths, pick a number between 1 and 12, I will show you the multiplication table: "))
for i in range(1, 13):
    print(i, " X ", num, " = ", num * i )

print()
#reads a number below 50 and returns a countdown from 50 to int
num = int(input("Enter a number below 50 and I will count from 50 to your number: "))
for i in range(50, num, -1):
    print(i)
print(num)

print()
#reads users name and an int, < 10 display name as many times as int value > 10 output to high * 3

name = input("Enter your name: ")
x = int(input("Enter a number less  than ten, and I will say your name that number of times: "))
if x < 10:
    for i in range(x):
        print(name)
else:
    for i in range(4):
        print("Too High!!!")

print()
#reads five int value, ask user which values should be added to total, outputs total
tot = 0
for i in range(5):
    x = int(input("Enter a number: "))
    y = input("Would you like this value added to the sum total, enter yes or no: ")
    y = y.lower()
    if y == "yes":
        tot += x
    elif y == "no":
        continue
    else:
        print("I need a yes or no answer please try again")
        i -= 1
        
print("Your total is: ", tot)

print()
#reads direction
#If direction is up asks for int, and counts to number
#If direction is down, reads value below 20 and counts to int value
#If direction isn't up or down, outputs "Dont understand"
x = input("Enter a direction for me to count up or down: ")
x = x.lower()
if x == "up":
    y = int(input("Enter a number for me to count up to: "))
    for i in range(1, y+1):
        print(i)
elif x == "down":
    y = int(input("Enter a number below 20 for me to count down to: "))
    if y <= 20:
        for i in range(y, 1 - 1, -1 )
            print(i)
    else:
        print("The number you have chosen is greater than 20")
else:
    print("Must choose up or down as your direction")

print()
#read int value
#if value is below 10, ask for 10 names
#during each iteration output a name confirm invitation
#if number is grerater than 10 out put "Too many people"
x = int(input("Your allowed to have a party, your allowed to invite 10 people, how many people would you like to invite?: "))
if x <= 10:
    for i in range(x):
        y = input("Enter the name of the person you would like to invite: ")
        print(y, " has been invited")
else:
    print("Too many people!!!!")
