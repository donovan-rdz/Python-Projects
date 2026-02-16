# Script: 02_number_comparer.py
# Topic: Conditionals (if / elif / else)
# Description:
# This script asks the user for two numbers and compares them.

try:
    # Ask the user to enter two numbers and attempt to convert them to floats
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Validates the numbers and compares them
    if num1 > num2:
        print(f"{num1} is greater than {num2}.")
    elif num1 < num2:
        print(f"{num1} is less than {num2}.")
    else:
        print(f"{num1} is equal to {num2}.")
        
# Handle case where input is not a valid whole number
except ValueError:
    print("Invalid input. Please enter numeric values.")