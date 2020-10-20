#read int value, increment by 1 from 1 to that number
def userNum():
    num = int(input("Enter a number: "))
    return num

def count(num):
    for i in range(1, num + 1):
        print(i)

def main():
    num = userNum()
    count(num)
#main()
import random

print()
#asks user for a high and low number and picks a random value between the two
#asks user to guess the random value
def pickNum():
    low = int(input("Enter a low number: "))
    high = int(input("Enter a high number: "))
    comp_num = random.randint(low, high)
    return comp_num

def user_guess():
    guess = int(input("I am thinking of a number....Can you guess?: "))
    return guess

def game(comp_num, guess):
    x = 0
    while x == 0:
        if guess == comp_num:
            print("Correct, you win!")
            x += 1
        elif guess > comp_num:
            guess = int(input("Too high, guess again: "))
        elif guess < comp_num:
            guess = int(input("Too low, guess again: "))

def main():
    comp_num = pickNum()
    guess = user_guess()
    game(comp_num, guess)
#main()

print()
#asks the user to choose an addition or subtraction maths question
def menu():
    print("1) Addition")
    print("2) Subtration")
    opt = int(input("Enter either 1 or 2: "))
    return opt

def addition():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    answer = num1 + num2
    print(num1, "+", num2)
    userans = int(input("Your answer: "))
    ans = (answer, userans)
    return ans
    

def subtraction():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    answer = num1 - num2
    print(num1, "-", num2)
    userans = int(input("Your answer: "))
    ans = (answer, userans)
    return ans

def check(answer, userans):
    if userans == answer:
        print("Correct!")
    elif userans != answer:
        print("Incorrect, the answer is ", answer)

def main():
    x = False
    while x == False:
        opt = menu()
        if opt == 1:
            answer, userans = addition()
            check(answer, userans)
            x = True
        elif opt == 2:
            subtraction()
            check(answer, userans)
            x = True
        else:
            print("Please select an option from the menu.")
#main()

print()
#helps user manage a list
def menu():
    print("1) Add name")
    print("2) Change a name")
    print("3) Delete a name")
    print("4) View list")
    print("5) End program")
    opt = int(input("Select your option here: "))
    return opt

def add_name():
    name = input("Enter the name you would like to add to the list: ")
    lst.append(name)
    return lst

def change_name():
    name = input("Enter the name you would like to change: ")
    newName = input("Enter the name you would like to change it too: ")
    i = lst.index(name)
    lst[i] = newName
    return lst
    
def delete_name():
    name = input("Enter the name in the list you would like to remove: ")
    if name in lst:
        lst.remove(name)    
    else:
        print("Name not in list.")
    return lst

def view_list(lst):
    for name in lst:
        print(name)

def main():
    opt = 0
    while opt != 5:
        opt = menu()
        if opt == 1:
            lst = add_name()
        elif opt == 2:
            lst = change_name()
        elif opt == 3:
            lst = delete_name()
        elif opt == 4:
             view_list(lst)
        elif opt == 5:
            print("Thats all folks")
        else:
            print("Must choose an option from the menu")
#lst = []
#main()
import csv
def add_record():
    file = open("Salaries.csv", "a")
    name = input("Enter a name to add to the file: ")
    sal = int(input("Enter the salary: "))
    file.write(name + "," + "£" + str(sal) + "\n")
    file.close()

def view_record():
    file = open("Salaries.csv", "r")
    print(file.read())
    file.close()

def delete_file():
    file = open("Salaries.csv", "r")
    tmp = []
    x = 0
    for row in file:
        tmp.append(row)
    file.close()
    for row in tmp:
        print(x,row)
        x += 1
    delete = int(input("Enter the row number you would like to remove: "))
    del tmp[delete]
    file = open("Salaries.csv", "w")
    for row in tmp:
        file.write(row)
    file.close() 

def main():
    opt = 0
    while opt != 4:
        print("1) Add to file")
        print("2) View all records")
        print("3) Delete Record")
        print("4) Quit program")
        opt = int(input("Enter the number of your selection: "))
        if opt == 1:
            add_record()
        elif opt == 2:
            view_record()
        elif opt == 3:
            delete_file()
        elif opt == 4:
            print("Thats all folks")
        else:
            print("Must select an option from the menu")
main()  
    



