# Managing an inventory
inventory = ["apples", "bananas", "oranges", "grapes"]

# Adding a new item
inventory.append("strawberries")

# Removing an item that is out of stock
inventory.remove("bananas")

# Checking if an item is in stock
item = "oranges"
if item in inventory:
    print(f"{item} are in stock.")
else:
    print(f"{item} are out of stock.")

# printing the current inventory
print("Current Inventory:")
for item in inventory:
    print(f"- {item}")