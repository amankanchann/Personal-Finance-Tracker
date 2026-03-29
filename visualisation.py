import matplotlib.pyplot as plt

def plot_expense_pie_chart(transactions):
    """Creates a pie chart with income (green) and expense (red), including descriptions."""
    
    if not transactions:
        print("No transactions available to display.")
        return

    categories = []
    amounts = []
    colors = []

    for transaction in transactions:
        categories.append(f"{transaction['category']} - {transaction['description']}")
        amounts.append(abs(transaction['amount']))  # Ensure absolute value
        colors.append('green' if transaction['amount'] > 0 else 'red')  # Green for income, Red for expense

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(amounts, labels=categories, autopct='%1.1f%%', colors=colors, startangle=140)

    # Add separator lines for better clarity
    for wedge in wedges:
        wedge.set_edgecolor('black')

    ax.set_title("Income & Expense Breakdown")
    plt.show()
