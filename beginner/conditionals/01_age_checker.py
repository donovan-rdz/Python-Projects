age_input = input("Enter your age: ")
try:
    age = int(age_input)

    if age < 0:
        print("Age cannot be negative.")
    elif age < 18:
        print("You are a minor.")
    elif age == 18:
        print("You are exactly 18 - you are an adult.")
    else:
        print("You are an adult.")

except ValueError:
    print("Invalid input. Please enter a whole number.")
