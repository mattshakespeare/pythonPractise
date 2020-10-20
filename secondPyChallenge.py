# A function that asks for two numbers and outputs the numbers in asscending order
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

if num1 > num2:
    print(num2, num1)
else:
    print(num1, num2)

print() # Line space between each challenge

#Asks for a number below 20 and ouputs a message "Too High" or "Thank You"
userNum = int(input("Enter a number below 20: "))

if userNum >= 20:
    print("Too High")
else:
    print("Thank You")

print()# Line space between each challenge

# Asks user to enter a number between 10 and 20, output incorrect if it's out of range.
userNum = int(input("Enter a number between 10 and 20: "))

if userNum >= 10 and userNum <= 20:
    print("Thank You")
else:
    print("Incorrect answer")

print() # Line space between each challenge


# Asks the user to enter a colour and, while the computer likes the colour red.
red = "red", "RED", "Red"
userColour = input("What is your favourite colour?: ")

if userColour == "red":
    print("I like red too")
else:
    print("I don't like ", userColour," I like red.")

print()# Line space between each challenge

# Ask the user 2 quetions and evaluates their response to advice appropriate action.
rain = str.lower(input("Is it rainining outside?: "))
wind = str.lower(input("Is it windy?: "))

if wind == "yes" and rain == "yes":
    print("It is to windy for an unbrella")
elif wind == "no" and rain == "yes":
    print("Take an umbrella")
else:
    print("Enjoy your day")

print()# Line space between each challenge

# Ask user for their age, and output thing they can participate in at that age.
age = int(input("How old are you?: "))

if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a lottery ticket")
elif age <= 16:
    print("You can go trick or treating")

print() # Line space between each challenge

#Asks the user to enter 1, 2 or 3 and outputs a response to the answer.
num = int(input("Enter either 1, 2 or 3: "))

if num == 1:
    print("Thank you")
elif num == 2:
    print("Well done")
elif num == 3:
    print("Correct")
else:
    print("Error message")


    
