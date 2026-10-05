

def calculate_gross_income(client_count, price_per_project):
    return client_count * price_per_project

def calculate_expenses(gross_income, expenses_rate):
    return gross_income * expenses_rate

def calculate_net_income(gross_income, expenses):
    return gross_income - expenses

def calculate_monthly_income(weekly_income):
    return weekly_income * 4


client_count = int(input("Number of clients: "))
price_per_project = float(input("Price per project: "))

expense_rate = 0.10


gross_income = calculate_gross_income(client_count, price_per_project)
expenses = calculate_expenses(gross_income, expense_rate)
net_income = calculate_net_income(gross_income, expenses)
monthly_income = calculate_monthly_income(net_income)

print(
    "\nFreelance income estimate\n"
    f"Client/s: {client_count}\n"
    f"Price per project: {price_per_project:,.2f}\n"
    f"Gross income: {gross_income:,.2f}\n"
    f"Estimated net income: {net_income:,.2f}\n"
    f"Estimated expenses: {expenses:,.2f}\n"
    f"Estimated monthly income: {monthly_income:,.2f}\n"
)

