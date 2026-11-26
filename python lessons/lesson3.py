correct_pin=12345
balance=1000
user_pin=int(input("enter your pin number: "))
if user_pin == correct_pin:
    amount=int(input("enter the amount you want to withdraw: "))
    if amount > balance:
        print("insufficiant balance")
    else:
        balance=balance-amount
        print(f"withdraw successfulyour new balance is {balance}")

elif user_pin!= correct_pin:
    print("invalid pin number")
else:
    print("enter the amount needed to be withdrawen")



