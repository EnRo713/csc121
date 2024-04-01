from pathlib import Path

# Define the file path
file_path = Path('guest_book.txt')

# Prompt users for their name
while True:
    name = input("Please enter your name (or 'q' to quit): ")
    if name.lower() == 'q':
        break

    # Print greeting to the screen
    print(f"Welcome, {name}! Your visit has been recorded in the guest book.")

    # Open the file in append mode
    with file_path.open('a') as file:
        file.write(f"{name}\n")
