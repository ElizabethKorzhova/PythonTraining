"""This module is designed for expense tracking and developing console interface for user."""

total_expense: float = 0.0


def add_expense(expense: float) -> None:
    """Function to add the expense to the total."""
    global total_expense
    total_expense += expense


def get_expense() -> float:
    """Function to get the expense."""
    return total_expense


while True:
    choice = input("Choose the option: add expense (a) or get expense (g) or exit (any key): ")
    if choice == "a":
        new_expense = float(input("Enter your new expense: "))
        add_expense(new_expense)
        print("New expense has been added")
    elif choice == "g":
        print(f"Total expense: {get_expense()}")
    else:
        print("Goodbye")
        break
