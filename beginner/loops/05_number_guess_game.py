# Script: 05_number_guessing_game.py
# Topic: Loops, conditionals, and exception handling
# Description:
# This script implements a simple number guessing game.
# The user has a limited number of attempts to guess
# a randomly generated number between 1 and 10.

import random # Used to generate the random target number

# Initialize game configuration
num_attempts = 5
attempts_used = 0
number_to_guess = random.randint(1, 10)

# Main game loop — runs while attempts remain
while num_attempts > 0:
    user_input = input(f"You have {num_attempts} attempts left. Guess a number between 1 and 10: ")
    try:
        # Attempt to convert input into an integer
        guess = int(user_input)
        # Validate that the guess is within the allowed range
        if guess < 1 or guess > 10:
            num_attempts -= 1
            attempts_used += 1
            print("Please enter a number between 1 and 10.")
            
        # Correct guess condition
        elif guess == number_to_guess:
            print("Congratulations! You've guessed the correct number!")
            print(f"You've guessed the number in {attempts_used + 1} attempts!")
            break
        # Incorrect guess condition
        else:
            num_attempts -= 1
            attempts_used += 1
            if num_attempts == 0:
                print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")
            else:
                print("Incorrect guess. Try again.")
                
    # Handle non-numeric input
    except ValueError:
        print("That's not a valid number. Please try again.")