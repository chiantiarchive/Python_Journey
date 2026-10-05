

def calculate_total_income(client_count, price_per_project):
    calculate_total_income = client_count * price_per_project

    return calculate_total_income

income = calculate_total_income(3, 4_500)

print(f"Total income: {income}")

