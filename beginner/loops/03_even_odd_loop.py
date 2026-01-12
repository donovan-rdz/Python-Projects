try:
    number = int(input("Enter a number: "))
    for i in range(1, number + 1):
        if i % 2 == 0:
            print(f"{i} is even.")
        else:
            print(f"{i} is odd.")
    
except ValueError:
    print("That's not a valid number. Please enter a whole number.")