# Program 1: Animals
# Define a list of animals with a unique common characteristic
animals = ["Platypus", "Echidna", "Spiny anteater"]

# Print the name of each animal using a for loop
print("Animals:")
for animal in animals:
    print(animal)

# Print a statement about each animal
for animal in animals:
    print("The", animal.lower(), "is a monotreme.")

# Print a statement about what these animals have in common
print("All of these animals lay eggs and produce milk.")

# Program 2: Cubes
# Make a list to store the first 10 cubes
cubes = []

# Calculate the cube of each integer from 1 through 10 and add it to the list
for number in range(1, 11):
    cubes.append(number ** 3)

# Print out the value of each cube using a for loop
for cube in cubes:
    print(cube)

# Program 3: Slices
# Define a list of people to invite to dinner
guest_list = [
    "Salvador Dali",
    "Arnold Schwarzenegger",
    "Selena Quintanilla",
    "Bruce Lee",
    "Alan Watts",
    "Michelle Yeoh",
    "Jimi Hendrix"
]

# To inform the guests
print("\nGreat news! We found a bigger dinner table.")

# Add three more guests to the list
guest_list.insert(0, "Princess Diana")  # Add at the beginning
guest_list.insert(len(guest_list) // 2, "Frida Kahlo")  # Add in the middle
guest_list.append("Bob Marley")  # Add at the end

# Sort the list alphabetically
guest_list.sort()

# Print invitation messages for each person in the sorted list
for guest in guest_list:
    print("Dear", guest + ",\nI would like to invite you to dinner. "
        "Please join me for an evening of good food and conversation.\n"
        "Sincerely,\nRich Rodriguez")

# Print the first three items in the list
print("\nThe first three items in the list are:")
print(guest_list[:3])

# Print three items from the middle of the list
print("\nThree items from the middle of the list are:")
middle_index = len(guest_list) // 2
print(guest_list[middle_index - 1:middle_index + 2])

# Print the last three items in the list
print("\nThe last three items in the list are:")
print(guest_list[-3:])
