import random

# List containing numbers and letters
lottery_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select four numbers and one letter
lottery_numbers = random.sample(lottery_choices[:10], 4)
lottery_letter = random.choice(lottery_choices[10:])

# Combine numbers and letter to form the lottery number
lottery_ticket = lottery_numbers + [lottery_letter]

# Get input from the user for their lottery number
user_numbers = []
for i in range(4):
    user_input = int(input(f"Enter number {i+1} (1-10): "))
    user_numbers.append(user_input)
user_letter = input("Enter a letter (A-E): ").upper()

# Compare the user's input to the lottery number
if user_numbers == lottery_numbers and user_letter == lottery_letter:
    print("Congratulations! You're the winner!")
else:
    print("Sorry, better luck next time!")
    print(f"The winning numbers are: {lottery_numbers}")
    print(f"The winning letter is: {lottery_letter}")
