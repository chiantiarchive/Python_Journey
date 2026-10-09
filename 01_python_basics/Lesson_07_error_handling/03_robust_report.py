

from pathlib import Path

def generate_client_report(clients, output_path):
    lines = []
    lines.append("Clients Report")
    lines.append("=" * 40)

    total_budget = 0
    paid_count = 0
    skipped_count = 0

    for i, client in enumerate(clients, start=1):
        try:
            name = client["name"]
            budget = client["budget"]
            has_paid = client["has_paid"]

            try:
                budget = float(budget)
            except (ValueError, TypeError):
                print(f"Warning: Client #{i} has invalid budget; skipping.")
                skipped_count += 1
                continue

            paid_status = "Paid" if has_paid else "Not paid"

            lines.append(f"{name} - Budget: {budget:,.2f} - {paid_status}")

            total_budget += budget
            if has_paid:
                paid_count += 1

        except KeyError as e:
            print(f"Warning: Client #{i} is missing required filed {e}; skipping")

            skipped_count += 1
            continue

    lines.append("=" * 40)
    lines.append(f"Total clients processed: {len(clients) - skipped_count}")
    lines.append(f"Skipped clients: {skipped_count}")
    lines.append(f"Total budget: {total_budget:,.2f}")
    lines.append(f"Clients paid: {paid_count}")

    report_text = "\n".join(lines) + "\n"

    try:
        output_path.parent.mkdir(exist_ok=True)
        output_path.write_text(report_text, encoding="utf-8")
        print(f"Report written to: {output_path}")
    except OSError as e:
        print(f"Error writing report: {e}")


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
            "name": "BadClient",
            "budget": "not-a-number",
            "has_paid": False,
        },
        {
            "name": "MissingBudget",
            "has_paid": True,
        },
        {
            "name": "Chivara",
            "budget": 10_000,
            "has_paid": False,
        },
    ]

    base_dir = Path(__file__).parent
    output_path = base_dir / "output" / "robust_client_report.txt"

    generate_client_report(clients, output_path)

if __name__ == "__main__":
    main()

