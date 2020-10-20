#displys a tuple containing strings
#reads a string from the user and ouputs its index.
ctry = ("China", "England", "India", "Russia", "Canada")
print(ctry)
user = input("Enter one of the Countries that have been shown: ")
user = user.title()
print("The index number of ", user, " is ", ctry.index(user))

print()
#Exstention of above, reads index number and displays strings in position
user = int(input("Enter a numbers between 0-4 and i will display the country in that position: "))
dis = False
while dis == False:
    if user >= 0 and user <= 4:
        print("The country in position ", user, " is ", ctry[user])
        dis = True
    else:
        user = int(input("You must pick a number between 0 - 4: "))

print()
#reads users favourite sport, appends sport to a list, and displys sorted list        
sport = ["Rugby", "Football"]
user = input("What is your favourite sport: ")
user = user.title()
sport.append(user)
sport.sort()
print(sport)

print()
#stores a list of subjects, deletes an entity from the list, displays list again
sub = ["History", "Math", "English", "Science", "Geography", "French"]
print(sub)
dis = True
while dis == True:
    user = input("Which of the subjects do you dislike the most: ")
    user = user.title()
    if user in sub:
        sub.remove(user)
        print("I have removed the subject ", user, sub)
        dis = False
    else:
        print("You must choose a subject from the list.")

print()
#reads user favourite foods and stores in a dictionary
food = {}
print("Im going to ask you for four of your favourite foods.")
for i in range(4):
    f = input("Enter one of your favourite foods: ")
    f = f.title()
    food[i + 1] = f
print(food)
rem = int(input("Pick the index number of the food you would to remove from the list: "))
del food[rem]
print(sorted(food.values()))

print()
#stores a list of ten colour, reads a slice begging and end
col = ["Red","Green", "Blue", "Orange", "Yellow", "Gold", "Silver", "Pink", "Black", "White"]
x = int(input("Enter a starting indices between 0 - 4: "))
y = int(input("Enter a final indices between 5 - 9: "))
print(col[x:y])

print()
#stores list, outputs list to user, reads users entity.
#if entity in list display indices of entity
#if entity not in list output confirm to user

nums = [432, 543, 836, 995]
for i in nums:
    print(i)
user = int(input("Enter a three digit number: "))
if user in nums:
    print(user, " is in position: ", nums.index(user))
else:
    print( user," is not in the list.")

print()
#reads a list of entities, user adds to the list until they break the loop
inv = []
x = input("Enter yes to add someone to your party invitations: ")
while x == "yes":
    y = input("Who would you like to invite: ")
    inv.append(y)
x = input("Would you like to invite another person to your party: ")
print("You have invited", len(inv), " people to your party.")
print(inv)

print()
#Extension of the above program
name = input("Enter the name of an individual on the list to find their position in the list: ")
print(inv.index(name))
z = True
while z == True:
    y = input("Do you still want to invite this person to your party: ")
    if y == "yes":
        print(name, "is still invited to the party")
        z = False
    elif y == "no":
        print(name, "is no longer on the list.")
        z = False
        inv.remove(name)
    else:
        print("You must enter yes or no")
print(inv)

print()
#stores a list, outputs entities on seperate lines.
#reads a new entity user dictates postion
#outputs new list
tv = ["Scrubs", "South Park", "Friends", "Top Gear"]
for i in tv:
    print(i)
user = input("Enter a TV show to be inserted into the list: ")
pos = int(input("At what position in the list do you want this to be inserted: "))
tv.insert(pos, user)
for i in tv:
    print(i)
print("That's all for today folks!!!")


