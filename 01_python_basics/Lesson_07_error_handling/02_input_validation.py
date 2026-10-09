

def get_int(prompt):
    while True:
        text = input(prompt)
        try:
            return int(text)
        except ValueError:
            print("Please enter aa valid whole number")

def get_positive_float(prompt):
    while True:
        text = input(prompt)
        try:
            value = float(text)
            if value <= 0:
                print("Value must be greater than zero.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    age = get_int("Enter your age: ")
    budget = get_positive_float("Enter your budget: ")

    print(
        f"\nSummary:\n"
        f"Age: {age}\n"
        f"Budget: {budget:,.2f}\n"
    )

if __name__ == "__main__":
    main()

