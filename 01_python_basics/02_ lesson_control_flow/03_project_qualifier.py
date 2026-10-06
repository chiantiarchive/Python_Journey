

client_name = input("Client name: ")
client_budget = int(input("Client budget in pesos: "))

minimum_project_price = 5_000

if client_budget > 10_000 :
    print(f"{client_name}, You can get the Premium automation package available.")
elif client_budget >= 5_000:
    print(f"{client_name}, You can afford the Standard automation package available.")
else:
    budget_gap = minimum_project_price - client_budget
    
    print(
        f"\nThanks, {client_name}.\n"
        "This client's budget is below the minimum project price.\n"
        f"They need {budget_gap} more to meet the minimum budget.\n"
        )

