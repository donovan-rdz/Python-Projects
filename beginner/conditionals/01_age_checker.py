# Script: 01_age_checker.py
# Topic: Conditionals (if / elif / else)
# Description:
# This script asks the user for their age 
#  and classifies them as a minor or an adult.


# Ask the user to enter their age as text input
age_input = input("Enter your age: ")
try:
    
    # Attempt to convert the input into an integer
    age = int(age_input)

    # Validate age range and classify user
    if age < 0:
        print("Age cannot be negative.")
    elif age < 18:
        print("You are a minor.")
    elif age == 18:
        print("You are exactly 18 - you are an adult.")
    else:
        print("You are an adult.")

# Handle case where input is not a valid whole number
except ValueError:
    print("Invalid input. Please enter a whole number.")
