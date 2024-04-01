def add_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Error: Please enter a valid number for the first input.")

    while True:
        try:
            num2 = float(input("Enter the second number: "))
            result = num1 + num2
            print("The result of adding the numbers is:", result)
            break
        except ValueError:
            print("Error: Please enter a valid number for the second input.")

add_numbers()
