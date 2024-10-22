# Define the Expense class
class Expense:
    def __init__(self, amount, category, description=""):
        self.amount = amount
        self.category = category
        self.description = description

    def __str__(self):
        return f"{self.category}: {self.amount} - {self.description}"

# Define the ExpenseTracker class
class ExpenseTracker:
    
    def __init__(self):
        # List to store all expenses
        self.expenses = []

    # Function to add an expense
    def add_expense(self, amount, category, description=""):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        print(f"Added: {expense}")

    # Function to remove an expense
    def remove_expense(self, index):
        if 0 <= index < len(self.expenses):
            removed_expense = self.expenses.pop(index)
            print(f"Removed: {removed_expense}")
        else:
            print("Invalid index. Unable to remove expense.")

    # Function to view all expenses
    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("List of Expenses:")
            for i, expense in enumerate(self.expenses):
                print(f"{i}. {expense}")

    # Function to calculate the total expenses
    def total_expenses(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: {total}")
        return total

# Define the main function
def main():
    # Create an instance of ExpenseTracker
    tracker = ExpenseTracker()

    # Display options for the user
    while True:
        print("\nExpense Tracker Options:")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. View Expenses")
        print("4. View Total Expenses")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description (optional): ")
            tracker.add_expense(amount, category, description)

        elif choice == '2':
            tracker.view_expenses()  # Show the list first
            index = int(input("Enter the index of the expense to remove: "))
            tracker.remove_expense(index)

        elif choice == '3':
            tracker.view_expenses()

        elif choice == '4':
            tracker.total_expenses()

        elif choice == '5':
            print("Exiting the Expense Tracker.")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
