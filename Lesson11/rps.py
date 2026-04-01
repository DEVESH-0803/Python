import random
import sys
from enum import Enum 

# used a global variable to keep track of the number of games played
# Used nested fxn.

game_count = 0

def play_rps():

    class Choices(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = int(input("\nEnter your choice\n 1 for Rock,\n 2 for Paper, \n 3 for Scissors:\n\n "))
    computerchoice = random.randint(1, 3) 

    if playerchoice not in [1, 2, 3]:
        print("Enter a number between 1 and 3 only.\n")
        return play_rps()
    
    player = int(playerchoice)
    computer = int(computerchoice)


    print("Your's choice: " + Choices(playerchoice).name)
    print("Computer's choice: " + Choices(computerchoice).name + '\n')

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "Player wins! 😭\n"
        elif player == 2 and computer == 1:
            return "Player wins! 😫\n"
        elif player == 3 and computer == 2:
            return "Player wins! 😒\n"
        elif player == computer:
            return "It's a tie! 😂\n"
        else:
            return "Computer wins! 😏\n"

    result = decide_winner(player, computer)
    print(result)

    global game_count
    game_count += 1

    print(f"Game count: {game_count}")
    print(f"Play Again?")

    while True:
         play_again = input('\n Y for Yes \n N for NO \n' )
         if play_again.lower() not in ['y', 'n']:
             continue
         else:
             break 

    if play_again.lower() != 'y':
      print("Thanks You for playing!")
      sys.exit('Bye! 😭')
    else:
        play_rps()

   
play_rps()


