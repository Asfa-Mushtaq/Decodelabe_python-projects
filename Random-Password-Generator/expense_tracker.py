print("===================================")
print("      Expense Tracker")
print("===================================")

total = 0

while True:
    expense = input("Enter expense amount (or type 'done' to finish): ")

    if expense.lower() == "done":
        break

    try:
        total += float(expense)
    except ValueError:
        print("Please enter a valid number!")

print("\n========== Result ==========")
print(f"Total Spent: Rs. {total:.2f}")
print("============================")