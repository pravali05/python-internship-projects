
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r", newline="") as file:
        return list(csv.DictReader(file))

def save_expenses(expenses):
    with open(FILE_NAME, "w", newline="") as file:
        fields = ["date", "category", "amount", "description"]
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(expenses)

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        datetime.strptime(date, "%Y-%m-%d")
        category = input("Enter category: ").strip()
        amount = float(input("Enter amount: "))
        if not category or amount <= 0:
            raise ValueError
        description = input("Enter description: ")

        expenses = load_expenses()
        expenses.append({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })
        save_expenses(expenses)
        print("Expense added successfully!")

    except ValueError:
        print("Invalid date or amount!")

def view_expenses():
    expenses = load_expenses()
    for expense in expenses:
        print(expense)

def filter_expenses():
    category = input("Enter category to filter: ").lower()
    expenses = load_expenses()
    for expense in expenses:
        if expense["category"].lower() == category:
            print(expense)

def category_summary():
    expenses = load_expenses()
    totals = {}
    for expense in expenses:
        category = expense["category"]
        totals[category] = totals.get(category, 0) + float(expense["amount"])

    for category, total in totals.items():
        print(category, ":", total)

while True:
    print("\n--- PERSONAL EXPENSE TRACKER ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter Expenses")
    print("4. Category Summary")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        filter_expenses()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
      
