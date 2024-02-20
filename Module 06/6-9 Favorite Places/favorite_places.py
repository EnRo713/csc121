# Define the dictionary of favorite places
favorite_places = {
    'Ana': ['Medellín, Colombia', 'Asheville, NC'],
    'Rich': ['Concepcion, Philippines', 'Puerta Vallarta, Mexico'],
    'Carmen': ['Fiji', 'Rio de Janeiro, Brazil', 'Bali, Indonesia']
}

# Loop through dictionary, print each person's name and favorite places
for person, places in favorite_places.items():
    print(person + "'s favorite places are:")
    for place in places:
        print("• " + place)
    print()  # Print empty line for readability
