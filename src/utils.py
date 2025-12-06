import requests
import sys
from tabulate import tabulate

# Constants for US Geographic bounds (Approximate CONUS box)
LAT_MIN, LAT_MAX = 24.0, 50.0
LON_MIN, LON_MAX = -125.0, -66.0

# USER AGENT for API requests
MY_USER_AGENT = "(IS4010-Weather-App, weatherappdemoproject25@gmail.com)"

HEADERS = {
    "User-Agent": MY_USER_AGENT,
    "Accept": "application/geo+json"
}

def validate_coordinates(lat: float, lon: float) -> bool:
    """Ensures coordinates are roughly within the US mainland."""
    return (LAT_MIN <= lat <= LAT_MAX) and (LON_MIN <= lon <= LON_MAX)

def get_lat_lon_from_city(city_name):
    """
    Uses the OpenStreetMap (Nominatim) API to convert a city name 
    into Latitude and Longitude.
    """
    base_url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": city_name,
        "format": "json",
        "limit": 1,
        "countrycodes": "us"
    }
    
    try:
        # Nominatim is STRICT. We must use a unique User-Agent.
        response = requests.get(base_url, params=params, headers=HEADERS, timeout=10)
        
        # This will print the error code if it fails (e.g., 403 Forbidden)
        if response.status_code != 200:
            print(f"Error: OpenStreetMap API returned status code {response.status_code}")
            return None, None, None

        data = response.json()
        
        if data:
            return float(data[0]['lat']), float(data[0]['lon']), data[0]['display_name']
        else:
            return None, None, None
            
    except requests.exceptions.RequestException as e:
        print(f"Connection Error: {e}")
        return None, None, None

def get_forecast_url(lat: float, lon: float):
    """Step 1 of NWS API: Convert Lat/Lon to a Gridpoint URL."""
    url = f"https://api.weather.gov/points/{lat},{lon}"
    
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['properties']['forecast']
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to NWS Point API: {e}")
        return None
    except KeyError:
        print("Error: Could not find forecast URL. Location might be outside NWS coverage.")
        return None

def get_forecast_data(forecast_url: str):
    """Step 2 of NWS API: Fetch the actual forecast periods."""
    try:
        response = requests.get(forecast_url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data['properties']['periods']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching forecast data: {e}")
        return None

def format_forecast_table(periods: list, days: int) -> str:
    """Formats the raw forecast periods into a readable table."""
    num_periods = days * 2
    sliced_periods = periods[:num_periods]

    table_data = []
    for p in sliced_periods:
        # Truncate at 80 chars to fit standard screens
        limit = 80
        short_desc = (p['shortForecast'][:limit] + '..') if len(p['shortForecast']) > limit else p['shortForecast']
        
        table_data.append([
            p['name'],
            f"{p['temperature']} {p['temperatureUnit']}",
            f"{p['windSpeed']} {p['windDirection']}",
            short_desc
        ])

    headers = ["Period", "Temp", "Wind", "Forecast"]
    return tabulate(table_data, headers=headers, tablefmt="grid")

def print_examples():
    """Prints example coordinates."""
    examples = [
        ["New York City, NY", 40.7128, -74.0060],
        ["Chicago, IL", 41.8781, -87.6298],
        ["Cincinnati, OH", 39.1031, -84.5120],
        ["Dallas, TX", 32.7767, -96.7970],
        ["Los Angeles, CA", 34.0522, -118.2437]
    ]
    print("\nHere are some example coordinates you can try:")
    print(tabulate(examples, headers=["City", "Latitude", "Longitude"], tablefmt="simple"))