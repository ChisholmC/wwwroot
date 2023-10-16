# Guessing Game

# Cameron Chisholm
# W0488566
# IT Generealist
#Date October 4th 2023
#VERSION 1.82

import random

print("Hello, what's your name?")
username = input("Enter your username: ")
print("Hello " + username + ", welcome to my guessing game. I will pick a number between 1 and 10, and you have 5 tries to guess it!")

num = random.randint(1, 10)
attempts = 0
max_attempts = 5

while attempts < max_attempts:
    guess = input("Guess a number between 1 and 10: ")
    
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    
    guess = int(guess)
    attempts += 1

    if guess == num:
        print("Congratulations, you won! The number was", num)
        break
    else:
        if attempts < max_attempts:
            print("Nope, sorry. You have", max_attempts - attempts, "tries left.")
        else:
            print("Nope, sorry. You're out of tries. The number was", num)
