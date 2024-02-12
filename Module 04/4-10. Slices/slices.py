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
    print("Dear", guest + ",\nI would like to invite you to dinner. Please join me for an evening of good food and conversation.\nSincerely,\nRich Rodriguez")

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
