from city_functions import get_formatted_info


def test_city_country():
    "City name and it's country"
    formatted_info = get_formatted_info('Santiago', 'chile')
    assert formatted_info == "Santiago Chile"
    
def test_city_population_country():
    """City, population and country"""
    formatted_info = get_formatted_info('santiago', 'chile',  population=5000000)
    assert formatted_info == "Santiago 5000000 Chile"

