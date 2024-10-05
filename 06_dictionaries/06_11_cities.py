cities = {
    'Cairo': {
        'country': 'Egypt',
        'population': 9735000,
        'fact': 'Cairo is known as "The City of a Thousand Minarets" due to its historic mosques.'
    },
    'Moscow': {
        'country': 'Russia',
        'population': 11920000,
        'fact': 'Moscow is home to the famous Red Square and the Kremlin.'
    },
    'Bangkok': {
        'country': 'Thailand',
        'population': 10530000,
        'fact': 'Bangkok is known for its vibrant street life and cultural landmarks like the Grand Palace.'
    }
}

# Loop through the dictionary and print each city and its information
for city, info in cities.items():
    print(f"City: {city}")
    print(f" - Country: {info['country']}")
    print(f" - Population: {info['population']}")
    print(f" - Fact: {info['fact']}")
    print()  