

from pathlib import Path

def generate_client_report(clients, output_path):
    lines = []
    lines.append("client Report")
    lines.append("=" * 40)

    total_budget = 0
    paid_count = 0

    for client in clients:
        name = client["name"]
        budget = client["budget"]
        has_paid = client["has_paid"]

        paid_status = "Paid" if has_paid else "Not paid"

        lines.append(f"{name} - Budget: {budget:,.2f} - {paid_status}")

        total_budget += budget
        if has_paid:
            paid_count += 1

    lines.append("=" * 40)
    lines.append(f"Total clients: {len(clients)}")
    lines.append(f"Total Budget: {total_budget:,.2f}")
    lines.append(f"Clients paid: {paid_count}")

    report_text = "\n".join(lines) + "\n"

    #   Ensure output folder exists 
    output_path.parent.mkdir(exist_ok=True)

    #   Write report to file
    output_path.write_text(report_text, encoding="utf-8")

    print(f"Report written to: {output_path}")

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
        {
            
            "name": "Chivara",
            "budget": 10_000,
            "has_paid": False,
        },
    ]

    base_dir = Path(__file__).parent
    output_Path = base_dir / "output" / "client_report.txt"

    generate_client_report(clients, output_Path)

if __name__ == "__main__":
    main()