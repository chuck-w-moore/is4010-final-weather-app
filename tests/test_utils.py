import pytest
from src.utils import validate_coordinates, format_forecast_table, get_lat_lon_from_city

# --- Existing Tests ---

def test_validate_coordinates_valid():
    """Test that US coordinates return True."""
    # Cincinnati
    assert validate_coordinates(39.1031, -84.5120) is True

def test_validate_coordinates_invalid():
    """Test that coordinates outside US return False."""
    # London, UK (Outside US)
    assert validate_coordinates(51.5074, -0.1278) is False
    # Zero/Zero
    assert validate_coordinates(0, 0) is False

def test_format_forecast_table_structure():
    """Test that the table formatter processes data correctly."""
    mock_data = [
        {
            "name": "Today",
            "temperature": 70,
            "temperatureUnit": "F",
            "windSpeed": "5 mph",
            "windDirection": "N",
            "shortForecast": "Sunny"
        },
        {
            "name": "Tonight",
            "temperature": 50,
            "temperatureUnit": "F",
            "windSpeed": "10 mph",
            "windDirection": "N",
            "shortForecast": "Clear"
        }
    ]
    
    # Requesting 1 day (should include both periods above)
    result = format_forecast_table(mock_data, days=1)
    
    assert "Today" in result
    assert "70 F" in result
    assert "Sunny" in result
    assert "Period" in result  # Header check

# --- New Tests for Geocoding ---

def test_get_lat_lon_from_city_success(mocker):
    """Test that we can successfully parse a city API response."""
    # Mock the OpenStreetMap API call
    mock_get = mocker.patch('src.utils.requests.get')
    
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    # The API returns a list of matches. We simulate one match.
    mock_response.json.return_value = [{
        'lat': '25.7742',
        'lon': '-80.1936',
        'display_name': 'Miami, Florida'
    }]
    mock_get.return_value = mock_response

    # Call the function
    lat, lon, name = get_lat_lon_from_city("Miami, FL")

    # Assert correct conversion to float and string extraction
    assert lat == 25.7742
    assert lon == -80.1936
    assert name == "Miami, Florida"

def test_get_lat_lon_from_city_not_found(mocker):
    """Test handling when a city is not found."""
    mock_get = mocker.patch('src.utils.requests.get')
    
    mock_response = mocker.MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = [] # Empty list = no results found
    mock_get.return_value = mock_response

    lat, lon, name = get_lat_lon_from_city("Imaginary City")

    assert lat is None
    assert lon is None
    assert name is None