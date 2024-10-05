pet_1 = {
    'kind': 'dog',
    'owner': 'Betty',
    'name': 'Bobby'
}

pet_2 = {
    'kind': 'cat',
    'owner': 'Icespice',
    'name': 'Cinnamon'
}

pet_3 = {
    'kind': 'parrot',
    'owner': 'Kanye',
    'name': 'Polly'
}

pet_4 = {
    'kind': 'hamster',
    'owner': 'David',
    'name': 'Sticks'
}

#list of pets
pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"Pet Name: {pet['name']}")
    print(f"Kind of Animal: {pet['kind']}")
    print(f"Owner: {pet['owner']}")
    print()  # For spacing