"""
ui.py
User interface helpers: menus, input prompts, and result display.
"""


def display_menu() -> None:
    """Print the main navigation menu."""
    print("What would you like to do?")
    print("  [1] Evaluate an expression")
    print("  [2] Solve a linear equation")
    print("  [3] Solve a quadratic equation")
    print("  [4] Exit")
    print()


def get_user_input(prompt: str) -> str:
    """Read a line of input from the user."""
    return input(f"  {prompt}")


def display_result(result: dict) -> None:
    """Display the result or error returned by the calculator."""
    print()
    if result.get("success"):
        print(f"Result: {result['result']}")
    else:
        print(f"Error: {result.get('error', 'Unknown error')}")
    print()
