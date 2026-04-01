import random
import sys
from enum import Enum 

def play_rps():

    class Choices(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = int(input("\nEnter your choice\n 1 for Rock,\n 2 for Paper, \n 3 for Scissors:\n\n "))
    computerchoice = random.randint(1, 3) 

    if playerchoice not in [1, 2, 3]:
        print("Please enter a number between 1 and 3.\n")
        return play_rps()


    print("Your's choice: " + Choices(playerchoice).name)
    print("Computer's choice: " + Choices(computerchoice).name + '\n')

    if playerchoice==1 and computerchoice == 3:
        print("Player wins! 😭\n")
    elif playerchoice==2 and computerchoice == 1:
        print("Player wins! 😫\n")
    elif playerchoice==3 and computerchoice == 2:
        print("Player wins! 😒\n")
    elif playerchoice== computerchoice:
        print("It's a tie! 😂\n")
    else : 
        print("Computer wins! 😏\n")

# Ask the player if they want to play again in  a loop until they provide a valid input
    while True:
         play_again = input(' Play Again? \n Y for Yes \n N for NO \n' )
         if play_again.lower() not in ['y', 'n']:
             continue
         else:
             break 
# If the player does not want to play again, exit the game. Otherwise, start a new game.
    if play_again.lower() != 'y':
      print("Thanks You for playing!")
      sys.exit('Bye! 😭')
    else:
        play_rps()

   
play_rps()


