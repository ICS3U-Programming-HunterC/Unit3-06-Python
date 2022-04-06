#!/usr/bin/env python3
# Created by: Hunter Connolly
# Created on: April 5, 2022
# This is a program that generates a random number
# and the user guesses a number, if the user enters something that is not
# an integer than the program will know and let the user know


import random


def main():
    # this function checks if the guess is correct\

    # generate random number
    random_variable = random.randint(1, 9)  # a number between 1 and 9

    # get the user's guess as a string
    guess_as_string = input("Guess a number between 1 and 9: ")
    print("")

    # switch the guess into an int and then check if it is a number and if
    # it is correct or not
    try:
        guess_as_number = int(guess_as_string)
        if guess_as_number == random_variable:
            print("That is CORRECT! :)")
        else:
            print("That is wrong :(")
            print("The correct number was: {}".format(random_variable))
    except Exception:
        print("That is not a number!!")
        print("The correct number was: {}".format(random_variable))
    finally:
        print("")
        print("Thanks for playing!")


if __name__ == "__main__":
    main()
