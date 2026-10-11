

import csv
from pathlib import Path

def load_clients(input_path):
    clients = []

    with input_path.open("r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                name = row["name"].strip()
                budget = float(row["budget"])
                has_paid = row["has_paid"].strip().lower() == "true"

                if not name:
                    print("Skipping a row with empty name.")
                    continue

                clients.append({
                    "name": name,
                    "budget": budget,
                    "has_paid": has_paid,
                })
            except (KeyError, ValueError) as error:
                print(f"Skipping invalid row {row}: {error}")

        return clients

def write_clients(output_path, clients):
    fieldnames = ["name", "budget", "has_paid"]

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(clients)

def main():
    base_dir = Path(__file__).parent
    input_path = base_dir / "input" / "clients.csv"
    output_path = base_dir / "output" / "processed_clients.csv"

    clients = load_clients(input_path)

    if not clients:
        print("No valid client record to process")
        return

    total_budget = sum(client["budget"] for client in clients)
    paid_count = sum(client["has_paid"] for client in clients)

    write_clients(output_path, clients)

    msg_client = (
        f"\nClients processed: {len(clients)}\n"
        f"Total budget: {total_budget:,.2f}\n"
        f"Clients paid: {paid_count}\n"
        f"Saved CSV: {output_path}\n"
    )

    print(msg_client)

if __name__ == "__main__":
    main()