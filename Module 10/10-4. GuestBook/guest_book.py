filename = 'guest_book.txt'

print("Welcome to the Guest Book!")
print("Enter 'quit' when you're finished.")

while True:
    name = input("\nEnter your name: ")
    if name.lower() == 'quit':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write(name + "\n")
        print(f"Hello, {name}! You've been added to the guest book.")
