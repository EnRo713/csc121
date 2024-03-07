class User:
    """A class to represent a user profile."""

    def __init__(self, first_name, last_name, age, email):
        """Initialize the user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Welcome back, {self.first_name}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

# Create an instance representing a user
user = User('Rich', 'Rodriguez', 37, 'rich@example.com')

# Call increment_login_attempts() several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the value of login_attempts
print(f"Login attempts: {user.login_attempts}")

# Call reset_login_attempts()
user.reset_login_attempts()

# Print login_attempts again to verify it was reset to 0
print(f"Login attempts after reset: {user.login_attempts}")
