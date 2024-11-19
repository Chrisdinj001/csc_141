class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, username, email,pronouns):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.pronouns =pronouns.title()

    def describe_user(self):
        """Display a summary of the user's information."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Pronouns: {self.pronouns}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"\nWelcome back, {self.username}!")

shawn = User('shawn', 'graves', 's_graves', 's_graves@example.com', 'he/him')
shawn.describe_user()
shawn.greet_user()

lilly = User('lilly', 'lady', 'lillylady', 'lillady@example.com', 'she/her')
lilly.describe_user()
lilly.greet_user()