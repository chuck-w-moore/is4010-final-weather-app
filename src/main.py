import sys
from src.utils import (
    validate_coordinates, 
    get_forecast_url, 
    get_forecast_data, 
    format_forecast_table, 
    print_examples,
    get_lat_lon_from_city
)

def main():
    print("=" * 60)
    print("      Welcome to the US Weather CLI App!")
    print("=" * 60)
    
    # Show examples so they know the format
    print_examples()
    
    print("\nType 'exit' at any time to quit.")

    while True:
        print("\n" + "-" * 40)
        # Direct prompt for city - no menu needed
        city_input = input("Enter a US City (e.g., 'Miami, FL'): ").strip()
        
        if city_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break

        if not city_input:
            continue

        print(f"Searching for '{city_input}'...")
        
        # 1. Geocoding (City -> Lat/Lon)
        lat, lon, display_name = get_lat_lon_from_city(city_input)
        
        if lat is None:
            print(f"[!] Could not find location '{city_input}'. Please try again.")
            continue
        
        # 2. Validate Bounds (Must be in US)
        if not validate_coordinates(lat, lon):
            print(f"\n[!] Error: '{display_name}' appears to be outside the supported US area.")
            continue

        print(f"Found: {display_name}")
        
        # 3. Get Duration
        days = 1
        days_input = input("Forecast duration in days (1, 3, 7) [Default: 1]: ").strip()
        if days_input in ['1', '3', '7']:
            days = int(days_input)

        print(f"\nFetching forecast...")

        # 4. Fetch Weather Data
        forecast_url = get_forecast_url(lat, lon)
        if not forecast_url:
            continue

        periods = get_forecast_data(forecast_url)
        if not periods:
            continue

        # 5. Output Table
        print(f"\nThe forecast for {display_name}:")
        print(format_forecast_table(periods, days))

        # 6. Loop or Quit
        again = input("\nCheck another location? (y/n): ").lower()
        if again != 'y':
            print("Thanks for using the Weather App. Goodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        sys.exit(0)