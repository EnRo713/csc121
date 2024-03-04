# Initialize the list of sandwich orders
sandwich_orders = ["Turkey", "Ham and Cheese", "BLT", "Grilled Cheese", "Tuna"]

# Initialize the list of finished sandwiches
finished_sandwiches = []

# Loop through each sandwich order
while sandwich_orders:
    # Make the sandwich and move it to the list of finished sandwiches
    current_sandwich = sandwich_orders.pop(0)
    print("I made your", current_sandwich, "sandwich.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
print("\nList of finished sandwiches:")
for sandwich in finished_sandwiches:
    print("- " + sandwich)
