from modules.user_profile import run_user_profile
from modules.grade_checker import run_grade_checker
from modules.atm_simulator import run_atm_simulator

def main():
    """
    Main entry point for the Python Learning Hub.
    Provides a menu to select and run different lesson modules.
    """
    while True:
        print("\n" + "="*30)
        print("  PYTHON LEARNING HUB  ")
        print("="*30)
        print("1. User Profile & Age Calculator")
        print("2. Grade Checker")
        print("3. ATM Simulator")
        print("4. Exit")
        print("-" * 30)

        choice = input("Select an option (1-4): ")

        if choice == '1':
            run_user_profile()
        elif choice == '2':
            run_grade_checker()
        elif choice == '3':
            run_atm_simulator()
        elif choice == '4':
            print("\nThank you for using the Python Learning Hub. Goodbye!")
            break
        else:
            print("\nInvalid choice, please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
