import random
import sys
from enum import Enum #enum : module Enum → class inside that module

class Choices(Enum):  # An Enum (Enumeration) defines a fixed set of named constants(Rock(1), Paper(2), Scissors(3)).
    ROCK = 1 
    PAPER = 2
    SCISSORS = 3

# just to show what enum is and how it works, you can ignore this part for now

# print(Choices(2))
# print(Choices(2).name)
# print(Choices(2).value)
  


print("")

# taking input from the user and type casting it to integer
player_choice = int(input("Enter your choice\n 1 for Rock,\n 2 for Paper, \n 3 for Scissors:\n\n "))

# taking input from the computer and type casting it to integer
computer_choice = int(random.choice('123')) 


# checking if the player has entered a valid input or not
if player_choice > 3 or player_choice < 1:
    print("Invalid input! Please enter a number between 1 and 3.")
    sys.exit() # Exiting the program if the input is invalid

print("")

# 1 way to display the choices of the player and computer
 
# print("Player's choice: ", playerchoice)
# print("Computer's choice: ", computerchoice)
 

# 2 way to display the choices of the player and computer using enum
print("Your's choice: " + Choices(player_choice).name)
print("Computer's choice: " + Choices(computer_choice).name)

print("")
# Actual Logic of the game
if player_choice==1 and computer_choice == 3:
    print("Player wins! 😭") #win + . -> for emojis
elif player_choice==2 and computer_choice == 1:
    print("Player wins! 😫")
elif player_choice==3 and computer_choice == 2:
    print("Player wins! 😒")
elif player_choice== computer_choice:
    print("It's a tie! 😂")

else : 
    print("Computer wins! 😏")




