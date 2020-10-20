from array import *

#reads an int, adds int to array, outputs array in descending order
nums = array("i", [])
for i in range(5):
    x = int(input("Enter a number for the array: "))
    nums.append(x)
nums = sorted(nums)
nums.reverse()
print(nums)

print()
#stores a five random int values in an array, displays each item on a seperate line
import random
nums = array("i",[])
for i in range(5):
    x = random.randint(0,100)
    nums.append(x)
for i in nums:
    print(i)

print()
#reads 5 int values and stores in an array
#if int < 10 or > 20 "Outside the range"
#output each item on a seperate line
nums = array("i", [])
count = 0
while count < 5:
    x = int(input("Enter a number for the array between 10 - 20: "))
    if x < 10 or x > 20:
        print("Outside the range.")
    else:
        print("Thank you succesfully added.")
        nums.append(x)
        count += 1
for i in nums:
    print(i)

print()
#displays array to user, reads an item in array, outputs the number of iterations of the item in array
nums = array("i",[1,2,3,3,4,5,6,7,7,4,8])
print(nums)
x = int(input("Enter one of the numbers from the array: "))
print(nums.count(x))

print()
#reads five values, stores in array, sorts array, outputs array, reads an item, removes item from list.
nums = array("i", [])
for i in range(5):
    x = int(input("Enter a number for an array: "))
    nums.append(x)
print(nums)
y = int(input("Which number should be removed from the array: "))
nums.remove(y)
nums1 = array("i", [y])
print(nums)
print(nums1)

print()
#outputs array, reads users choice, diplay position of item.
#if users choice is not in array, ask user to again
nums = array("i", [1,2,3,4,5])
print(nums)
x = int(input("Choose an item from the array: "))
y = False
while y == False:
    if x in nums:
        print("The postion of item is", nums.index(x))
        y = True
    else:
        x = int(input("Must choose an item from the array, try again: "))

print()
#stores an array of floats, reads a divisor, divides each number in the array, outputs result to 2 d.p
nums = array("f",[45.33,76.32,85.99,34.93,20.22])
print(nums)
div = int(input("Enter a number between 2 and 5: "))
y = True
while y == True:
    if div < 2 or x > 5:
        div = int(input("Enter a number between 2 and 5: "))
    else:
        y = False
for i in nums:
    x = i / div
    x = round(x, 2)
    print(x)   
    
