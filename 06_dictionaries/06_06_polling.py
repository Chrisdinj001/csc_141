favorite_languages = {
    'alice': 'python',
    'bob': 'java',
    'charlie': 'ruby',
}

#list of people who should take the favorite languages poll
people_to_poll = ['alice', 'david', 'sara', 'bob', 'lucy']

#loop through the list of people who should take the poll
for person in people_to_poll:
    if person.lower() in favorite_languages:
        print(f"Thank you, {person.title()}, for responding!")
    else:
        print(f"Hi {person.title()}, please take our favorite languages poll!")
