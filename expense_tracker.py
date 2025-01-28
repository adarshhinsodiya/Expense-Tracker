import csv
import os
from datetime import datetime
import pandas as pd  # Importing pandas for table display

# Constants for file storage
FILENAME = 'expenses.csv'

# Function to initialize the CSV file
def initialize_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Amount', 'Description'])

# Function to add a new expense
def add_expense():
    date = datetime.now().strftime('%d-%m-%Y')
    category = input("Enter the category of the expense: ").strip()
    try:
        amount = float(input("Enter the amount: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return
    description = input("Enter a description (optional): ").strip()

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("Expense added successfully!")
    


# Function to calculate the total expenses
def calculate_total():
    total = 0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            total += float(row[2])  # Amount is in the third column
    
    print(f"Total expenses: {total}")

# Function to filter expenses by category
def filter_by_category():
    category_filter = input("Enter the category to filter by: ").strip()

    # Load the CSV data using pandas
    df = pd.read_csv(FILENAME)

    # Filter the DataFrame based on the user input category
    filtered_df = df[df['Category'].str.lower() == category_filter.lower()]

    # Check if there are any records matching the filter
    if filtered_df.empty:
        print(f"No expenses found for category: {category_filter}")
        return

    # Display the filtered DataFrame as a table
    print(f"Expenses for category: {category_filter}")
    print(filtered_df.to_string(index=False))  # Display without the index column

    # Calculate the total expenses for that category
    total = filtered_df['Amount'].sum()
    print(f"Total expenses in {category_filter}: {total:.2f}")

# Function to display CSV file as a table
def display_table():
    if not os.path.exists(FILENAME):
        print("No expenses found!")
        return

    df = pd.read_csv(FILENAME)
    if df.empty:
        print("No data to display.")
    else:
        print(df.to_string(index=False))  # Display the CSV content in a table format

# Function to view all expenses (using pandas for better display)
def view_expenses():
    print("Showing expenses in table format:")
    display_table()

# Main function to display the menu and handle user choices
def menu():
    initialize_file()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Filter expenses by category")
        print("4. Calculate total expenses")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            filter_by_category()
        elif choice == '4':
            calculate_total()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    menu()
