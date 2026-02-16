# Script: 02_interactive_menu.py
# Topic: match / case
# Description:
# This script demonstrates how to use match/case
# to handle an interactive menu.

import random # Used to generate a random number for one of the menu options

# Main program loop - runs until the user chooses to exit
while True:
    print("\nWelcome to the interactive menu!")
    print("Please select an option:")
    
    # Get user input and remove leading/trailing whitespace
    input_option = input("1. Option 1\n2. Option 2\n3. Exit\n").strip()
    
    # Use match/case to handle different menu selections
    match input_option:
        # Case 1: Simple greeting message
        case "1": 
            print("Hello!")
        # Case 2: Generate and display a random number between 1 and 100
        case "2":
            num = random.randint(1, 100)
            print(f"Your number is: {num}")
        # Case 3: Exit the program
        case "3":
            print("Exiting program. Goodbye!")
            break
        # Default case: Handle invalid input
        case _:
            print("Invalid option selected. Please choose 1, 2, or 3.")