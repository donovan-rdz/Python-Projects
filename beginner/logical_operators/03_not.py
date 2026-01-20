# Script: 03_not.py
# Topic: Logical Operators (not)
# Description:
# This script checks if a user is NOT blocked.
# Access is granted only when the user is not blocked.

while True:
    #Ask the user if they are blocked
    is_blocked_input = input("Are you blocked? (yes/no): ").lower()
    
    if is_blocked_input == "no":
            is_blocked = False
    elif is_blocked_input == "yes":
            is_blocked = True
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
        continue #Asks again if the input is invalid
    
    # NOT operator: access is granted if the user is NOT blocked
    if not is_blocked:
            print("Access granted.")
    else:
            print("Access denied.")
    break  # End program after successful access
   