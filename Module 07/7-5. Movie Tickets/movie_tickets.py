# Initialize ticket prices
ticket_price_under_3 = 0
ticket_price_3_to_12 = 10
ticket_price_over_12 = 15

# Prompt the user for the number of tickets
num_tickets = int(input("How many tickets do you want to purchase? "))

# Initialize total cost
total_cost = 0

# Loop through each ticket holder
for i in range(num_tickets):
    age = int(input(f"Enter the age of ticket holder {i+1}: "))
    
    # Determine ticket price based on age
    if age < 3:
        ticket_price = ticket_price_under_3
    elif age >= 3 and age <= 12:
        ticket_price = ticket_price_3_to_12
    else:
        ticket_price = ticket_price_over_12
    
    # Add ticket price to total cost
    total_cost += ticket_price

# Display the total cost of tickets
print("The total cost of your movie tickets is:", total_cost)
