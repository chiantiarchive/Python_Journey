

client = {
    "name": "Serene",
    "age": 20,
    "has_paid": False,
}


#   Add new data
client["budget"] = 7_000


#   Change existing data
client["age"] = 19
client["has_paid"] = True

#   Remove data
del client["age"]

#   Check the data exists
if "budget" in client:
    print("Budget is set.")


