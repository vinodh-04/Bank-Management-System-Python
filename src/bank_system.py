# Bank Management System - Main Module

from account import BankAccount
import random

DATA_FILE = "../data/accounts.txt"

def show_menu():
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Exit")
    print("==================================")

def generate_account_number():
    return random.randint(100000, 999999)

def create_account():
    print("\n--- Create New Account ---")
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))

    acc_number = generate_account_number()
    account = BankAccount(name, acc_number, initial_deposit)

    # Save to file
    with open(DATA_FILE, "a") as file:
        file.write(f"{account.name},{account.account_number},{account.balance}\n")

    print("\nAccount Created Successfully!")
    print("Account Number:", account.account_number)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            print("Thank you for using Bank Management System!")
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
