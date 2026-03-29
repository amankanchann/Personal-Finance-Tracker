import json
import os

TRANSACTION_FILE = "transactions.json"

def load_transactions():
    """Loads transactions from the JSON file."""
    try:
        if os.path.exists(TRANSACTION_FILE):
            with open(TRANSACTION_FILE, "r") as file:
                return json.load(file)
        return []
    except (json.JSONDecodeError, IOError):
        print("⚠️ Error: Unable to read transactions.json")
        return []

def save_transactions(transactions):
    """Saves transactions to the JSON file."""
    try:
        with open(TRANSACTION_FILE, "w") as file:
            json.dump(transactions, file, indent=4)
    except IOError:
        print("⚠️ Error: Unable to save transactions.")

def add_transaction(date, amount, category, description):
    """Adds a new transaction."""
    if not date or not category or not description:
        raise ValueError("Date, Category, and Description cannot be empty.")
    
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
    except ValueError:
        raise ValueError("Amount must be a valid number.")

    transactions = load_transactions()
    transactions.append({
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    })
    
    save_transactions(transactions)
