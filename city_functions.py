def city_country(city, country, population=None):
    """Return a neatly formatted city and country, with an optional population."""
    result = f"{city.title()}, {country.title()}"
    if population:
        result += f" – population {population}"
    return result
