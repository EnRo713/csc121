try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    result = num1 + num2
    print("The result of adding", num1, "and", num2, "is:", result)
except ValueError:
    print("Error: Please enter numerical values only.")
