# Script: 03_even_odd_loop.py
# Topic: Input validation with loops and exception handling
# Description:
# This script prompts the user to enter a number.
# It ensures the number is valid 
# and then uses a loop to determine 
# if each number from 1 to the user's number is even or odd.   

try:
    # Get a number from the user
    number = int(input("Enter a number: "))
    
    # Loop through numbers from 1 to the user's number
    for i in range(1, number + 1):
        if i % 2 == 0:
            print(f"{i} is even.")
        else:
            print(f"{i} is odd.")
    
except ValueError:
    print("That's not a valid number. Please enter a whole number.")