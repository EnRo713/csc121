# Define a dictionary of rivers and the countries they run through
rivers = {
    'magdalena': 'colombia',
    'cagayan': 'philippines',
    'amazon': 'brazil',
}

# Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Print the name of each river
print("\nRivers:")
for river in rivers.keys():
    print(river.title())

# Print the name of each country
print("\nCountries:")
for country in rivers.values():
    print(country.title())
