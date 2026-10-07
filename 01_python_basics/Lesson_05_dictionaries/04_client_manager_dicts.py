

clients = [
    {
        "name": "Serene",
        "age": 18,
        "has_paid": False,
        "budget": 7_000,
    },
    {
        "name": "Chianti",
        "age": 22,
        "has_paid": True,
        "budget": 5_500,
    },
    {
        "name": "Chivara",
        "age": 20,
        "has_paid": False,
        "budget": 3_000,
    },
]


def display_clients(clients):
    if not clients:
        print("No clients in the list.")
        return

    print("\nClient list:")
    for i, client in enumerate(clients, start=1):
        paid_status = "Paid" if client["has_paid"] else "Not paid"
        print(f"{i}. {client["name"]} - Budget: {client["budget"]} - {paid_status}")

def add_client(clients):
    name = input("Enter client name: ").strip()
    if not name:
        print("Client name cannot be empty.")
        return

    budget_text = input("Enter client budget: ").strip()
    try:
        budget = float(budget_text)
    except ValueError:
        print("Invalid budget. Must be a number.")
        return

    client = {
        "name": name,
        "budget": budget,
        "has_paid": False, 
    }

    clients.append(client)
    print(f"Added client: {name}")

def mark_as_paid(clients):
    display_clients(clients)

    if not clients:
        return

    index_text = input("Enter client number to mark as paid: ").strip()
    try:
        index = int(index_text) - 1
    except ValueError:
        print("Invalid number.")
        return

    if 0 <= index < len(clients):
        clients[index]["has_paid"] = True
        print(f"Marked {clients[index]["name"]} as paid.")
    else:
        print("Invalid client number")

def main():
    clients = [
        {
            "name": "Serene",
            "budget": 7_000,
            "has_paid": False,
        },
        {
            "name": "Chianti",
            "budget": 5_500,
            "has_paid": True,
        },
    ]

    while True:
        print(
            "\nClient Manager (with dictionaries)\n",
            "1. Display clients\n",
            "2. Add clients\n",
            "3. Mark client as paid\n",
            "4. Exit\n"
        )
        

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            display_clients(clients)
        elif choice == "2":
            add_client(clients)
        elif choice == "3":
            mark_as_paid(clients)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Choose (1-4).")

if __name__ == "__main__":
    main()

