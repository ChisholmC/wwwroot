# Cameron Chisholm
# w0488566
# 2023-09-25
# Version 1.82

# Ask the user for their name and their age in years
while True:
    user_name = input("Please Enter Your Name: ")
    age_in_years = input("Please Enter your age in years: ")

    # Determine if the user input a valid age (or if they are 0 years old)
    if age_in_years.isdigit():
        age_in_years = int(age_in_years)  # Convert age_in_years to an integer

        if age_in_years == 0:
            print("You were either born today or you haven't been born yet!")
        else:
            # Calculate the current year
            current_year = 2023

            # Determine the birth year
            birth_year = current_year - age_in_years

            # Display the user's birth year
            print(f"{user_name}, you were born in the year {birth_year}")
        break  # Exit the loop when valid input is provided
    else:
        print("Please enter a valid age as a number.")

        