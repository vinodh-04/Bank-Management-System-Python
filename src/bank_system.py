# Bank Management System - Main Module

from account import BankAccount

def show_menu():
    print("\n===== BANK MANAGEMENT SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. View Account Details")
    print("6. Exit")
    print("==================================")

if __name__ == "__main__":
    show_menu()
