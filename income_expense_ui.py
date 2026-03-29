import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from transaction_manager import load_transactions, save_transactions

TRANSACTION_FILE = "transactions.json"

def run_income_expense_ui(root):
    """Creates the UI inside the given root window"""
    
    # Main Frame
    frame = tk.Frame(root)
    frame.pack(pady=10)

    # Welcome Label
    tk.Label(frame, text="Welcome to Personal Finance Tracker", font=("Arial", 16)).pack()

    # Matplotlib Pie Chart
    fig, ax = plt.subplots(figsize=(5, 4))
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack()

    def update_chart():
        transactions = load_transactions()
        
        if not transactions:
            ax.clear()
            ax.text(0.5, 0.5, "No Transactions Available", fontsize=12, ha='center', va='center')
            canvas.draw()
            return

        descriptions = []
        amounts = []
        colors = []

        for t in transactions:
            descriptions.append(t["description"])
            amounts.append(t["amount"])
            colors.append("green" if t["category"] == "Income" else "red")

        ax.clear()
        wedges, texts, autotexts = ax.pie(
            amounts, labels=descriptions, autopct="%1.1f%%", colors=colors, wedgeprops={'edgecolor': 'black'}
        )
        
        ax.set_title("Expense & Income Breakdown")

        canvas.draw()

    update_chart()

    # Add Transaction Section
    ttk.Label(frame, text="Add Transaction", font=("Arial", 12, "bold")).pack(pady=5)
    
    ttk.Label(frame, text="Date (YYYY-MM-DD):").pack()
    date_entry = ttk.Entry(frame)
    date_entry.pack()

    ttk.Label(frame, text="Amount:").pack()
    amount_entry = ttk.Entry(frame)
    amount_entry.pack()

    ttk.Label(frame, text="Category:").pack()
    category_var = tk.StringVar()
    category_dropdown = ttk.Combobox(frame, textvariable=category_var, values=["Income", "Expense"])
    category_dropdown.pack()

    ttk.Label(frame, text="Description:").pack()
    description_entry = ttk.Entry(frame)
    description_entry.pack()

    def add_transaction():
        try:
            date = date_entry.get()
            amount = amount_entry.get()
            category = category_var.get()
            description = description_entry.get()

            if not amount.isdigit():
                raise ValueError("Amount must be a number.")

            amount = float(amount)

            if amount <= 0:
                raise ValueError("Amount must be greater than zero.")

            new_transaction = {"date": date, "amount": amount, "category": category, "description": description}

            transactions = load_transactions()
            transactions.append(new_transaction)
            save_transactions(transactions)

            messagebox.showinfo("Success", "Transaction Added Successfully!")
            update_chart()

        except ValueError as ve:
            messagebox.showerror("Error", str(ve))

    ttk.Button(frame, text="➕ Add Transaction", command=add_transaction).pack(pady=5)
