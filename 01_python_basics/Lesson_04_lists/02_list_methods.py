

clients = ["Chianti", "Serene", "Primus"]

#   Change an item
clients[1] = "Nz"

#   Add an item to the end
clients.append("Bruno")
print(clients)


#
#
#


clients = ["Chianti", "Serene", "Primus"]

clients.insert(1, "Bruno")  # Inset at index 1
print(clients)




#
#
#


clients = ["Chianti", "Serene", "Primus"]

#   Remove by value
clients.remove("Serene")

#   Remove by index
removed_client = clients.pop(1)

#   Remove the last item
last_client = clients.pop()

print(
    "\n",clients, "\n"
    "Removed:", removed_client,"\n"
    "Last removed:", last_client,"\n"
    )


#
#
#


clients = ["Chianti", "Serene", "Primus"]

count = len(clients)
print(f"Total clients: {count}")

