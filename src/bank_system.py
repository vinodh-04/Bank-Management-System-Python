# Bank Management System - Main Program

from account import BankAccount
from utils import generate_account_number, save_account, load_accounts, update_account_file

def show_menu():
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View Account Details")
    print("6. Exit")
    print("==================================")

def create_account(accounts):
    print("\n--- Create New Account ---")
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))

    acc_number = generate_account_number()
    account = BankAccount(name, acc_number, initial_deposit)

    accounts[acc_number] = (name, initial_deposit)
    save_account(name, acc_number, initial_deposit)

    print("\nAccount Created Successfully!")
    print("Your Account Number:", acc_number)

def deposit_money(accounts):
    acc = int(input("Enter your account number: "))

    if acc in accounts:
        amount = float(input("Enter amount to deposit: "))
        name, balance = accounts[acc]
        balance += amount
        accounts[acc] = (name, balance)
        update_account_file(accounts)
        print("Amount deposited successfully!")
    else:
        print("Account not found!")

def withdraw_money(accounts):
    acc = int(input("Enter your account number: "))

    if acc in accounts:
        amount = float(input("Enter amount to withdraw: "))
        name, balance = accounts[acc]

        if amount <= balance:
            balance -= amount
            accounts[acc] = (name, balance)
            update_account_file(accounts)
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")
    else:
        print("Account not found!")

def check_balance(accounts):
    acc = int(input("Enter your account number: "))

    if acc in accounts:
        name, balance = accounts[acc]
        print(f"Account Holder: {name}")
        print(f"Current Balance: {balance}")
    else:
        print("Account not found!")

def view_account_details(accounts):
    acc = int(input("Enter your account number: "))

    if acc in accounts:
        name, balance = accounts[acc]
        print("\n--- Account Details ---")
        print("Name:", name)
        print("Account Number:", acc)
        print("Balance:", balance)
    else:
        print("Account not found!")

def main():
    accounts = load_accounts()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            deposit_money(accounts)
        elif choice == "3":
            withdraw_money(accounts)
        elif choice == "4":
            check_balance(accounts)
        elif choice == "5":
            view_account_details(accounts)
        elif choice == "6":
            print("Thank you for using Bank Management System!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
