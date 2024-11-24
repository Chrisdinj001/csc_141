
from city_functions import city_country

def test_city_country():
    """Test that city_country() returns the correct format without population."""
    result = city_country('santiago', 'chile')
    expected = 'Santiago, Chile'  # Expected output without population
    assert result == expected

def test_city_country_population():
    """Test that city_country() returns the correct format with population."""
    result = city_country('tokyo', 'japan', population=37000000)
    expected = 'Tokyo, Japan – population 37000000'  # Expected output with population

    assert result == expected
    