import csv
import os
from datetime import datetime

# Configuration
FILENAME = "expenses.csv"

def initialize_system():
    """Checks if the database exists; if not, creates it with headers."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Headers are essential for DictReader to work
            writer.writerow(["Date", "Category", "Description", "Amount"])
        print("[SYSTEM] New database initialized.")

def log_expense():
    """Collects user input and appends it to the CSV file."""
    print("\n--- Log New Expense ---")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    category = input("Enter Category (e.g., Food, Travel, Education): ")
    description = input("Enter Description: ")
    
    try:
        amount = float(input("Enter Amount (INR): "))
        with open(FILENAME, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, description, amount])
        print("[SUCCESS] Expense recorded successfully.")
    except ValueError:
        print("[ERROR] Invalid amount. Please enter a numeric value.")

def generate_report():
    """Reads the CSV file and calculates total spending."""
    if not os.path.exists(FILENAME):
        print("[ERROR] No data found. Log an expense first.")
        return

    total = 0.0
    print("\n--- Spending Report ---")
    print(f"{'Date':<20} | {'Category':<15} | {'Amount':<10}")
    print("-" * 50)
    
    with open(FILENAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"{row['Date']:<20} | {row['Category']:<15} | {row['Amount']:<10}")
            total += float(row['Amount'])
            
    print("-" * 50)
    print(f"TOTAL EXPENDITURE: {total:.2f} INR")

def main():
    initialize_system()
    while True:
        print("\n=== SMARTSPEND: PERSONAL FINANCE TRACKER ===")
        print("1. Log Expense")
        print("2. Generate Report")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            log_expense()
        elif choice == '2':
            generate_report()
        elif choice == '3':
            print("Exiting SmartSpend. Goodbye!")
            break
        else:
            print("[ERROR] Invalid selection. Try again.")

if __name__ == "__main__":
    main()