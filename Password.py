import csv

def get_data():
    file = list(csv.reader(open("Passwords.csv")))
    tmp = []
    for x in file:
        tmp.append(x)

def create_user_id(tmp):
    name_again = True
    while name_again == True:
        user_id = input("Enter a new user ID: ")
        in_list = False
        row = 0
        if tmp != None:
            for y in tmp:
                if user_id in [row][0]:
                    print("User ID has been take, please try again: ")
                    inlist = True
                row = row + 1
            if inlist == False:
                name_again = False
        else:
            user_id = user_id
        return user_id

def create_password():
    password = input("Enter a new password: ")
    special_characters = ["!","@","£","$","%","^","&","*","(",")","#"]
    score = 0
    weak = True
    while weak == True:
        for i in password:
            if i == i.upper():
                score += 1
            elif i in special_characters:
                score += 1
            elif i.isdigit() == True:
                score += 1
        if score < 3:
            print("Password is weak, try again")
        elif score < 5:
            a = input("Password could be stronger, enter 'y' to try again, 'n' to save password.")
            if a == "y":
                continue
            else:
                print("Password accepted.")
                weak = False
        else:
            print("Password accepted.")
            weak = False
    
    return password

def save_id(user_id, user_password):
    file = open("Passwords.csv", "a")
    new_id = str(user_id) + "," + str(user_password) + "\n"
    file.write(new_id)
    file.close()
    print("New user has been and password has been saved.")


def main():
    file = open("Passwords.csv", "a")
    file.close()
    tmp = get_data()
    print("Menu\n\n1) Create a new user ID\n2) Change a password\n3) Display all user ID\n\n")

    selection = int(input("Enter your selection here: "))

    if selection == 1:
        user_id = create_user_id(tmp)
        user_password = create_password()
        save_id(user_id, user_password)
    else:
        print("Must select a number from one of the options")

main()
