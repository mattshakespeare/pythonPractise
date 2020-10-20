#Ask the user to enter their name, and output the length of the name.
name = input("Please enter your name?: ")

print(len(name))

print()#Line space between challenges.

#Reads the users first and second name, concatenates the strings together and returns
#the length of both strings.
firstName = input("Please enter your first name: ")
surname = input("Please enter your surname: ")
name = firstName + " " + surname

print(name, " ", len(name))

print()#Line space between challenges.

#Reads users first and surname in lowercase, concatenates the names in title case and returns.
firstName = str.lower(input("Please enter your first name: "))
surname = str.lower(input("Please enter your surname: "))
name = firstName + " " + surname
name = name.title()

print(name)

print()#Line space between challenges

#reads a nursery rhyme, dispays length of string, reads two numbers, slices str.
nursery = input("Enter the first line of nursery rhyme: ")
nursery = nursery.strip(" ")
nurseryLen = len(nursery)
print("This has ", nurseryLen, " character in it")
start = int(input("Now i need a starting number: "))
end = int(input("And a end number: "))

print(nursery[start:end])

print()#Line space between challenges

#returns the users firstname in lower case if name >= 5
#returns users first and surname contatenated if name < 5
firstName = input("Enter first name: ")
surname = input("Enter surname: ")


if len(firstName) < 5:
    name = firstName + surname
    name = name.upper()
elif len(firstName) >= 5:
    name = firstName
    name = name.lower()
print(name)

# changes a word into pig latin
word = input("Enter a word: ")
word = word.lower()

if word[:1] == "a" or word[:1] == "e" or word[:1] == "i" or word[:1] == "o" or word[:1] == "u":
    print(word + "way")
else:
    print(word + "ay")
