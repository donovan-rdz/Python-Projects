# Script: 01_and.py
# Topic: Logical Operators (and)
# Description:
# This script checks if a person is an adult and has a valid ID
# to determine if they can enter a venue.

while True:
    # Ask the user for their age
    age_input = input("Enter your age: ")
    # Validate and convert the input to an integer
    try:
        age = int(age_input)
        
        # Check if the user is an adult
        if age <= 0:
            print("Age cannot be negative nor 0.")
            continue   
        elif age < 18:
            print("You are a minor.")
            break
        else:
            print("You are an adult.")
        
        id_input = input("Do you have a valid ID? (yes/no): ").lower()
        # AND operator: user must be adult AND have a valid ID
        if id_input == "yes" and age >= 18:
                print("You can enter the venue.")
        else:
                print("You cannot enter the venue.")
        break   # End the program because minors cannot continue 
    except ValueError:
        print("Invalid input. Please enter a whole number.")