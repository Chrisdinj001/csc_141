class Restaurant():
    """A class representing a restaurant."""

    def __init__(self, name, cuisine_type):
        """Initialize the restaurant."""
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Display a summary of the restaurant."""
        msg = f"{self.name} serves wonderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Display a message that the restaurant is open."""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

restaurant = Restaurant('the circle', 'pizza')
print(restaurant.name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()

talkin_tacos = Restaurant("talkin tacos", 'mexican food')
talkin_tacos.describe_restaurant()

krusty_krab = Restaurant('krusty krab', 'burgers')
krusty_krab.describe_restaurant()