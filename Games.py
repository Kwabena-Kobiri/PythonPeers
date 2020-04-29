"""
This file contains several games that our user can play whenever s/he is stressed out
"""
# FUNCTIONS FOR THE VARIOUS GAMES
 
# MODULES TO IMPORT
import random

# WE BEGIN WITH THE NUMBER GUESS GAME

def NumberGuessGame():
    print("\nWanna have some fun?? Then let's play the Guess Game!")
    print("You are to choose a number between a range of numbers\nThe computer would generate a random number between the range provided")
    print("You would then have to make a guess within the provided range. \nYour guess should match that of the computer to be able to win the game")
    print("If you guess wrongly, you would be provided with a couple of chances to try again.\n")

    start = int(input("Enter the starting number of the guess range\n"))
    end = int(input("\nEnter the ending number of the guess range\n"))

    correctGuess = random.randint(start, end)   #Computer-generated guess
    #difference = int(end - start)
    #ratio = range(int((start + end)/difference))
    print("\nI am thinking of a number between ",start," and ",end,"\n")

    for ration in range(1, 4):
        userGuess = int(input("Take a guess\n"))

        if userGuess < correctGuess:
            print("\nYour guess is too low\n")
        elif userGuess > correctGuess:
            print("\nYour guess is too high\n")
        else:
            break

    if userGuess == correctGuess:
        print("Congratulations! You guessed right after trying ", ration, " time(s)")
    else:
        print("I was thinking of the number ", correctGuess, "\n")


NumberGuessGame()
