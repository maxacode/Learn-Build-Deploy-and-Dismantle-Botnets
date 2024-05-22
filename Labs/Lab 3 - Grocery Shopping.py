b"""
1. Create a list of groceries with an available budget
2. Iterate the list for budget calculation. 
3. Simulate grocery shopping
4. Exit to leave store 
5. Print how many Items of each they have. Ex:
        3 Apples
        2 Lemons
        50 Dollars left

"""

# Define groceries and their prices
groceries = {"Apple": 1, "Lemon": 2, "Bread": 5, "Milk": 3}
budget = 10  # Starting budget

# bShopping loop
shopping_cart = {}  # Dictionary to store items and quantities
while True:
  # Display options
  print("\nWelcome to the Grocery Store!")
  print(f"Budget: ${budget}")
  print("Available Items:")
  for item, price in groceries.items():
    print(f"- {item} (${price})")

  # Get user input
  item_name = input("\nEnter item name (or 'exit' to leave): ").title()

  if item_name.lower() == "exit":
    break  # Exit the loop on 'exit'

  if item_name not in groceries:
    print(f"Sorry, '{item_name}' is not available.")
    continue  # Skip to next iteration

  # Get quantity
  try:
    quantity = int(input(f"How many {item_name}s would you like? "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue

  # Check budget and add to cart
  total_cost = quantity * groceries[item_name]
  if total_cost > budget:
    print(f"Sorry, insufficient funds. That would cost ${total_cost}.")
  else:
    budget = budget - total_cost
    if item_name in shopping_cart:
      shopping_cart[item_name] += quantity
    else:
      shopping_cart[item_name] = quantity
    print(f"Added {quantity} {item_name}(s) to your cart.")

# Print final receipt
print("\nYour Shopping Cart:")
for item, quantity in shopping_cart.items():
  print(f"{quantity} {item}(s)")
print(f"Remaining Budget: ${budget}")
