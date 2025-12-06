# US Weather App CLI

## Project Overview

An interactive command-line application that allows users to fetch and display weather forecasts for specific locations within the United States. Unlike static scripts, this application utilizes **Geocoding** to allow users to search by City Name (e.g., "Miami, FL") rather than requiring manual coordinate entry.

#### Forecast Data Output:

| Data Point | Description |
| :--- | :--- |
| **Location** | The specific city and state identified by the Geocoding API. |
| **Period** | The specific timeframe (e.g., "This Afternoon", "Tonight", "Wednesday"). |
| **Temperature** | The predicted temperature in Fahrenheit or Celsius. |
| **Wind** | Wind speed and direction (e.g., "10 mph N"). |
| **Short Forecast** | A brief textual summary of the weather conditions. |

## API Integration

This project implements a **Dual-API architecture** to resolve location data and fetch weather details.

### 1. Location Services (Geocoding)
* **API:** OpenStreetMap (Nominatim)
* **Base URL:** `https://nominatim.openstreetmap.org/search`
* **Purpose:** Converts user input (City/State string) into Latitude and Longitude.
* **Key Endpoint:**
    * `?q={city}&format=json` - Returns geometric coordinates for the search query.

### 2. Weather Data
* **API:** U.S. National Weather Service (NWS)
* **Base URL:** `https://api.weather.gov`
* **Purpose:** Fetches the forecast grid and period data.
* **Key Endpoints:**
    * `/points/{lat},{lon}` - Determines the specific NWS grid station for the coordinates.
    * `/gridpoints/{office}/{gridX},{gridY}/forecast` - Returns the actual forecast data (periods, temperature, etc.).

## Usage

The application is fully interactive. To run the program:

```bash
python -m src.main
```

### Application Flow:
1.  **Welcome Screen:** Displays example cities and coordinates.
2.  **Input:** Prompts the user to enter a US City (e.g., "Cincinnati, OH").
3.  **Processing:**
    * Validates input.
    * Fetches coordinates via OpenStreetMap.
    * Validates that coordinates are within US boundaries.
    * Fetches weather grid via NWS.
4.  **Output:** Displays a formatted table of the weather forecast.
5.  **Loop:** Asks the user if they wish to search for another location.

## AI-Assisted Development Process
AI assistance was utilized for the following aspects of the project:
* **Initial project structure:** Building a draft of the project to improve upon.
* **Dual API Integration:** Implementing logic to chain requests between OpenStreetMap and the National Weather Service.
* **Error Handling:** Developing robust `try/except` blocks to handle API 403/404 errors and connection timeouts.
* **Interactive Interface:** Ensuring the application has interactive features and functions accordingly.
* **Formatting:** Using the `tabulate` library to dynamically resize and wrap text for CLI output.

## Technical Stack

* **Python 3.10+**
* **`requests`:** For handling HTTP GET requests to external APIs.
* **`tabulate`:** For rendering ASCII tables in the terminal.
* **`sys` & `json`:** For system operations and data parsing.

## Code Organization

* **`main.py`**
    * Contains the main application loop.
    * Handles user input (City names, forecast duration).
    * Orchestrates the flow between the user and the utility functions.

* **`src/utils.py`**
    * `get_lat_lon_from_city`: Handles interaction with the OpenStreetMap API.
    * `get_forecast_url` & `get_forecast_data`: Handles interactions with the NWS API.
    * `validate_coordinates`: Ensures locations are within the US geographic bounds.
    * `format_forecast_table`: Processes raw JSON into a readable table format.

## Standards

* **Docstrings:** Included for all major functions to explain inputs and returns.
* **PEP 8:** Code follows standard Python styling guidelines.
* **Handle errors gracefully:** (e.g., API errors, invalid user input) using `try/except` and 
* **API:** Mock all external API calls in tests.


## Reflection

### Successes

- Gemini built great boilerplate code to build upon.
- Debugging was simple using AI by building well-structured prompts.
- Gemini was excellent at properly writing docstrings for functions.

### Challenges

- Gemini struggles to build markdown files, as it renders the markdown in its response.
- Integrating two API's was difficult at first, but after many trials & errors and careful debugging it succeeded.

### Learning Impact

- Utilizing AI allowed me to go above and beyond my technical capabilities while also learning lots about API integration.
- I made a focus of perfecting the user experience, python application structure, and logic behind functions.
- I allowed Gemini to focus on generating a strong boilerplate and generating logic which I needed assistance with.