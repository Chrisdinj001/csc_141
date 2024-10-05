person_0 = {
    'first_name': 'Liam',
    'last_name': 'John',
    'age': 30,
    'city': 'New York'
}

person_1 = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'age': 24,
    'city':'Baltimore'
    }

person_2 = {
    'first_name': 'Robert',
    'last_name': 'Johnson',
    'age': 25,
    'city': 'Los Angeles'
}

person_3 = {
    'first_name': 'Isabel',
    'last_name': 'Jones',
    'age': 28,
    'city': 'Chicago'
}

#list of people
people = [person_0,person_1, person_2, person_3]

# Loop through the list of people and print their information
for person in people:
    print(f"Name: {person['first_name']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}")
    print()  # For spacing