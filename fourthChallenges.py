#math challeneges

# read a float and multiply it by two

num = float(input("Enter a number with lots of decimal places: "))
print("Your number multiplied by two = ", num * 2)

print()
# Round previous anser to 2 D.P

print("To 2 decimal places your answer = ", round(num * 2, 2))

print()
#Read an integer >= 500 and return sqr to 2 D.P

import math

num = float(input("Enter  number greater than 500 and I will return the square root to 2 decimal places: "))
sq = math.sqrt(num)
print("The square root of your number to 2 decimal places = ", round(sq, 2))

print()
#display pi to 5 decimal places

pI = round(math.pi, 5)

print("pi to 5 decimal places", pI)

print()
# Read the radius of a circle and calculate it's area


rad = float(input("Enter the radius of a circle and I will return the area of the circle: "))
print("The area of the cirlce is = ", math.pi * (rad ** 2))

print()
# Read the radius and depth of a cylinder and output the volume of the cylinder to 3 D.P

rad = float(input("Enter the radius of a cylinder: "))
dep = float(input("Enter a the depth of cylinder so i can calculate the volume: "))
radArea = math.pi * (rad ** 2)
print("The volume of the cylinder = ", radArea * dep )

print()
#Reads two numbers and outputs inputs the whole number division and the remainder

num1 = int(input("Now I will divide two numbers and output the whole number answer and it's remainder. What is the first number: "))
num2 = int(input("And what is the second number: "))
print(num1, " divided by ", num2, " = ", num1 // num2, " with a remainder of ", num1 % num2)

print()
#Reads the users decision, reads for sqr length of one side, for triangle, base and height and returns the area

print("Choose whether I claculate the area of a circle or square.")
shape = int(input("1) Square\n2) Triangle\n\nEnter a number to choose the shape:  "))

if shape == 1:
      l = int(input("Enter the length of the side: "))
      print("The area of the square = ", l ** 2 )
if shape == 2:
      h = int(input("Enter the height of the triangle: "))
      b = int(input("Enter the length of the base of the triangle: "))
      print("The area of the triangle = ", (h * 2) / 2)
      
