

has_paid = True
has_unfinished_project = False

print(has_paid)
print(has_unfinished_project)

#
#
#

project_price = 5_000
client_budget = 7_000

print(client_budget > project_price)
print(client_budget == project_price)
print(client_budget < project_price)

#
#
#

client_budget = 7_000
minimum_project_budget = 5_000

if client_budget >= minimum_project_budget:
    print("This client can afford the project")

#
#
#

client_budget = 3_000
minimum_project_budget = 5_000

if client_budget >= minimum_project_budget:
    print("This client can afford the project")
else:
    print("This client's budget is below the minimum project price.")

