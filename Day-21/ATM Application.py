import random
balance = 10000
# Generate a 4-digit PIN
pin = random.randint(1000, 9999)
print("Your ATM PIN is:", pin)
entered_pin = int(input("Enter your PIN: "))
if entered_pin == pin:
    while True:
        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Your balance is: ₹", balance)
        elif choice == 2:
            amount = float(input("Enter deposit amount: ₹"))
            if amount > 0:
                balance += amount
                print("Deposit successful!")
                print("New balance: ₹", balance)
            else:
                print("Invalid amount.")
        elif choice == 3:
            amount = float(input("Enter withdrawal amount: ₹"))
            if amount > balance:
                print("Insufficient balance.")
            elif amount <= 0:
                print("Invalid amount.")
            else:
                balance -= amount
                print("Please collect your cash.")
                print("Remaining balance: ₹", balance)
        elif choice == 4:
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid choice.")
else:
    print("Incorrect PIN!")