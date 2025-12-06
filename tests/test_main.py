import pytest
import requests  # <--- Make sure this is imported!
from unittest.mock import MagicMock
from src.utils import get_forecast_url

def test_get_forecast_url_success(mocker):
    """Test successfully extracting the forecast URL from the API response."""
    mock_get = mocker.patch('src.utils.requests.get')

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "properties": {
            "forecast": "https://api.weather.gov/gridpoints/ILN/123,456/forecast"
        }
    }
    mock_get.return_value = mock_response

    result = get_forecast_url(39.1031, -84.5120)

    assert result == "https://api.weather.gov/gridpoints/ILN/123,456/forecast"
    mock_get.assert_called_once()

def test_get_forecast_url_failure(mocker):
    """Test handling of a failed API call (e.g., 404 or connection error)."""
    # 1. Mock requests.get
    mock_get = mocker.patch('src.utils.requests.get')

    # 2. Configure the mock
    mock_response = MagicMock()
    mock_response.status_code = 404
    
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Client Error")
    
    mock_get.return_value = mock_response

    # 3. Call the function
    result = get_forecast_url(0, 0)

    # 4. Assertions
    # The code should catch the error and return None (not crash)
    assert result is None