import random
import sys
from enum import Enum 

class Choices(Enum):  
    ROCK = 1 
    PAPER = 2
    SCISSORS = 3 


while True:

    playerchoice = int(input("\nEnter your choice\n 1 for Rock,\n 2 for Paper, \n 3 for Scissors:\n\n "))
    computerchoice = random.randint(1, 3) 

    if playerchoice > 3 or playerchoice < 1:
        print("Invalid input! Please enter a number between 1 and 3.\n")
        continue


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

    again = input(' Play Again? \n Y for Yes \n N for NO \n' )

    if again.lower() != 'y':
        print("Thanks You for playing!")
        break
sys.exit('Bye! 😭') 


