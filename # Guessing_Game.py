# Guessing Game

# Cameron Chisholm
# W0488566
# IT Generealist
#Date October 4th 2023
#VERSION 1.82

print("Hello whats your name?")
    
username = input("Enter username:")
print("Hello " + username, "This is my guessing game. i will pick a number between 1 and 10 and you have 5 trys to guess it!")




import random

num = random.randint(1,10)
guess = None


while guess !=num:
    guess = input("Guess a number between 1 and 10: ")
    guess = int(guess)


    if guess == num:
        print("congratulations! you won")
        break
    else:
        print("Nope, sorry. you loose!")

