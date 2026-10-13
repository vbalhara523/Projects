
import csv
import os
from datetime import date

FILE = "expenses.csv"


def setup():
    if not os.path.exists(FILE):
        with open(FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Date", "Category", "Amount", "Note"])


def add_expense():
    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    try:
        amount = float(input("Enter amount: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
    except ValueError:
        print("Enter a valid amount.")
        return

    note = input("Enter note: ")
    expense_date = date.today().isoformat()

    with open(FILE, "r", newline="") as f:
        rows = list(csv.reader(f))

    expense_id = max(
        (int(row[0]) for row in rows[1:] if row),
        default=0
    ) + 1

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            expense_id, expense_date, category, amount, note
        ])

    print("Expense added successfully!")


def view_expenses():
    with open(FILE, "r", newline="") as f:
        rows = list(csv.reader(f))

    if len(rows) == 1:
        print("No expenses recorded.")
        return

    print("\nID | Date | Category | Amount | Note")
    print("-" * 55)

    for row in rows[1:]:
        print(" | ".join(row))


def total_expenses():
    total = 0

    with open(FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total += float(row["Amount"])

    print(f"Total expenses: Rs. {total:.2f}")


def delete_expense():
    view_expenses()

    try:
        expense_id = int(input("Enter expense ID to delete: "))
    except ValueError:
        print("Enter a valid ID.")
        return

    with open(FILE, "r", newline="") as f:
        rows = list(csv.reader(f))

    updated = [rows[0]]
    found = False

    for row in rows[1:]:
        if row and int(row[0]) == expense_id:
            found = True
        else:
            updated.append(row)

    if found:
        with open(FILE, "w", newline="") as f:
            csv.writer(f).writerows(updated)
        print("Expense deleted successfully!")
    else:
        print("Expense ID not found.")


def main():
    setup()

    while True:
        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Total Spending")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

