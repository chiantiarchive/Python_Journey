

clients = [
    "Chianti",
    "Serene",
    "Primus"
]

for client in clients:
    print(
        f"Sending reminder to: {client}"
    )


#
#
#


clients = [
    "Chianti",
    "Serene",
    "Primus"
]


for i in range(len(clients)):
    print(
        f"Client {i}: {clients[i]}"
    )


#
#
#


clients = [
    ["Chianti", 3_500, True],
    ["Serene", 5_000, False],
    ["Primus", 4_200, True],
]

for client in clients:
    name = client[0]
    price = client[1]
    paid = client[2]

    print(
        f"{name} - {price} - Paid: {paid}"
    )





