def main_menu():
    print("Welcome to the Mini Utility System!")
    print("Please select an option:")
    print("1. Math Utility")
    print("2. Text Utility")
    print("3. Exit")
    
    return input("Enter your choice: ").strip()

def get_two_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        raise ValueError("Cannot divide by zero.")

def math_utility():
    while True:
        print("\nMath Utility")
        print("1. Add two numbers")
        print("2. Subtract two numbers")
        print("3. Multiply two numbers")
        print("4. Divide two numbers")
        print("5. Return to main menu")

        choice = input("Enter your choice: ").strip()

        match choice:
            case "1":
                num1, num2 = get_two_numbers()
                print(f"The sum of {num1} and {num2} is {add(num1, num2)}.")
            case "2":
                num1, num2 = get_two_numbers()
                print(f"The difference between {num1} and {num2} is {subtract(num1, num2)}.")
            case "3":
                num1, num2 = get_two_numbers()
                print(f"The product of {num1} and {num2} is {multiply(num1, num2)}.")
            case "4":
               try:
                    num1, num2 = get_two_numbers()
                    result = divide(num1, num2)
                    print(f"The quotient of {num1} and {num2} is {result}.")
               except ValueError as e:
                    print(e)
            case "5":
                break
            case _:
                print("Invalid choice. Please select a valid option.")
                
def count_characters(text):
    return len(text)

def to_uppercase(text):
    return text.upper()                
                
                
def text_utility():
    while True:
        print("\nText Utility")
        print("1. Count characters in a string")
        print("2. Capitalize a string")
        print("3. Return to main menu")

        choice = input("Enter your choice: ").strip()        

        match choice:
            case "1":
                text = input("Enter a string: ")
                print(f"The number of characters in the string is {count_characters(text)}.")
            case "2":
                text = input("Enter a string: ")
                print(f"The capitalized string is: {to_uppercase(text)}")
            case "3":
                break
            case _:
                print("Invalid choice. Please select a valid option.")

def main():
    running = True

    while running:
            choice = main_menu()

            match choice:
                case "1":
                    math_utility()
                case "2":
                    text_utility()
                case "3":
                    print("Exiting the Mini Utility System. Goodbye!")
                    running = False
                case _:
                    print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()