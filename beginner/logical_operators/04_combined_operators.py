# Script: 04_combined_operators.py
# Topic: Logical Operators (and, or, not)

while True:
    age_input = input("Enter your age: ")
    try:
        age = int(age_input)
        if age <= 0:
            print("Age cannot be negative nor zero. Please try again.")
            continue
        elif age < 18:
            print("You are a minor and cannot proceed.")
            break
        else:
            print("You are an adult.")
        id_input = input("Do you have permission? (yes/no): ").lower()
        if id_input == "yes":
            has_permission = True
        elif id_input == "no":
            has_permission = False
           
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        
        guest_input = input("Are you a guest? (yes/no): ").lower()
        if guest_input == "yes":
            is_guest = True
        elif guest_input == "no":
            is_guest = False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        
        is_blocked_input = input("Are you blocked? (yes/no): ").lower()
        if is_blocked_input == "no":
            is_blocked = False
        elif is_blocked_input == "yes":
            is_blocked = True
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue
        if age >= 18 and (has_permission or is_guest) and not is_blocked:
            print("Access granted.")
        else:
            print("Access denied.")
        break
    except ValueError:
        print("Invalid input. Please enter a whole number.")