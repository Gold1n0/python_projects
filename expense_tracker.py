"""
Simple Expense Tracker
A small CLI app to practice: variables, functions, dicts/lists,
loops, file I/O, error handling, and basic OOP.
"""

import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"


# ---------- OOP: a class to represent one expense ----------
class Expense:
    def __init__(self, amount, category, note=""):
        self.amount = amount
        self.category = category
        self.note = note
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "note": self.note,
            "date": self.date,
        }

    def __str__(self):
        return f"[{self.date}] {self.category:<12} ${self.amount:>8.2f}  {self.note}"


# ---------- File I/O: load/save with error handling ----------
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_expenses(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=2)


# ---------- Core functions ----------
def add_expense(expenses):
    try:
        amount = float(input("Amount: $"))
        category = input("Category (food, rent, fun, etc.): ").strip().lower()
        note = input("Note (optional): ").strip()
    except ValueError:
        print("⚠️  Please enter a valid number for amount.\n")
        return

    expense = Expense(amount, category, note)
    expenses.append(expense.to_dict())
    save_expenses(expenses)
    print(f"✅ Added: {expense}\n")

def delete_expense(expenses):
    if not expenses:
        print("No expenses to delete.\n")
        return

    print("\n--- All Expenses ---")
    for idx, e in enumerate(expenses, start=1):
        exp = Expense(e["amount"], e["category"], e["note"])
        exp.date = e["date"]
        print(f"{idx}. {exp}")

    try:
        choice = int(input("Enter the number of the expense to delete (0 to cancel): "))
        if choice == 0:
            print("Deletion canceled.\n")
            return
        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses(expenses)
            print(f"✅ Deleted: {Expense(removed['amount'], removed['category'], removed['note'])}\n")
        else:
            print("⚠️  Invalid choice.\n")
    except ValueError:
        print("⚠️  Please enter a valid number.\n")



def view_expenses(expenses):
    if not expenses:
        print("No expenses yet.\n")
        return
    print("\n--- All Expenses ---")
    for e in expenses:
        exp = Expense(e["amount"], e["category"], e["note"])
        exp.date = e["date"]  # keep original timestamp
        print(exp)
    print()


def summary_by_category(expenses):
    if not expenses:
        print("No expenses yet.\n")
        return

    # dict comprehension + loop to total by category
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]

    print("\n--- Summary by Category ---")
    for category, total in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"{category:<12} ${total:>8.2f}")

    grand_total = sum(totals.values())
    print(f"{'TOTAL':<12} ${grand_total:>8.2f}\n")


# ---------- Main loop ----------
def main():
    expenses = load_expenses()

    menu = """
=== Expense Tracker ===
1. Add expense
2. View all expenses
3. Summary by category
4. Quit
5. Delete an expense
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            summary_by_category(expenses)
        elif choice == "4":
            delete_expense(expenses)
        elif choice == "5":
            print("Goodbye! 👋")
            break
            
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()