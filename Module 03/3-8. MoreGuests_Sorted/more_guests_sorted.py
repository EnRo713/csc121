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
