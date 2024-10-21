class Game:
    def __init__(self):
        self.rooms = {
            'entrance': Room(
                "You are at the entrance of the zoo. You can see paths leading to the lion enclosure, the monkey house, and the bird aviary.",
                {'north': 'lion_enclosure', 'east': 'monkey_house', 'south': 'bird_aviary'}
            ),
            'lion_enclosure': Room(
                "You are in the lion enclosure. The lions are resting under a tree. They look well-fed.",
                {'south': 'entrance'},
                items=['meat']
            ),
            'monkey_house': Room(
                "You are in the monkey house. The monkeys are swinging around and playing. They love bananas.",
                {'west': 'entrance'},
                items=['banana']
            ),
            'bird_aviary': Room(
                "You are in the bird aviary. Colorful birds are flying around, and they seem curious.",
                {'north': 'entrance'},
                items=['seeds']
            ),
        }
        self.current_room = self.rooms['entrance']
        self.inventory = []
        self.is_running = True

    def play(self):
        print("Welcome to the Zookeeper Adventure!")
        while self.is_running:
            print("\n" + self.current_room.description)
            if self.current_room.items:
                print("You see: " + ", ".join(self.current_room.items))
            else:
                print("There's nothing here.")
            command = input("What do you want to do? ").lower()
            self.process_command(command)

    def process_command(self, command):
        if command in ['exit', 'quit']:
            self.is_running = False
            print("Thanks for visiting the zoo! Goodbye!")
        elif command in self.current_room.connections:
            self.current_room = self.rooms[self.current_room.connections[command]]
            print(f"You move to: {self.current_room.description}")
        elif command.startswith("take "):
            item = command.split("take ")[-1]
            if item in self.current_room.items:
                self.inventory.append(item)
                self.current_room.items.remove(item)
                print(f"You took the {item}.")
            else:
                print("There's no such item here.")
        elif command.startswith("feed "):
            animal = command.split("feed ")[-1]
            if animal == "lion" and 'meat' in self.inventory:
                print("You fed the lions! They roar thank you!")
            elif animal == "monkey" and 'banana' in self.inventory:
                print("You fed the monkeys! Ooh-ooh Ahh-ahh!")
            elif animal == "bird" and 'seeds' in self.inventory:
                print("You fed the birds! They chirp you a song!")
            else:
                print("You need the correct food to feed that animal.")
        elif command.startswith("pet "):
            animal = command.split("pet ")[-1]
            if animal == "lion":
                print("You cautiously pet the lion. It purrs softly!")
            elif animal == "monkey":
                print("You pet the monkey. It grasps on to your finger!")
            elif animal == "bird":
                print("You gently pet the bird. It chirps and flutters its wings!")
            else:
                print("You can't pet that animal.")
        else:
            print("You can't do that.")

class Room:
    def __init__(self, description, connections, items=[]):
        self.description = description
        self.connections = connections
        self.items = items

if __name__ == "__main__":
    game = Game()
    game.play()