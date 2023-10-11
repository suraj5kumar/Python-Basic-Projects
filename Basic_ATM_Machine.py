"""
A program that simulates a basic ATM machine. The program will display a menu with options such as:

1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Quit

Implementing these options using a while loop to allow the user to
perform multiple transactions until they choose to quit.

Assuming an initial balance of 10000rs.
"""


def atmMachine():
    pin = 9876
    balance = 10000
    incorrect = 0

    print("Welcome to ABC Bank")
    while True:
        p = int(input("Enter your 4 digit pin: "))
        if p == pin:
            while True:
                print()
                print("Welcome XYZ Kumar")
                print("Please select one option from below to proceed.")
                print("1. Check Balance")
                print("2. Deposite Money")
                print("3. Withdraw Money")
                print("4. Quit")
                option = int(input("Enter the option number to proceed: "))
                if option == 1:
                    print()
                    print(f"Available Balance: {balance}")
                elif option == 2:
                    deposite = int(input("Enter money to deopsite: "))
                    balance += deposite
                    print()
                    print(f"{deposite}rs deposited successfully")
                    print(f"Updated balance: {balance}")
                elif option == 3:
                    withdraw = int(input("Enter money to withdraw: "))
                    if withdraw <= balance:
                        balance -= withdraw
                        print()
                        print(f"{withdraw}rs withdrawl successfull.")
                        print(f"Remaining balance: {balance}")
                    else:
                        print()
                        print("Sorry, insufficient balance.")
                elif option == 4:
                    print("Transaction successful")
                    exit()
                else:
                    print("Invalid option, try again.")
        else:
            print("Incorrect pin, try again.")
            incorrect += 1

        if incorrect == 3:
            print(
                "You have reached maximum number of attempts. Try again after 30 minutes."
            )
            exit()
        else:
            continue


atmMachine()
