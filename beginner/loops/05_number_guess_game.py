import random

num_attempts = 5
attempts_used = 0
number_to_guess = random.randint(1, 10)
while num_attempts > 0:
    user_input = input(f"You have {num_attempts} attempts left. Guess a number between 1 and 10: ")
    try:
        guess = int(user_input)
        if guess < 1 or guess > 10:
            num_attempts -= 1
            attempts_used += 1
            
            print("Please enter a number between 1 and 10.")
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the correct number!")
            print(f"You've guessed the number in {attempts_used + 1} attempts!")
            break
        else:
            num_attempts -= 1
            attempts_used += 1
            if num_attempts == 0:
                print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")
            else:
                print("Incorrect guess. Try again.")
    
    except ValueError:
        print("That's not a valid number. Please try again.")