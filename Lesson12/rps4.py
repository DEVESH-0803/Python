import random
import sys
from enum import Enum 

# Outer function to create a closure for the game state
def rps():
    game_count = 0
    player_win_count = 0
    computer_win_count = 0

 # Inner function that will be called to play the game
    def play_rps(): 
        nonlocal player_win_count
        nonlocal computer_win_count

        class Choices(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_choice = (input("\nEnter your choice\n 1 for Rock,\n 2 for Paper, \n 3 for Scissors:\n\n "))
        computer_choice = random.choice("123") 

        if player_choice not in ['1', '2', '3']:
            print("Enter a number between 1 and 3 only.\n")
            return play_rps()

        player = int(player_choice)
        computer = int(computer_choice)
        print("Your's choice: " + Choices(player).name)
        print("Computer's choice: " + Choices(computer).name + '\n')

        def decide_winner(player, computer):
            nonlocal player_win_count
            nonlocal computer_win_count
            if player == 1 and computer == 3:
                player_win_count += 1
                return "Player wins! 😭\n"
            elif player == 2 and computer == 1:
                player_win_count += 1
                return "Player wins! 😫\n"
            elif player == 3 and computer == 2:
                player_win_count += 1
                return "Player wins! 😒\n"
            elif player == computer:
                return "It's a tie! 😂\n"
            else:
                computer_win_count += 1
                return "Computer wins! 😏\n"

        result = decide_winner(player, computer)
        print(result)

        nonlocal game_count
        game_count += 1

        print(f"Game count: {game_count}")
        print(f"Player's wins: {player_win_count}")
        print(f"Computer's wins: {computer_win_count}")
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

    return play_rps  # Return the inner function to be called later(closure)

   
play = rps() # Call the outer function to get the inner function (closure)

play()


