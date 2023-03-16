'''
Author - Swapnil Bondar
Description - Rock Paper Scissors game use by random function in python 
Date - 16-03-2023

'''

import random

while True:

    user_action = input("Enter a choice (rock, paper, scissors): ")

    possible_actions = ["rock", "paper", "scissors"]

    computer_action = random.choice(possible_actions)

    print(f"\nYou Chose {user_action}, Computer Chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both Players selected {user_action}. It's a tie!! ")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!! ")
        else:
            print("Paper covers rock! You lose. ")

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!! ")
        else:
            print("Scissors cuts paper! You lose. ")

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!! ")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
    