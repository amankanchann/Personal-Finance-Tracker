from visualisation import plot_expense_pie_chart
from transaction_manager import load_transactions


import tkinter as tk
from income_expense_ui import run_income_expense_ui

if __name__ == "__main__":
    root = tk.Tk()
    run_income_expense_ui(root)
    root.mainloop()
