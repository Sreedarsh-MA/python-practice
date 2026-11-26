from datetime import datetime

def run_user_profile():
    """
    Collects user information and calculates current age.
    Refactored from lesson 1.py
    """
    print("\n--- User Profile & Age Calculator ---")
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        height = float(input("Enter your height (in cm/m): "))
        birth_year = int(input("Enter your birth year (YYYY): "))

        current_year = datetime.now().year
        calculated_age = current_year - birth_year

        print("\n--- Profile Summary ---")
        print(f"Hello {name}!")
        print(f"Age: {age}")
        print(f"Height: {height}")
        print(f"Based on your birth year, you are {calculated_age} years old.")
    except ValueError:
        print("\nError: Invalid input. Please enter numbers for age, height, and birth year.")
