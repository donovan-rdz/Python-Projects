import random

while True:
    print("\nWelcome to the interactive menu!")
    print("Please select an option:")
    input_option = input("1. Option 1\n2. Option 2\n3. Exit\n").strip()
    match input_option:
        case "1": 
            print("Hello!")
        case "2":
            num = random.randint(1, 100)
            print(f"Your number is: {num}")
        case "3":
            print("Exiting program. Goodbye!")
            break
        case _:
            print("Invalid option selected. Please choose 1, 2, or 3.")