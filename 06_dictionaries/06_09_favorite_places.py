favorite_places = {
    'Stacy': ['Californa', 'New York', 'Bahamas'],
    'Alyssa': ['Itay', 'Japsn'],
    'Leah': ['Spain', 'Paris', 'Berlin'],
}

# Loop through the dictionary and print each person's name and their favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f" - {place}")
    print() 