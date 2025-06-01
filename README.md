# Expense Tracker CLI

A simple command-line based Expense Tracker built in Python. This tool helps you log your expenses, categorize them, view summaries, and filter your spending—all stored locally in a CSV file for easy access and modification.

## Features

- **Add New Expenses:** Quickly add expenses with category, amount, and description.
- **View All Expenses:** Display all recorded expenses in a clear tabular format.
- **Filter by Category:** See expenses for a specific category and get the total for that category.
- **Calculate Total Expenses:** Instantly calculate the sum of all your recorded expenses.
- **Persistent Storage:** All data is stored in `expenses.csv`—no database required.

## Requirements

- Python 3.x
- [pandas](https://pandas.pydata.org/) library

## Installation

1. **Clone the repository or copy the script.**
2. **Install dependencies:**
   ```bash
   pip install pandas
   ```

## Usage

Run the script in your terminal:
```bash
python expense_tracker.py
```

You will see a menu:
```
Expense Tracker Menu:
1. Add a new expense
2. View all expenses
3. Filter expenses by category
4. Calculate total expenses
5. Exit
```

Choose an option by entering the corresponding number.

### Example

**Adding an Expense:**
```
Enter the category of the expense: Food
Enter the amount: 12.50
Enter a description (optional): Lunch at cafe
Expense added successfully!
```

**Filtering by Category:**
```
Enter the category to filter by: Food
Expenses for category: Food
     Date Category  Amount     Description
01-06-2025    Food   12.50  Lunch at cafe
Total expenses in Food: 12.50
```

## File Structure

- `expense_tracker.py` — The main script.
- `expenses.csv` — Automatically created/updated; stores your expense data.

## Notes

- The CSV file will be created automatically if it does not exist.
- The date is logged automatically based on your system's current date.
- The script is intended for personal use and does not include user authentication.

## License

This project is open source and free to use.

---

*Happy tracking your expenses!*
