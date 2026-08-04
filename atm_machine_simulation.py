def atm():
    """
    Basic ATM Simulation.

    Features:
    - Balance Check
    - Deposit
    - Withdraw
    - Transaction History
    - Bank Name
    - Account Holder Name

    Returns:
        None
    """

    bank_name = input("Enter Bank Name: ")
    account_holder = input("Enter Account Holder Name: ")

    balance = 5000

    transaction_history = []

    while True:

        print("\n========== ATM MENU ==========")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose Option: ")

        # Check Balance
        if choice == "1":

            print("\nCurrent Balance =", balance)

        # Deposit Money
        elif choice == "2":

            amount = float(input("Enter Deposit Amount: "))

            balance = balance + amount

            print(amount, "Added Successfully.")
            print("Total Balance =", balance)

            transaction_history.append("Deposit : +" + str(amount))

        # Withdraw Money
        elif choice == "3":

            amount = float(input("Enter Withdraw Amount: "))

            if amount <= balance:

                balance = balance - amount

                print(amount, "Debited Successfully.")
                print("Remaining Balance =", balance)

                transaction_history.append("Withdraw : -" + str(amount))

            else:

                print("Insufficient Balance")

        # Transaction History
        elif choice == "4":

            if len(transaction_history) == 0:

                print("\nNo Transaction Found")

            else:

                print("\n===== Transaction History =====")

                for transaction in transaction_history:

                    print(transaction)

        # Exit
        elif choice == "5":

            print("\nThank You For Visiting")
            print(bank_name)
            print("Account Holder :", account_holder)

            break

        else:

            print("Invalid Choice")


atm()
