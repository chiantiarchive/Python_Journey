

client = {
    "name": "Serene",
    "age": 20,
    "has_paid": False,
    "budget": 7_000,
}


print(client["name"])      # "Serene"
print(client["budget"])    # 7000


print(f"{client["name"]} has a budget of ₱{client["budget"]}.")

