def describe_city(city, country='united  states'):
    """Describe a city."""
    msg = f"{city.title()} is in {country.title()}."
    print(msg)

describe_city('new york')
describe_city('lima', 'peru')
describe_city('dallas')