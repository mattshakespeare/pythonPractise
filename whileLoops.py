#reads a int, total + int, while total < 50 continue loop
tot = 0
while tot <= 50:
    tot += int(input("Enter a number below 50, when your total is above 50 the loop will end: "))
    print("Your total is ",tot )

print()
#while number is less than 5 continue loop
num = 0
while num < 5:
    num = int(input("Enter a number, while the number is less than 5 the loop will continue: "))
print("The last number you entered was ", num)

print()
#reads two numbers and adds them together, loop continues until the input != y
res = "y"
while res == 'y':
    a = int(input("Enter two numbers and i will add them together. What is your first number: "))
    b = int(input("Enter your second number: "))
    print(a + b)
    res = input("Enter y to carry on: ")
    
print()
#asks the user to invite someone to the party, outputs the invite, carrys on until user breaks the loop
name = input("Enter the name of someone you would like to invite to your party, Enter y when you are finished:  ")
while name != "y":
    print(name, " has been invited to the party.")
    name = input("Enter the name of someone you would like to invite to your, Enter y when you are finished: ")

print()
#reads users guess, loop continues until the user guesses value.
compNum = 50
userNum = int(input("Guess the computers number: "))
while userNum != compNum:
    if userNum < compNum:
        print("You are too low!")
    elif userNum > compNum:
        print("You are to high!")
    userNum = int(input("Guess the computers number: "))
print("You guessed correctly.")

print()
#reads an int value, if value below 10 ' too high ', if above 20 ' too low '
num = int(input("Enter a value between 10 and 20: "))
while num < 10 or num > 20:
    if num < 10:
        print("Too Low!!")
    elif num > 20:
        print("Too high!!")
print("Thank you")

print()
#reads users int input, after outputing green bottle.
#if user input int == green bottles - 1, outputs next line of the song
#else "no try agian".
#continue while green bottles != 0
bot = 10
while bot > 1:
    print("There are ", bot," green bottles hanging on the wall.")
    print(bot, " green bottles hanging on the wall")
    x = int(input("if 1 green bottles should accidently fall, how many green bottles are hanging on the wall: "))
    if x == bot - 1:
        bot = x
        print("There will be ", bot, " green bottles hanging on the wall.")
    else:
        print("No, try again!")
