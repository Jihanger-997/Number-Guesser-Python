# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import sys
import time


def number_gen(n):
    if n == 1:
        # easy
        number_generated = random.randint(1, 5)
        print("Pick a number between 1 and 5: ")
    elif n == 2:
        # medium
        number_generated = random.randint(1, 10)
        print("Pick a number between 1 and 10: ")
    elif n == 3:
        # hard
        number_generated = random.randint(1, 20)
        print("Pick a number between 1 and 20: ")
    else:
        # nightmare
        number_generated = random.randint(1, 100)
        print("Pick a number between 1 and 100: ")

    return number_generated


# This is a translation of the java program to python #
# # # # # # # # # # # # # # # # # # # # # # # # # # # #

# variables
continueGame = True
guess = int(0)
generatedNum = int(0)
gameNum = int(0)
winLoss = [False] * 10
wins = int(0)
feedback = float(0)

# initial print
print("N U M B E R  G U E S S E R")
print("   Maximum games: 10")

# main game loop, will execute as long as player wishes or when it reaches 10 games
while continueGame and gameNum < 10:
    print("  Pick Your Difficulty")
    print("--------------------------")
    print("1 for Easy")
    print("2 for Medium")
    print("3 for Hard")
    print("4 for Nightmare")
    print("--------------------------")

    # this will ask for user input
    difficultyInput = input("Choice: ")
    diffInpInt = int(difficultyInput)  # this will transform the input to an int
    print("Round:", (gameNum + 1))  # show game number
    print("")

    # this if checks if input is valid
    if 1 <= diffInpInt <= 4:
        textGen = "Generating a number . . .\n\n"
        for l in textGen:
            sys.stdout.write(l)  # similar to print
            sys.stdout.flush()  # this will flush the buffer of .write
            time.sleep(0.1)  # wait to show text

        # method assignment and call
        generatedNum = number_gen(diffInpInt)
        print("")
        print("ADMIN:Generated num: ", generatedNum) # debug line of code
        guess_raw = input('')
        guess = int(guess_raw)

        # this if else chain will set the array value of the game turn to true if the guess was correct
        if guess == generatedNum:
            print("-------------------")
            print("| You're correct! |")
            print("-------------------\n\n")
            wins += 1
            winLoss[gameNum] = True
        else:
            print("-------------------")
            print("|    Try again!   |")
            print("| The number was", generatedNum)
            print("-------------------\n\n")

        print("Wins:",wins,"-- Games:", (gameNum + 1))
        gameNum += 1

        print("Continue? (input 1 for yes, anything else for no")
        continueInt = input("")
        if continueInt != "1":
            continueGame = False
        print("\n")
        # end of game round (if)
    # end of game (while)

wins = 0 # reset wins variable to count how many games were won from the array list

# this will count how many games you won
for x in winLoss:
    if x:
        wins += 1

print("You played", gameNum, "out of 10 games.")
print("You won", wins, "out of", gameNum, "played games.")

noWins = False

# this sets wins to 0 to avoid errors
if wins == 0:
    wins = 1
    noWins = True

feedback = float(gameNum / wins)
print("ADMIN:",feedback) # debug command
if noWins:
    print("Try leveling up your Luck stat!")
elif feedback == 1.0:
    print("Very good job! You did perfect!")
elif feedback <= 2:
    print("Good job!")
elif feedback < gameNum:
    print("You can do better next time!")
else:
    print("Try leveling up your Luck stat!")

endProgram = input("Enter to Exit") # this line was added to show the remaining text after the game exits the while loop