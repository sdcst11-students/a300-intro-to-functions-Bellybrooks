"""
Task 2:
Create a program to play a number guessing game
There should be a function:
title()
displays instructions and how to play

game()
plays the games
"""
import random
def number_guessing_game():
    secret_number=random.randint(1,100)
    attempts=0

    while True:
        guess=int(input("guess a number between 1 and 100:"))
        attempts+=1
        if guess<secret_number:
            print("too low!")
        elif guess> secret_number:
            print("too hight!")
        else:
            print("congratulations! you guessed the number in",attempts,"attempts.")
            break
number_guessing_game()
        