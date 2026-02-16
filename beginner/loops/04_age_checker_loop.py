# Script: 04_age_checker_loop.py
# Topic: Input validation with loops and exception handling
# Description:
# This script repeatedly prompts the user to enter their age.
# It ensures the value is a non-negative integer before accepting it.

# Main loop - continues until a valid age is entered
while True:
    age_input = input("Please enter your age: ")

    try:
        # Attempt to convert input to integer
        age = int(age_input)
        
        # Validate that age is not negative
        if age < 0:
            print("Age cannot be negative. Please try again.")
        else:
            # Valid input condition — exit loop
            print(f"You have entered a valid age: {age}")
            break
        
    # Handle non-numeric input
    except ValueError:
        print("Invalid input. Please enter a whole number.")
