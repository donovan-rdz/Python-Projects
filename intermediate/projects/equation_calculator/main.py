"""
Equation Calculator
Entry point of the application.
"""

from src.calculator import EquationCalculator
from src.ui import display_menu, get_user_input, display_result


def main():
    calculator = EquationCalculator()
    print("\n========================================")
    print("       EQUATION CALCULATOR v1.0         ")
    print("========================================\n")

    while True:
        display_menu()
        choice = get_user_input("Select an option: ").strip()

        if choice == "1":
            expr = get_user_input("Enter expression (e.g. 2 + 3 * x, x=5): ")
            result = calculator.evaluate(expr)
            display_result(result)

        elif choice == "2":
            eq = get_user_input("Enter linear equation (e.g. 2x + 3 = 7): ")
            result = calculator.solve_linear(eq)
            display_result(result)

        elif choice == "3":
            eq = get_user_input("Enter quadratic equation (e.g. x^2 - 5x + 6 = 0): ")
            result = calculator.solve_quadratic(eq)
            display_result(result)

        elif choice == "4":
            print("\nGoodbye!\n")
            break

        else:
            print("\nInvalid option. Please try again.\n")


if __name__ == "__main__":
    main()
