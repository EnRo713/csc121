class User:
    """A class to represent a user profile."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Welcome back, {self.first_name}!")

# Create instances representing different users
user1 = User('Rich', 'Rodriguez', 37, 'rich@example.com')
user2 = User('Alice', 'Smith', 46, 'alice@example.com')
user3 = User('Emily', 'Palmer', 22, 'emily@example.com')

# Call both methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()
