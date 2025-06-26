#create a Guess the Number Game

import random
start = True

while(start):
    rnd = random.randint(1, 10)
    print("Guess the Number Game", end="")
    user = int(input("Enter Number: "))
    if user > rnd:
        print("Greater Than")
        print("Restart")
    elif user < rnd:
        print("Less Than")
        print("Restart")
    elif user == rnd:
        print("Correct")
        print("Restart")
        break
    else:
        print("Something Went Wrong")
        print("Restart")
