# ==============================
#      EXPENSE TRACKER
# ==============================

expenses = []
total = 0

print("===================================")
print("        Expense Tracker")
print("===================================")

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        expense = float(expense)

        if expense < 0:
            print("Expense cannot be negative!")
            continue

        expenses.append(expense)
        total += expense

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount!")

print("\n========== Expense Summary ==========")

if len(expenses) == 0:
    print("No expenses entered.")
else:
    print("\nExpenses:")
    for i, amount in enumerate(expenses, start=1):
        print(f"{i}. Rs. {amount:.2f}")

    average = total / len(expenses)

    print("\n-------------------------------------")
    print(f"Total Expenses      : Rs. {total:.2f}")
    print(f"Number of Expenses  : {len(expenses)}")
    print(f"Average Expense     : Rs. {average:.2f}")

print("=====================================")
print("Thank you for using Expense Tracker!")
print("=====================================")
