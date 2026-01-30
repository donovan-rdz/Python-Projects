# Script: 01_match_case_selector.py
# Topic: match / case
# Description:
# This script demonstrates how to use match/case
# to handle menu-like user selections.

input_option = input("Select an option:\n 1. Option 1\n 2. Option 2\n 3. Exit\n").strip()
match input_option:
    case "1":
        print("You selected option 1.")
    case "2":
        print("You selected option 2.")
    case "3":
        print("Exiting program.")
    case _:
        print("Invalid option selected. Please choose 1, 2, or 3.")