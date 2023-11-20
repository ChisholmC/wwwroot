import random

# Step 1: Create lists of programming languages and difficulty levels
programming_languages = ["Python", "Javascript", "C++", "Ruby", "Java"] 
difficulty_levels = [1, 2, 3, 4, 5]

# Step 2: Combine the two lists into a list of tuples
quiz_data = list(zip(programming_languages, difficulty_levels))

# Step 3: Shuffle the list for a random quiz order 
random.shuffle(quiz_data)

score = 0
for language, difficulty in quiz_data:
    guess = int(input(f"What is the difficulty level of {language}? (Enter a number from 1 to 5)"))
    
    # Check if the guess is correct
    if guess == difficulty:
        print("Correct!")
        score += 1
    else:
        print(f"Oops! The correct difficulty level of {language} is {difficulty}")

# Print the final score after the loop
print("\nQuiz Complete! Your final score:", score)





