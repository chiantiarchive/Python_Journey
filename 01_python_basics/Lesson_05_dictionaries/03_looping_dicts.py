

client = {
    "name": "Serene",
    "age": 20,
    "has_paid": False,
    "budget": 7_000,
}


for key in client:
    print(key)

for value in client.values():
    print(value)

for key, value in client.items():
    print(f"{key}: {value}")


#
#
#


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


first_client = clients[0]
print(first_client["name"])  # "Serene"

for client in clients:
    print(f"{client["name"]} - Budget: ₱{client["budget"]}")

for client in clients:
    if not client["has_paid"]:
        print(f"Reminder: {client["name"]} has not paid yet.")

