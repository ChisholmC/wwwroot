# Rock Paper Sissors

# Cameron Chisholm
# W0488566
# IT Generealist
#Date October 4th 2023
#VERSION 1.82



import random

# Global Constants
ROCK = 1
PAPER = 2
SCISSORS = 3

while True:
    # Local Variable user_input
    user_input = input("Press 1 for rock, 2 for paper, 3 for scissors: ")

    # Validate user input
    if user_input.isdigit():
        user_input = int(user_input)
        
        if 1 <= user_input <= 3:
            # Calculate the computer's value
            computer_value = random.randint(1, 3)

            if user_input == computer_value:
                print("Tie Game")
            elif (user_input == ROCK and computer_value == SCISSORS) or \
                 (user_input == PAPER and computer_value == ROCK) or \
                 (user_input == SCISSORS and computer_value == PAPER):
                print("You Win!")
            else:
                print("Computer Wins!")
        else:
            print("Invalid input. Please enter 1 for rock, 2 for paper, or 3 for scissors.")
    else:
        print("Invalid input. Please enter a digit (1, 2, 3).")

        
