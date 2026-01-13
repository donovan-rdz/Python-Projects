while True:
    age_input = input("Please enter your age: ")

    try:
        age = int(age_input)

        if age < 0:
            print("Age cannot be negative. Please try again.")
        else:
            print(f"You have entered a valid age: {age}")
            break

    except ValueError:
        print("Invalid input. Please enter a whole number.")
