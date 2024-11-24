class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email, pronouns):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.pronouns = pronouns.title()
        self.login_attempts = 0

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.pronouns}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0

shawn = User('shawn', 'graves', 's_graves', 's_graves@example.com', 'he/him')
shawn.describe_user()
shawn.greet_user()

print("\nMaking 3 login attempts...")
shawn.increment_login_attempts()
shawn.increment_login_attempts()
shawn.increment_login_attempts()
print(f"  Login attempts: {shawn.login_attempts}")

print("Resetting login attempts...")
shawn.reset_login_attempts()
print(f"  Login attempts: {shawn.login_attempts}")