

def display_clients(clients):
    if not clients:
        print("No clients in the list")
        return

    print("Client list: ")

    for i, client in enumerate(clients, start=1):
        print(f"{i}. {client}")

def add_client(clients, new_client):
    clients.append(new_client)
    print(f"Added client: {new_client}")


def remove_client(clients, client_name):
    if client_name in clients:
        clients.remove(client_name)
        print(f"Client '{client_name}' not found!")


def main():
    clients = ["Chianti","Serene","Primus"]

    while True:
        print(
            "\nClient List Manager\n"
            "1. Display clients\n"
            "2. Add client\n"
            "3. Remove client\n"
            "4. Exit\n"
        )

        choice = input("choose an option (1-4): ")

        if choice == "1":
            display_clients(clients)
        elif choice =="2":
            new_client = input("Enter client name: ").strip()

            if new_client:
                add_client(clients, new_client)
            else:
                print("Client name cannot be empty.")

        elif choice == "3":
            client_name = input("Enter client name to remove: ").strip()
            remove_client(clients, client_name)
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Choose (1-4).")

if __name__ == "__main__":
    main()


