# Script: 02_or.py
# Topic: Logical Operators (or)
# Description:
# This script checks a user's role to determine if they have access
# to the system. Access is granted if the user is an admin OR a moderator.

while True:
    # Ask the user for their role
    role_input = input("Enter your role (admin/moderator/user): ").lower()
    
    # Remove extra spaces from the input
    role = role_input.strip()
    
    # OR operator: only one of these conditions needs to be true
    if role == "admin" or role == "moderator":
            print("You have access to the system.")
            
    # User role does not grant access
    elif role == "user":
            print("You don't have access to the system.")
            break # End program after successful access
    
    # Handle invalid role input
    else:
            print("Invalid role entered.")
    