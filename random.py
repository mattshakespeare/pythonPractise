#outputs random int between 1 - 100
import random

print(random.randint(1,100))

print()
#outputs random entity from a list of fruit
fruit = ["Grapes", "Orange", "Banana", "Grapefruit", "Honeydew Melon", "Strawberry", "Watermelon"]
print(random.choice(fruit))

print()
#user and computer choose heads or tails
#if user == computer "You win"
#if user != computer "Bad luck"
y = "y"
while y == "y":
    x = ["Heads", "Tails"]
    comp = random.choice(x)
    user = input("Lets play heads or tails, what do you choose: ")
    user = user.title()
    if user == "Heads" or user == "Tails":
        if user == comp:
            print("You win, the computer picked", comp,".")
            y = input("Press y to play again, press x to end the game: ")
        else:
            if user != comp:
                print("Bad luck!!!!!!, the computer picked ", comp,".")
                y = input("Press y to play again, press x to end the game: ")
    else:
        print("You must choose heads or tails.")

print()
#reads random int
#user has two attempts to guess the int
#before second attempt output "Too high" or "Too low"
comp = random.randint(1, 5)
user = int(input("The computer has a number between 1 and 5. Can you guess: "))
if user == comp:
    print("Correct, you win.")
else:
    if user > comp:
        user = int(input("Too high, try agian: "))
    elif user < comp:
        user = int(input("Too low, try again: "))
    if user == comp:
        print("Correct, second time lucky!!!")
    else:
        print("Unlcuky, you lose the computers number was", comp)

print()
#reads random int between 1 and 10
#while user int != comp int, loop continues
comp = random.randint(1,10)
user = int(input("The computer has a number between 1 and 10, can you guess the computers number: "))
if user != comp:
    while user != comp:
        if user > comp:
            print("Too high.")
        if user < comp:
            print("Too low.")
        user = int(input("Try again: "))
print(user, " is correct the game is over.")

print()
#math quiz, reads two random int *5 and user answers each sum.
#var stores users score and outputs score
score = 0
x = input("Let's have a math quiz, press x to take part, press anything else to skip: ")
if x == "x":
    for i in range(1, 6):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        ans = num1 + num2
        print("Question", i," : ", num1, " + ", num2)
        user = int(input("= "))
        if user == ans:
            print("Correct!")
            score += 1
        else:
            print("Incorrect. The answer is ", ans)
    print("You scored: ", score,"/5")

print()
#stores list of  five colours, user has two attempts to guess compters choice
col = ["Red", "Yellow", "Orange", "Blue", "Green"]
comp = random.choice(col)
print(col)
user = input("What colour do you think the computer is thinking of: ")
user = user.title()
if user == comp:
    print("Well done, you guessed correctly.")
elif user != comp:
    print("Wrong, you must  be ", comp, "with envy.")
    user = input("Try again: ")
    user = user.title()
    if user == comp:
        print("Second time lucky!!!")
    else:
        print("Unlucky, the computers colour was ", comp, ".")

        
