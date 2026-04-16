def calculate_total_cost(cart):
    total_cost = 0
    for item in cart: 
        total_cost +=item["price"] * item["quantity"]

    return total_cost

## example cart data

cart = [
     {"name": "Laptop", "price": 999.99, "quantity": 1},
     {"name": "Mouse", "price": 25.50, "quantity": 2},
     {"name": "Keyboard", "price": 45.00, "quantity": 1}
]

## calling the function
total_cost = calculate_total_cost(cart)
print(f"Total Cost: ${total_cost:.2f}")