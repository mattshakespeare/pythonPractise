

def code():
    newMessage = ""
    message = input("Enter message to encrypt: ")
    y = int(input("Enter a Number: "))
    
    for i in message:
        i = ord(i) + y
        newMessage += chr(i)

    print(newMessage)

def decode():
    newMessage = ""
    message = input("Enter encrypted message: ")
    y = int(input("Enter the Number: "))
    
    for i in message:
        i = ord(i) - y
        newMessage += chr(i)

    print(newMessage)


def main():
    x = 0
    while x != 3:
        print("Main Menu\n\n1) Make Code\n2) Decode Message\n3) Quit")
        x = int(input("Enter your selection here: "))

        if x == 1:
            code()
        elif x == 2:
            decode()
        elif x == 3:
            print("Thats all folks")
        else:
            print("Must select an option from the menu")

main()
