# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 14:29:54 2024

@author: swagatika panigrahi
"""

#import the required module 
import csv
from datetime import datetime

expenses = []
monthly_budget = 0

#Add new expense 
def add_expense():
    current_year = datetime.now().year
    current_month = datetime.now().month
    date = input("Enter date (YYYY-MM-DD): ")
    try:
        parsed_date = datetime.strptime(date,"%Y-%m- %d")
    except ValueError:
        # handling if the user entered a date without leading zeros
        try:
            parsed_date = datetime.strptime(date, "%Y-%m-%d").replace(day=int(date.split('-')[2]), month=int(date.split('-')[1]))
            if parsed_date.year != current_year or parsed_date.month != current_month:
                print("Error: Date must be from the current month.")
                return
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD format.")
            return

    date = parsed_date.strftime("%Y-%m-%d")
    category = input("Enter category (Example- Food or Travel): ").title()
    try:
        amount = float(input("Enter the amount spent: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    description = input("Enter a brief description: ")

    expense = {
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
        }
    expenses.append(expense)
    print("Expense added successfully.")
    
 #view expenses   
def view_expenses():
    if not expenses:
        print("No expenses recorded.")
        return

    print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<20}")
    print("-" * 60)

    for expense in expenses:
        if not all(key in expense and expense[key] for key in ['date', 'category', 'amount', 'description']):
            print("Incomplete entry detected, skipping.")
            continue
        
        print(f"{expense['date']:<12} {expense['category']:<15} {expense['amount']:<10.2f} {expense['description']:<20}")
        
        
        
        
# Function to set monthly budget
def set_budget():
    global monthly_budget
    try:
        monthly_budget = float(input("Enter your monthly budget: "))
        print(f"Monthly budget set to {monthly_budget}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        
        


#Function to track budget
def track_budget():
    total_expenses = sum(expense['amount'] for expense in expenses)
    remaining_budget = monthly_budget - total_expenses

    if total_expenses > monthly_budget:
        print("Warning: You have exceeded your budget!")
    else:
        print(f"You have {remaining_budget:.2f} left for the month.")


#save expenses 
def save_expenses():
    with open('expenses.csv', 'w', newline='') as file:
        fieldnames = ['date', 'category', 'amount', 'description']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for expense in expenses:
            writer.writerow(expense)
    print("Expenses saved successfully.")
    
    
#load expenses from the csv file 
def load_expenses():    
    try:
        with open('expenses.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    'date': row['date'],
                    'category': row['category'],
                    'amount': float(row['amount']),
                    'description': row['description']
                })
        print("Expenses loaded successfully.")
    except FileNotFoundError:
        print("No previous expenses found. Starting fresh.")
        
        
#display menu
def display_menu():
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Track Budget")
    print("4. Save Expenses")
    print("5. Exit")


def main():
    load_expenses()

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            if monthly_budget == 0:
                set_budget()
            track_budget()
        elif choice == '4':
            save_expenses()
        elif choice == '5':
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()

