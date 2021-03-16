import random
a = random.randint(0,9)
b = random.randint(0,9)
while a == b:
    b = random.randint(0,9)
c = random.randint(0,9)
while c == a or c == b :
    c = random.randint(0,9)
computer_number = int((str(a)+str(b)+str(c)))
a = str(a)
b = str(b)
c = str(c)
while True:
    User_num = input("Guess the 3 digit number from zero to 9 : ")
    User_num = str(User_num)
    x = User_num[0]
    y = User_num[1]
    z = User_num[2]
    if x == a and y == b and z == c :
        print("Congratulations , You guessed the right number ")
        break
    else:
        if x == a or y == b or z == c:
            print("Match")
        else:
            if x == b or x == c or y == a or y == c or z == a or z == b:
                print("Close")
            else:
                print("Sorry , try again")
