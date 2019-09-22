# RockPaperScissors
# Dulhan

import random

length = 0.0
width = 0.0
programLoop = True
wins = 0
loses = 0
ties = 0

while programLoop:
    print("Menu")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    print("wins:", wins)
    print("loses:", loses)
    print("ties:", ties)
    text = input("Please enter your choice (number or word): ")

    list = ["rock", "paper", "scissors"]
    move = random.choice(list)

    if text == "1" or text == "rock":
        print("Your move is rock")
        print("computer move is:", move)
        if move == "paper":
            print("Sorry, you lost")
            loses = loses + 1
        elif move == "scissors":
            print("You win, nice!")
            wins = wins + 1
        elif move == "rock":
            print("You tied!")
            ties = ties + 1

    elif text == "2" or text == "paper":
        print("Your move is paper")
        print("computer move is:", move)
        if move == "scissors":
            print("Sorry, you lost")
            loses = loses + 1
        elif move == "rock":
            print("You win, nice!")
            wins = wins + 1
        elif move == "paper":
            print("You tied!")
            ties = ties + 1
    elif text == "3" or text == "scissors":
        print("Your move is scissors")
        print("computer move is:", move)
        if move == "rock":
            print("Sorry, you lost")
            loses = loses + 1
        elif move == "paper":
            print("You win, nice!")
            wins = wins + 1
        elif move == "scissors":
            print("You tied!")
            ties = ties + 1


    elif text == "4":
        programLoop = False
        print("Program Exiting")

    else:
        print("You have entered an incorrect value. Please try again.")

input("Press enter to continue")
