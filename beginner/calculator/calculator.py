class Calculator:
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b


calc = Calculator()

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Choose operation: ")

    if choice == "5":
        print("Goodbye!")
        break

    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number")
        continue

    if choice == "1":
        print("Result:", calc.add(n1, n2))

    elif choice == "2":
        print("Result:", calc.subtract(n1, n2))

    elif choice == "3":
        print("Result:", calc.multiply(n1, n2))

    elif choice == "4":
        print("Result:", calc.divide(n1, n2))

    else:
        print("Invalid input")