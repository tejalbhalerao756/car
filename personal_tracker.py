import csv
from datetime import datetime

FILENAME = "expenses.csv"

def init_file():
    try:
        with open(FILENAME, "x", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    except FileExistsError:
        pass

def add_expense():
    date = datetime.now().strftime("%Y-%m-%d")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

    print("✅ Expense added successfully!")

def view_expenses():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)
            next(reader)
            print("\nDate | Category | Amount | Description")
            print("-" * 40)
            for row in reader:
                print(" | ".join(row))
    except FileNotFoundError:
        print("No expenses found.")

def total_expenses():
    total = 0
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[2])
    print(f"\n💰 Total Expenses: ₹{total}")

def category_wise():
    category = input("Enter category to filter: ")
    found = False

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1].lower() == category.lower():
                print(" | ".join(row))
                found = True

    if not found:
        print("No expenses found in this category.")

def menu():
    init_file()
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses")
        print("4. Category-wise Expenses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            category_wise()
        elif choice == "5":
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid choice")

menu()
