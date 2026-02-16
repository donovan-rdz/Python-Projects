# Script: 03_even_or_odd.py
# Topic: Conditionals (if / elif / else)
# Description:
# This script asks the user for a number and determines if it is even or odd.

try:
    # Ask the user to enter a number and attempt to convert it to an integer
    number = int(input("Enter a number: "))
    
    # Validate the number and determine if it is even or odd
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")
# Handle case where input is not a valid whole number
except ValueError:
    print("That's not a valid number. Please enter a whole number.")