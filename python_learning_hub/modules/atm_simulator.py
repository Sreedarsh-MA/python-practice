def run_atm_simulator():
    """
    A basic ATM simulator for PIN verification and withdrawals.
    Refactored from lesson3.py
    """
    print("\n--- ATM Simulator ---")
    correct_pin = 12345
    balance = 1000

    try:
        user_pin = int(input("Enter your 5-digit PIN number: "))

        if user_pin == correct_pin:
            print("PIN Verified Successfully!")
            amount = int(input("Enter the amount you want to withdraw: "))

            if amount <= 0:
                print("Error: Please enter a positive amount to withdraw.")
            elif amount > balance:
                print(f"Insufficient balance. Your current balance is ${balance}.")
            else:
                balance -= amount
                print(f"Withdrawal successful! Your new balance is ${balance}.")
        else:
            print("Error: Invalid PIN number. Please try again.")

    except ValueError:
        print("\nError: Invalid input. Please enter numbers only for PIN and amount.")
