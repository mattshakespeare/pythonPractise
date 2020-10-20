def highest_number(num1,num2,num3):
    high_num = -999
    res = (num1,num2,num3)
    for i in res:
        if i > high_num:
            high_num = i
    return high_num

def main():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    number3 = int(input("Enter the third number: "))

    largest_value = highest_number(number1,number2,number3)

    print("The largest number you entered was",largest_value)


def calc_volume(h, w, l):
    volume = h * w * l
    return volume
    
def main():
    print("Im going to calculate the volume of a cuboid.")
    height = int(input("Enter the height of the cuboid: "))
    width = int(input("Enter the width of a cuboid: "))
    length = int(input("Enter the length of the cuboid: "))
    volume = calc_volume(height,width,length)
    print("The volume of the cuboid is", volume)
    
#main()
import random

def roll_dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)

    return dice1, dice2
        
    
    
def main():
    print("Roll a double to begin the game")
    x = "y"
    while x == "y":
        x = input("Press y to roll and n to stop:")
        if x == "y":
            num1,num2 = roll_dice()
            print("You rolled a", num1, "and", num2)
            if num1 == num2:
                print("Congrats, Game Loading")
                x = "n"
            else:
                print("Unlucky, try again")
        elif x == "n":
            print("Thats all for today folks")
        else:
            print("You must enter y or n")
            x = "y"
#main()


def count_vowel(sentence):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for letter in sentence:
        if letter == "a":
            a += 1
        elif letter == "e":
            e += 1
        elif letter == "i":
            i += 1
        elif letter == "o":
            o += 1
        elif letter == "u":
            u += 1
        else:
            continue
    return a,e,i,o,u

def main():
    sentence = "Learning how to proramme is similar to learning an instrument. Both involve practise and making lost of mistakes. Both require perseverance to develop fluency. Keep going."
    a,e,i,o,u = count_vowel(sentence)
    print(sentence)
    print("Within the sentence there are", a, "A's", e, "E's", i, "I's", o, "o's and", u, "U's.")
    print("in case i don't see ya, good afternoon good evening and goodnight.")
#main()

def highest_number(numbers):
    num = -999
    for i in numbers:
        if i > num:
            num = i
    return num
    

def main():
    numbers = [9,8,72,22,21,81,2,1,11,76,32,54]
    high_number = highest_number(numbers)
    print(high_number)

#main()

def check_password(password):
    weak_pwd = ["password", "qwerty", "123456", "abcdefg", "hello123", "worcester17"]
    if password in weak_pwd:
        print("Password is too weak")
        main()
    elif len(password) < 10:
        print("Password is to short")
        main()
    else:
        print("Password accepted")
            

def main():
    password = input("Enter a new password: ")
    check_password(password)

#main()

def marks(des_grade):
    grades = [["A*","90"],["A","83"],["B","72"],["C","60"],["D","49"],["E","30"]]
    marks = ""
    for i in range(len(grades)):
        if grades[i][0] == des_grade:
            marks = grades[i][1]
    return marks

def main():
    desired_grade = input("Enter your desired grade: ")
    desired_grade = desired_grade[0].upper()
    req_mark = marks(desired_grade)
    print("To achieve", desired_grade,"you will need a mark of",req_mark)
#main()

def penalty(score):
    keeper = ["left", "right", "centre"]
    for i in range(5):
        shot = input("Enter left, right or centre to shoot in that direction: ")
        shot = shot.lower()
        save = random.choice(keeper)
        if shot == save:
            print("AND the keepers saved it, unlucky.")
        else:
            print("GOAL!!!!")
            score += 1
    return score      

def main():
    score = 0
    print("Welcome to the penalty shoot out.")
    play = input("Enter y to play n to forfiet: ")
    if play == "n":
        print("Shame i was looking forward to kicking your ass")
    elif play == "y":
        print("Game on")
        score = penalty(score)
    else:
        print("You must select from the options")
        main()
    print("You scored",score,"/5")

#main()



def create_user():
    firstname = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    user_name = surname.title() + firstname[0]
    file = open("User.txt", "r")
    user_file = file.read()
    tmp = [user_file]
    x = False
    print(tmp)
    for i in range(len(tmp)):
        print(i)
        if tmp[i][0] == user_name:
            x = True
    if x == True:
        user_name = user_name + "#"
    print("Your username is", user_name)
    file.close()
    return user_name

def create_password():
    user_password = input("Enter your password: ")
    weak_pwd = ["password", "qwerty", "123456", "abcdefg", "hello123", "worcester17"]
    x = True
    while x == True:
        if user_password in weak_pwd:
            print("Password is too weak")
        elif len(user_password) < 10:
            print("Password is to short")
        else:
            print("Password accepted")
            x = False
    return user_password

def app_user(user_name, user_password):
    new_user = [user_name,user_password]
    file = open("User.txt", "a")
    new_user = str(new_user)
    file.write(new_user)
    print("User has been added to file")
    file.close()
    
def main():
    file = open("User.txt","a")
    file.close()
    print("New User Menu")
    print()
    print("1) Create User 2) Exit")
    selection = int(input("Enter your selection: "))
    if selection == 1:
        username = create_user()
        password = create_password()
        app_user(username,password)
        main()
    elif selection == 2:
        change_user()
        main()
    else:
        print("Thats all folks")

#main()
#Above program does not work

def find_mean(number_lst):
    count = 0
    for i in number_lst:
        count += i
    print("The randomly generated list of numbers =", count)
    mean = count / len(number_lst)
    return mean
    
def main():
    lst = []
    for i in range(10):
        lst.append(random.randint(1,100))
    print(lst)
    mean = find_mean(lst)
    print("The mean from the randomly generated list of numbers =", mean)
#main()


def main():
     cs_scores = [["Karman",45,60,72],
                 ["Daniel",55,65,70],
                 ["Giacomo",71,78,78],
                 ["Jessica",68,79,80],
                 ["Edie",98,85,91]]
     for i in range(len(cs_scores)):
         print(cs_scores[i][0],"Scored",cs_scores[i][1], cs_scores[i][2],cs_scores[i][3])
         print(cs_scores[i][0],"Scored a total of", cs_scores[i][1] + cs_scores[i][2] + cs_scores[i][3])
         print(cs_scores[i][0],"Scored an average of", (cs_scores[i][1] + cs_scores[i][2] + cs_scores[i][3])/3)
#main()

def hex_to_den(hex_dec):
    hex_dic = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,"a":10,"b":11,"c":12,
               "d":13,"e":14,"f":15}
    denary = hex_dic[hex_dec]
    return denary
    

def main():
    hex_dec = input("Enter a single digit hexidecimal number: ")
    denary = hex_to_den(hex_dec)
    print(hex_dec, "=", denary)
main()
    
